#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, requests, json, datetime

AGENT_NAMES = {
    "eda59c6a-8b69-4bc9-b8e8-b8a477a11749": "Business Builder",
    "5dbbd0b4-4ae8-4e2a-b924-f8a2ed082e2a": "Digital Presence Mgr",
    "006f1cc1-6f96-40fe-90da-a7fe3d8b9319": "HR",
    "1b2e7035-dc4b-46ce-9125-a6713d1ba51d": "Brand Storyteller",
    "133b32e0-22c4-4b1f-a15c-2bbee6d2bc50": "Principle Architect",
    "333972c1-2e03-417e-b881-d4b6edce7411": "Outreach Coordinator",
    "ed683b84-7a68-4569-ba19-356a15c63911": "Founding Engineer",
}

BASE_URL = os.environ.get("PAPERCLIP_PUBLIC_URL", "https://paperclip.vitan.in")

def issue_link(identifier, title=None, style="id"):
    url = f"{BASE_URL}/VITA/issues/{identifier}"
    if style == "id":
        return (f'<a href="{url}" style="color:#D42B2B;text-decoration:none;'
                f'border-bottom:1px dashed #D42B2B;font-family:SF Mono,Consolas,monospace;'
                f'font-size:12px;font-weight:600;">{identifier}</a>')
    else:
        t = (title or identifier)[:60]
        return f'<a href="{url}" style="color:#1A1A1A;text-decoration:none;">{t}</a>'

def agent_badge(agent_id):
    name = AGENT_NAMES.get(agent_id, agent_id[:8] if agent_id else "Unassigned")
    return (f'<span style="background:#f0f0f0;color:#4A4A4A;padding:2px 8px;'
            f'border-radius:10px;font-size:11px;">{name}</span>')

def status_badge(status):
    styles = {
        "blocked": "background:#FFEBEE;color:#C62828",
        "in_progress": "background:#E3F2FD;color:#1565C0",
        "todo": "background:#FFF3E0;color:#E65100",
        "done": "background:#E8F5E9;color:#2E7D32",
        "backlog": "background:#F3E5F5;color:#6A1B9A",
        "in_review": "background:#E8EAF6;color:#283593",
        "cancelled": "background:#F5F5F5;color:#9E9E9E",
    }
    s = styles.get(status, "background:#F5F5F5;color:#9E9E9E")
    return (f'<span style="{s};padding:2px 8px;border-radius:10px;font-size:11px;font-weight:600;">'
            f'{status.replace("_"," ").upper()}</span>')

def issue_row(i, show_status=False):
    aid = i.get("assigneeAgentId")
    status_col = f"<td style='padding:6px 8px;'>{status_badge(i.get('status',''))}</td>" if show_status else ""
    agent_cell = agent_badge(aid) if aid else '<span style="color:#9E9E9E;font-size:11px;">Unassigned</span>'
    return (f'<tr style="border-bottom:1px solid #F0F0F0;">'
            f'<td style="padding:6px 8px;white-space:nowrap;">{issue_link(i["identifier"])}</td>'
            f'<td style="padding:6px 8px;">{issue_link(i["identifier"], i["title"], style="title")}</td>'
            f'{status_col}'
            f'<td style="padding:6px 8px;">{agent_cell}</td>'
            f'</tr>')

# Get OAuth token
resp = requests.post(
    f'https://{os.environ["OAUTH_ACCOUNTS_HOST"]}/oauth/v2/token',
    data={
        'grant_type': 'refresh_token',
        'client_id': os.environ['ZOHO_MAIL_CLIENT_ID'],
        'client_secret': os.environ['ZOHO_MAIL_CLIENT_SECRET'],
        'refresh_token': os.environ['ZOHO_MAIL_REFRESH_TOKEN'],
    }
)
access_token = resp.json()['access_token']

# Fetch issues
api_url = os.environ['PAPERCLIP_API_URL']
api_key = os.environ['PAPERCLIP_API_KEY']
company_id = os.environ['PAPERCLIP_COMPANY_ID']

