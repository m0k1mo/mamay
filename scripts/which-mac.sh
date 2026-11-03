#!/bin/bash
# which-mac.sh — where to build (Artem 03.11: «тільки мої ресурси, а якщо я не в мережі — гіт»; 18:45: «сам відслідковуй»).
# Prints artem-mac when Artem's Mac (self-hosted runner «artem-mac») answers, else xcode-27 (GitHub's Mac).
# 1. scripts/prefer-runner.txt: artem-mac / xcode-27 force it; auto (or nothing) → ask the Mac.
# 2. The Mac is busy with a job of this repo → it is there: artem-mac (the job waits its turn: one heavy job at a time).
# 3. Ping: start «Mac ping» (mac-ping.yml) and wait up to 75 s for it to start on artem-mac; no → cancel it, xcode-27.
# Needs GH_TOKEN = the workflow's own token with «actions: write» (no admin token).
REPO=${1:-m0k1mo/mamay}
API="https://api.github.com/repos/$REPO"
H=(-H "Authorization: Bearer $GH_TOKEN" -H "Accept: application/vnd.github+json")
P=$(curl -fsSL "https://raw.githubusercontent.com/$REPO/main/scripts/prefer-runner.txt" 2>/dev/null | tr -d '[:space:]')
if [ "$P" = artem-mac ] || [ "$P" = xcode-27 ]; then echo "$P"; echo "preferred: $P (scripts/prefer-runner.txt)" >&2; exit 0; fi
# busy?
BUSY=$(curl -fsS "${H[@]}" "$API/actions/runs?status=in_progress&per_page=30" 2>/dev/null | python3 -c "
import json,sys,urllib.request,os
d=json.load(sys.stdin); me=os.environ.get('GITHUB_RUN_ID','')
for r in d.get('workflow_runs',[]):
    if str(r['id'])==me: continue
    q=urllib.request.Request(r['jobs_url'],headers={'Authorization':'Bearer '+os.environ['GH_TOKEN'],'Accept':'application/vnd.github+json'})
    try: j=json.load(urllib.request.urlopen(q,timeout=10))
    except Exception: continue
    if any(x.get('status')=='in_progress' and x.get('runner_name')=='artem-mac' for x in j.get('jobs',[])): print('busy'); break
" 2>/dev/null)
if [ "$BUSY" = busy ]; then echo artem-mac; echo "Artem's Mac: busy with another job — online, this one waits its turn" >&2; exit 0; fi
# ping
TAG="${GITHUB_RUN_ID:-hand}-${GITHUB_RUN_ATTEMPT:-1}-$RANDOM"
curl -fsS -X POST "${H[@]}" "$API/actions/workflows/mac-ping.yml/dispatches" -d "{\"ref\":\"main\",\"inputs\":{\"tag\":\"$TAG\"}}" >/dev/null 2>&1 \
  || { echo xcode-27; echo "Artem's Mac: could not start the ping (token) — GitHub's Mac" >&2; exit 0; }
STATE=none; RID=""
for i in $(seq 1 25); do
  sleep 3
  RUN=$(curl -fsS "${H[@]}" "$API/actions/workflows/mac-ping.yml/runs?per_page=10" 2>/dev/null | python3 -c "
import json,sys
for r in json.load(sys.stdin).get('workflow_runs',[]):
    if '$TAG' in (r.get('display_title') or ''): print(r['id'], r['status'], r.get('conclusion') or ''); break" 2>/dev/null)
  [ -z "$RUN" ] && continue
  RID=${RUN%% *}
  ST=$(curl -fsS "${H[@]}" "$API/actions/runs/$RID/jobs" 2>/dev/null | python3 -c "
import json,sys
j=json.load(sys.stdin).get('jobs',[])
print(j[0]['status'] if j else 'none')" 2>/dev/null)
  if [ "$ST" = in_progress ] || [ "$ST" = completed ]; then STATE=online; break; fi
done
if [ "$STATE" = online ]; then echo artem-mac; echo "Artem's Mac: answered the ping" >&2
else
  [ -n "$RID" ] && curl -fsS -X POST "${H[@]}" "$API/actions/runs/$RID/cancel" >/dev/null 2>&1
  echo xcode-27; echo "Artem's Mac: no answer in 75 s (asleep, off or offline) — GitHub's Mac" >&2
fi
