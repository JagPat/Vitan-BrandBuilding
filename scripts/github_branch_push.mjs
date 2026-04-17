#!/usr/bin/env node

import { execFile } from "node:child_process";
import { promisify } from "node:util";

const execFileAsync = promisify(execFile);
const WORKFLOW_PREFIX = ".github/workflows/";

function usage() {
  console.error(
    "Usage: node scripts/github_branch_push.mjs [--branch name] [--remote origin] [--cwd path] [--dry-run] [--json]",
  );
}

export function parseArgs(argv) {
  const parsed = {
    branch: "",
    remote: "origin",
    cwd: process.cwd(),
    dryRun: false,
    asJson: false,
  };

  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];
    if (arg === "--branch") {
      const value = argv[i + 1];
      if (!value) throw new Error("Missing value for --branch");
      parsed.branch = value;
      i += 1;
      continue;
    }
    if (arg === "--remote") {
      const value = argv[i + 1];
      if (!value) throw new Error("Missing value for --remote");
      parsed.remote = value;
      i += 1;
      continue;
    }
    if (arg === "--cwd") {
      const value = argv[i + 1];
      if (!value) throw new Error("Missing value for --cwd");
      parsed.cwd = value;
      i += 1;
      continue;
    }
    if (arg === "--dry-run") {
      parsed.dryRun = true;
      continue;
    }
    if (arg === "--json") {
      parsed.asJson = true;
      continue;
    }
    if (arg === "--help" || arg === "-h") {
      usage();
      process.exit(0);
    }
    throw new Error(`Unknown argument: ${arg}`);
  }

  return parsed;
}

async function runGit(args, options = {}) {
  return execFileAsync("git", args, {
    cwd: options.cwd,
    env: options.env,
    maxBuffer: 10 * 1024 * 1024,
  });
}

async function resolveCurrentBranch(cwd) {
  const result = await runGit(["rev-parse", "--abbrev-ref", "HEAD"], { cwd });
  const branch = String(result.stdout || "").trim();
  if (!branch || branch === "HEAD") {
    throw new Error("Detached HEAD is not supported; pass --branch explicitly from a branch checkout.");
  }
  return branch;
}

async function remoteTrackingExists(cwd, remote, branch) {
  try {
    await runGit(["rev-parse", "--verify", `refs/remotes/${remote}/${branch}`], { cwd });
    return true;
  } catch {
    return false;
  }
}

function parsePaths(stdout) {
  return String(stdout || "")
    .split(/\r?\n/)
    .map((line) => line.trim())
    .filter(Boolean);
}

export async function detectChangedPaths({ cwd, remote, branch }) {
  if (await remoteTrackingExists(cwd, remote, branch)) {
    const result = await runGit(
      ["diff", "--name-only", `refs/remotes/${remote}/${branch}...HEAD`],
      { cwd },
    );
    return parsePaths(result.stdout);
  }

  const result = await runGit(["diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD"], {
    cwd,
  });
  return parsePaths(result.stdout);
}

export function hasWorkflowChanges(paths) {
  return paths.some((entry) => entry.startsWith(WORKFLOW_PREFIX));
}

export function resolvePushAuth(env, requiresWorkflowScope) {
  if (requiresWorkflowScope) {
    const workflowToken = env.GITHUB_WORKFLOW_PAT_VITAN?.trim();
    if (!workflowToken) {
      throw new Error(
        "Workflow changes detected but GITHUB_WORKFLOW_PAT_VITAN is not set. Provision a GitHub token with workflow scope, then retry with this helper.",
      );
    }
    return {
      mode: "workflow_pat",
      tokenEnvKey: "GITHUB_WORKFLOW_PAT_VITAN",
    };
  }

  if (env.GITHUB_PAT_VITAN?.trim()) {
    return {
      mode: "default_pat",
      tokenEnvKey: "GITHUB_PAT_VITAN",
    };
  }

  if (env.GITHUB_WORKFLOW_PAT_VITAN?.trim()) {
    return {
      mode: "workflow_pat_fallback",
      tokenEnvKey: "GITHUB_WORKFLOW_PAT_VITAN",
    };
  }

  throw new Error(
    "No GitHub push token is available. Set GITHUB_PAT_VITAN for normal pushes or GITHUB_WORKFLOW_PAT_VITAN for workflow-file pushes.",
  );
}