issues_resp = requests.get(
    f"{api_url}/api/companies/{company_id}/issues?limit=200",
    headers={"Authorization": f"Bearer {api_key}"}
)
issues_raw = issues_resp.json()
issues = issues_raw if isinstance(issues_raw, list) else issues_raw.get('issues', [])

agents_resp = requests.get(
    f"{api_url}/api/companies/{company_id}/agents",
    headers={"Authorization": f"Bearer {api_key}"}
)
agents_raw = agents_resp.json()
agents = agents_raw if isinstance(agents_raw, list) else agents_raw.get('agents', [])

# IST timezone
ist_offset = datetime.timedelta(hours=5, minutes=30)
now_utc = datetime.datetime.utcnow()
now_ist = now_utc + ist_offset
midnight_ist = now_ist.replace(hour=0, minute=0, second=0, microsecond=0)
midnight_utc = midnight_ist - ist_offset

completed_today, needs_attention, in_progress_list, blocked_list, tomorrow_queue = [], [], [], [], []

for i in issues:
    status = i.get('status')
    if status == 'done':
        try:
            upd = i.get('updatedAt', '')
            upd_dt = datetime.datetime.fromisoformat(upd.replace('Z', '+00:00')).replace(tzinfo=None)
            if upd_dt >= midnight_utc:
                completed_today.append(i)
        except:
            pass
    elif status == 'in_progress':
        in_progress_list.append(i)
    elif status == 'blocked':
        blocked_list.append(i)
    elif status == 'in_review':
        needs_attention.append(i)
    elif status == 'todo' and not i.get('assigneeAgentId'):
        needs_attention.append(i)
    elif status == 'todo' and i.get('assigneeAgentId'):
        tomorrow_queue.append(i)
    elif status == 'backlog':
        tomorrow_queue.append(i)

# Agent active issue counts
agent_issue_counts = {}
for i in issues:
    if i.get('status') not in ('done', 'cancelled') and i.get('assigneeAgentId'):
        aid = i['assigneeAgentId']
        agent_issue_counts[aid] = agent_issue_counts.get(aid, 0) + 1

date_str = now_ist.strftime("%d %b %Y")
time_str = now_ist.strftime("%I:%M %p IST")

def fmt_heartbeat(hb):
    if not hb:
        return "Never"
    try:
        dt = datetime.datetime.fromisoformat(hb.replace('Z', '+00:00')).replace(tzinfo=None)
        ist_dt = dt + ist_offset
        return ist_dt.strftime("%H:%M IST")
    except:
        return hb[:16]

# Build agent health rows
agent_rows_html = ""
for a in agents:
    aid = a.get('id')
    name = AGENT_NAMES.get(aid, a.get('name', '?'))
    status = a.get('status', 'idle')
    hb = a.get('lastHeartbeatAt', '')
    count = agent_issue_counts.get(aid, 0)
    status_color = "#2E7D32" if status == "running" else "#4A4A4A"
    status_indicator = "\u25b6" if status == "running" else "\u25cf"
    status_html = f'<span style="color:{status_color};font-weight:600;">{status_indicator} {status.upper()}</span>'
    agent_rows_html += (
        f'<tr style="border-bottom:1px solid #F0F0F0;">'
        f'<td style="padding:8px 10px;font-weight:500;">{name}</td>'
        f'<td style="padding:8px 10px;">{status_html}</td>'
        f'<td style="padding:8px 10px;color:#4A4A4A;">{fmt_heartbeat(hb)}</td>'
        f'<td style="padding:8px 10px;text-align:center;font-weight:600;">{count}</td>'
        f'</tr>'
    )

