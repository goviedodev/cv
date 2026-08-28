#!/usr/bin/env bash
payload=$(cat)
tool_name=$(printf '%s' "$payload" | jq -r '.tool_name // ""')
tool_input=$(printf '%s' "$payload" | jq -c '.tool_input // {}')

if ! printf '%s' "$tool_input" | grep -qi 'indeed\.com'; then
  exit 0
fi

if [ "$tool_name" = "Bash" ]; then
  # Only guard Bash calls that actually launch/drive a browser — not incidental
  # mentions of indeed.com (e.g. logging a URL to cv_job_links.md).
  cmd=$(printf '%s' "$tool_input" | jq -r '.command // ""')
  if ! printf '%s' "$cmd" | grep -qiE 'chrome-devtools-axi|google-chrome|chromium'; then
    exit 0
  fi
fi

profile17_ok=0
while IFS= read -r line; do
  [ -z "$line" ] && continue
  has_debug=$(printf '%s' "$line" | grep -c -- '--remote-debugging-port=')
  [ "$has_debug" -eq 0 ] && continue
  udd=$(printf '%s' "$line" | grep -oP -- '(?<=--user-data-dir=)[^ ]+' | head -1)
  pd=$(printf '%s' "$line" | grep -oP -- '(?<=--profile-directory=)[^ ]+' | head -1)
  [ -z "$udd" ] && udd="$HOME/.config/google-chrome"
  [ -z "$pd" ] && pd="Default"
  prefs="$udd/$pd/Preferences"
  if [ -f "$prefs" ] && grep -q 'goviedo.laboral@gmail.com' "$prefs"; then
    profile17_ok=1
    break
  fi
done < <(pgrep -x chrome -a 2>/dev/null)

if [ "$profile17_ok" = "1" ]; then
  echo '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"allow"}}'
else
  reason='Indeed (indeed.com) must only be opened under a Chrome instance signed in as goviedo.laboral@gmail.com (Profile 17), never Default, and it must have --remote-debugging-port set so this can be verified. No such instance is currently running/verifiable. Launch one first (e.g. a --user-data-dir copy of Profile 17 with --remote-debugging-port=<port>), then point chrome-devtools-axi or claude-in-chrome select_browser/switch_browser at it before retrying.'
  reason_json=$(printf '%s' "$reason" | jq -Rs .)
  echo "{\"hookSpecificOutput\":{\"hookEventName\":\"PreToolUse\",\"permissionDecision\":\"deny\",\"permissionDecisionReason\":${reason_json}}}"
fi