function credentialHelperValue(tokenEnvKey) {
  return `!f() { test "$1" = get || exit 0; echo username=x-access-token; echo "password=$${tokenEnvKey}"; }; f`;
}

export function buildPushArgs({ remote, branch, tokenEnvKey, dryRun }) {
  const args = [
    "-c",
    `credential.https://github.com.helper=${credentialHelperValue(tokenEnvKey)}`,
    "push",
  ];
  if (dryRun) args.push("--dry-run");
  args.push(remote, `HEAD:refs/heads/${branch}`);
  return args;
}

export async function pushBranch(options, execGit = runGit) {
  const branch = options.branch || (await resolveCurrentBranch(options.cwd));
  const changedPaths = await detectChangedPaths({
    cwd: options.cwd,
    remote: options.remote,
    branch,
  });
  const workflowChanges = hasWorkflowChanges(changedPaths);
  const auth = resolvePushAuth(process.env, workflowChanges);
  const args = buildPushArgs({
    remote: options.remote,
    branch,
    tokenEnvKey: auth.tokenEnvKey,
    dryRun: options.dryRun,
  });

  try {
    const result = await execGit(args, { cwd: options.cwd, env: process.env });
    return {
      ok: true,
      branch,
      remote: options.remote,
      dryRun: options.dryRun,
      workflowChanges,
      authMode: auth.mode,
      tokenEnvKey: auth.tokenEnvKey,
      changedPaths,
      stdout: String(result.stdout || "").trim(),
      stderr: String(result.stderr || "").trim(),
      pushArgs: args,
    };
  } catch (error) {
    const stderr = error instanceof Error && "stderr" in error ? String(error.stderr || "").trim() : "";
    const stdout = error instanceof Error && "stdout" in error ? String(error.stdout || "").trim() : "";
    const message = error instanceof Error ? error.message : String(error);
    return {
      ok: false,
      branch,
      remote: options.remote,
      dryRun: options.dryRun,
      workflowChanges,
      authMode: auth.mode,
      tokenEnvKey: auth.tokenEnvKey,
      changedPaths,
      stdout,
      stderr,
      pushArgs: args,
      error:
        stderr.includes("without `workflow` scope") || stderr.includes("without workflow scope")
          ? `${message}\nDetected workflow-scope rejection from GitHub. The configured ${auth.tokenEnvKey} value still does not have workflow scope.`
          : message,
    };
  }
}

export function renderMarkdown(result) {
  const lines = ["## GitHub Branch Push", ""];
  lines.push(`- Branch: \`${result.branch}\``);
  lines.push(`- Remote: \`${result.remote}\``);
  lines.push(`- Workflow changes: \`${result.workflowChanges ? "yes" : "no"}\``);
  lines.push(`- Auth mode: \`${result.authMode}\``);
  lines.push(`- Token env: \`${result.tokenEnvKey}\``);
  lines.push(`- Dry run: \`${result.dryRun ? "yes" : "no"}\``);
  lines.push(
    `- Changed paths: ${result.changedPaths.length > 0 ? result.changedPaths.map((entry) => `\`${entry}\``).join(", ") : "none detected"}`,
  );
  lines.push("");
  if (result.ok) {
    lines.push("Push completed successfully.");
  } else {
    lines.push("Push failed.");
    lines.push("");
    lines.push("```text");
    lines.push(result.error || result.stderr || "Unknown push failure");
    lines.push("```");
  }
  return `${lines.join("\n")}\n`;
}

async function main() {
  const options = parseArgs(process.argv.slice(2));
  const result = await pushBranch(options);
  if (options.asJson) {
    process.stdout.write(`${JSON.stringify(result, null, 2)}\n`);
  } else {
    process.stdout.write(renderMarkdown(result));
  }
  if (!result.ok) process.exit(1);
}

if (import.meta.url === `file://${process.argv[1]}`) {
  main().catch((error) => {
    console.error(error.message || String(error));
    process.exit(1);
  });
}