# Build issue table sections
def section(title_html, color, border_color, rows_html, count, extra_note="", show_status_header=False):
    if not rows_html:
        return ""
    status_th = '<th style="padding:6px 8px;text-align:left;color:#4A4A4A;font-size:11px;font-weight:600;text-transform:uppercase;">Status</th>' if show_status_header else ""
    return f"""
  <div style="margin-bottom:28px;">
    <div style="font-size:13px;font-weight:700;color:{color};letter-spacing:1px;text-transform:uppercase;border-bottom:2px solid {border_color};padding-bottom:8px;margin-bottom:12px;">
      {title_html} ({count})
    </div>
    <table width="100%" cellpadding="0" cellspacing="0" style="font-size:13px;">
      <tr style="background:#F9F9F9;">
        <th style="padding:6px 8px;text-align:left;color:#4A4A4A;font-size:11px;font-weight:600;text-transform:uppercase;">ID</th>
        <th style="padding:6px 8px;text-align:left;color:#4A4A4A;font-size:11px;font-weight:600;text-transform:uppercase;">Title</th>
        {status_th}
        <th style="padding:6px 8px;text-align:left;color:#4A4A4A;font-size:11px;font-weight:600;text-transform:uppercase;">Agent</th>
      </tr>
      {rows_html}
    </table>
    {extra_note}
  </div>
"""

completed_rows = "".join(issue_row(i) for i in completed_today[:25])
extra_completed = ""
if len(completed_today) > 25:
    extra_completed = f'<div style="color:#9E9E9E;font-size:12px;padding:6px 8px;">+ {len(completed_today)-25} more completed today</div>'

attention_rows = "".join(issue_row(i, show_status=True) for i in needs_attention[:15])
inprog_rows = "".join(issue_row(i) for i in in_progress_list[:10])
blocked_rows = "".join(issue_row(i) for i in blocked_list[:10])
blocked_note = ""
if blocked_list:
    blocked_note = ('<div style="color:#9E9E9E;font-size:12px;margin-top:8px;padding:6px 8px;'
                    'background:#FFF8E1;border-radius:4px;">'
                    f'All {len(blocked_list)} blocked issues are awaiting assets (technical drawings, '
                    'high-res photos) from the board/client.</div>')
tomorrow_rows = "".join(issue_row(i, show_status=True) for i in tomorrow_queue[:10])

active_count = len(in_progress_list) + len(blocked_list) + len(needs_attention)

