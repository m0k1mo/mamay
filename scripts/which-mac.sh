#!/bin/bash
# which-mac.sh — where to build (Artem 03.11, 01:54: «тільки мої ресурси, а якщо я не в мережі — гіт»).
# Prints artem-mac when Artem's Mac (self-hosted runner «artem-mac») is online, else xcode-27 (GitHub's Mac).
# Needs a token that may read the repo's runners (GH_TOKEN; FORMLAB_CODE_TOKEN if it has «Administration: read» on m0k1mo/mamay).
# A token that cannot read them → xcode-27, said in the log.
REPO=${1:-m0k1mo/mamay}
# the lead's switch (scripts/prefer-runner.txt): artem-mac while Artem is at home with his Mac, xcode-27, or auto (ask GitHub)
P=$(curl -fsSL "https://raw.githubusercontent.com/$REPO/main/scripts/prefer-runner.txt" 2>/dev/null | tr -d '[:space:]')
if [ "$P" = artem-mac ] || [ "$P" = xcode-27 ]; then echo "$P"; echo "preferred: $P (scripts/prefer-runner.txt)" >&2; exit 0; fi
S=$(curl -fsS -H "Authorization: Bearer $GH_TOKEN" -H "Accept: application/vnd.github+json" \
      "https://api.github.com/repos/$REPO/actions/runners?per_page=100" 2>/dev/null \
    | python3 -c "
import json,sys
d=json.load(sys.stdin)
st=[r['status'] for r in d.get('runners',[]) if 'artem-mac' in [l['name'] for l in r.get('labels',[])]]
print('online' if 'online' in st else (st[0] if st else 'missing'))" 2>/dev/null) || S="unknown (the token cannot read the runners)"
if [ "$S" = online ]; then echo artem-mac; else echo xcode-27; fi
echo "Artem's Mac: $S" >&2
