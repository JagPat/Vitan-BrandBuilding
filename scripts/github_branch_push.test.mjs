import test from "node:test";
import assert from "node:assert/strict";
import {
  buildPushArgs,
  hasWorkflowChanges,
  parseArgs,
  resolvePushAuth,
} from "./github_branch_push.mjs";

test("parseArgs uses defaults", () => {
  const parsed = parseArgs([]);
  assert.equal(parsed.branch, "");
  assert.equal(parsed.remote, "origin");
  assert.equal(parsed.dryRun, false);
  assert.equal(parsed.asJson, false);
});

test("hasWorkflowChanges detects workflow paths only", () => {
  assert.equal(hasWorkflowChanges(["README.md", "scripts/task.py"]), false);
  assert.equal(hasWorkflowChanges([".github/workflows/build.yml"]), true);
});

test("resolvePushAuth prefers dedicated workflow token for workflow changes", () => {
  const resolved = resolvePushAuth(
    {
      GITHUB_PAT_VITAN: "default-token",
      GITHUB_WORKFLOW_PAT_VITAN: "workflow-token",
    },
    true,
  );

  assert.deepEqual(resolved, {
    mode: "workflow_pat",
    tokenEnvKey: "GITHUB_WORKFLOW_PAT_VITAN",
  });
});

test("resolvePushAuth fails fast when workflow changes lack a workflow token", () => {
  assert.throws(
    () => resolvePushAuth({ GITHUB_PAT_VITAN: "default-token" }, true),
    /GITHUB_WORKFLOW_PAT_VITAN is not set/,
  );
});

test("buildPushArgs injects the selected token helper", () => {
  const args = buildPushArgs({
    remote: "origin",
    branch: "agent/fe",
    tokenEnvKey: "GITHUB_WORKFLOW_PAT_VITAN",
    dryRun: true,
  });

  assert.equal(args[0], "-c");
  assert.match(args[1], /credential\.https:\/\/github\.com\.helper=/);
  assert.match(args[1], /password=\$GITHUB_WORKFLOW_PAT_VITAN/);
  assert.deepEqual(args.slice(2), ["push", "--dry-run", "origin", "HEAD:refs/heads/agent/fe"]);
});