html = f"""<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"></head>
<body style="margin:0;padding:0;background:#F5F5F3;font-family:Segoe UI,Arial,sans-serif;">
<div style="max-width:680px;margin:24px auto;background:#FFFFFF;border-radius:8px;box-shadow:0 2px 12px rgba(0,0,0,0.08);overflow:hidden;">

  <div style="background:#D42B2B;padding:24px 32px;">
    <div style="color:#FFFFFF;font-size:11px;letter-spacing:2px;text-transform:uppercase;opacity:0.85;">Vitan Growth OS</div>
    <div style="color:#FFFFFF;font-size:22px;font-weight:700;margin-top:6px;">Evening Digest</div>
    <div style="color:rgba(255,255,255,0.85);font-size:13px;margin-top:4px;">{date_str} &nbsp;&middot;&nbsp; {time_str}</div>
  </div>

  <div style="padding:20px 32px;background:#FAFAFA;border-bottom:1px solid #EEEEEE;">
    <table width="100%" cellpadding="0" cellspacing="0">
    <tr>
      <td style="text-align:center;padding:12px 8px;background:#E3F2FD;border-radius:6px;">
        <div style="font-size:28px;font-weight:700;color:#1565C0;">{active_count}</div>
        <div style="font-size:11px;color:#1565C0;font-weight:600;text-transform:uppercase;letter-spacing:1px;">Active Issues</div>
      </td>
      <td width="8"></td>
      <td style="text-align:center;padding:12px 8px;background:#E8F5E9;border-radius:6px;">
        <div style="font-size:28px;font-weight:700;color:#2E7D32;">{len(completed_today)}</div>
        <div style="font-size:11px;color:#2E7D32;font-weight:600;text-transform:uppercase;letter-spacing:1px;">Completed Today</div>
      </td>
      <td width="8"></td>
      <td style="text-align:center;padding:12px 8px;background:#FFEBEE;border-radius:6px;">
        <div style="font-size:28px;font-weight:700;color:#C62828;">{len(needs_attention)}</div>
        <div style="font-size:11px;color:#C62828;font-weight:600;text-transform:uppercase;letter-spacing:1px;">Need Attention</div>
      </td>
      <td width="8"></td>
      <td style="text-align:center;padding:12px 8px;background:#263238;border-radius:6px;">
        <div style="font-size:28px;font-weight:700;color:#FFFFFF;">{len(agents)}</div>
        <div style="font-size:11px;color:#90A4AE;font-weight:600;text-transform:uppercase;letter-spacing:1px;">Agents Active</div>
      </td>
    </tr>
    </table>
  </div>

  <div style="padding:24px 32px;">
  {section("&#x2705; Completed Today", "#2E7D32", "#E8F5E9", completed_rows, len(completed_today), extra_completed)}
  {section("&#x1F534; Needs Your Attention", "#C62828", "#FFEBEE", attention_rows, len(needs_attention), show_status_header=True)}
  {section("&#x1F504; Still In Progress", "#1565C0", "#E3F2FD", inprog_rows, len(in_progress_list))}
  {section("&#x1F7E1; Blocked", "#E65100", "#FFF3E0", blocked_rows, len(blocked_list), blocked_note)}
  {section("&#x1F4CB; Tomorrow's Queue", "#6A1B9A", "#F3E5F5", tomorrow_rows, len(tomorrow_queue), show_status_header=True)}

  <div style="margin-bottom:28px;">
    <div style="font-size:13px;font-weight:700;color:#263238;letter-spacing:1px;text-transform:uppercase;border-bottom:2px solid #ECEFF1;padding-bottom:8px;margin-bottom:12px;">
      &#x1F916; Agent Health
    </div>
    <table width="100%" cellpadding="0" cellspacing="0" style="font-size:13px;">
      <tr style="background:#F9F9F9;">
        <th style="padding:8px 10px;text-align:left;color:#4A4A4A;font-size:11px;font-weight:600;text-transform:uppercase;">Agent</th>
        <th style="padding:8px 10px;text-align:left;color:#4A4A4A;font-size:11px;font-weight:600;text-transform:uppercase;">Status</th>
        <th style="padding:8px 10px;text-align:left;color:#4A4A4A;font-size:11px;font-weight:600;text-transform:uppercase;">Last Heartbeat</th>
        <th style="padding:8px 10px;text-align:center;color:#4A4A4A;font-size:11px;font-weight:600;text-transform:uppercase;">Active Issues</th>
      </tr>
      {agent_rows_html}
    </table>
  </div>
  </div>

  <div style="background:#F5F5F3;padding:16px 32px;border-top:1px solid #EEEEEE;text-align:center;">
    <a href="{BASE_URL}/VITA/agents/all" style="color:#D42B2B;text-decoration:none;font-size:12px;">View All Agents &rarr;</a>
    <span style="color:#CCCCCC;margin:0 12px;">|</span>
    <span style="color:#9E9E9E;font-size:12px;">Vitan Growth OS &nbsp;&middot;&nbsp; {date_str}</span>
  </div>
</div>
</body>
</html>"""

# Send via Zoho Mail API
account_id = os.environ['ZOHO_MAIL_ACCOUNT_ID']
mail_payload = {
    "fromAddress": os.environ['ZOHO_MAIL_FROM_ADDRESS'],
    "toAddress": "jagrutpatel@gmail.com",
    "ccAddress": "chitrang@vitan.in,kaivana@vitan.in",
    "subject": f"\U0001f3d7\ufe0f Vitan Growth OS \u2014 Evening Digest [{date_str}]",
    "mailFormat": "html",
    "content": html,
}

send_resp = requests.post(
    f"https://mail.zoho.in/api/accounts/{account_id}/messages",
    headers={
        "Authorization": f"Zoho-oauthtoken {access_token}",
        "Content-Type": "application/json",
    },
    json=mail_payload
)
result = send_resp.json()
print(f"HTTP {send_resp.status_code}")
print(json.dumps(result, indent=2))
