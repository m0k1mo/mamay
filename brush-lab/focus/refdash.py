"""Fetch Refs v3 own sheets and build the reference | ours dashboard.
usage: python3 refdash.py <dir> [pairH] [perPage]"""
import sys;sys.path.insert(0,'/home/claude/lab')
import re,urllib.request,urllib.parse,time,sys,os,json,glob
from PIL import Image,ImageDraw,ImageFont
out=sys.argv[1];os.makedirs(out,exist_ok=True)
PH=int(sys.argv[2]) if len(sys.argv)>2 else 360
PER=int(sys.argv[3]) if len(sys.argv)>3 else 10
FB=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',max(14,PH//18))
FS=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',max(12,PH//22))
D={x['n']:x for x in json.load(open('/home/claude/school/all_results.json'))}
B='https://raw.githubusercontent.com/m0k1mo/mamay/brush-lab-out/'
from ghraw import raw
rep=raw('report.md').decode()
own={int(m.group(1)):(m.group(2),m.group(3)) for m in re.finditer(r'!\[Refs v3 · #(\d+) ([^\]]*?) — own sheet\]\(([^)]+)\)',rep)}
from autocfg import CFG
CROP={k:v['crop'] for k,v in CFG.items() if 'crop' in v}
SC=json.load(open(f'{out}/scores.json')) if os.path.exists(f'{out}/scores.json') else {}
def get(n,fn):
    p=f'{out}/o{n:02d}.png'
    if os.path.exists(p) and '--cached' in sys.argv: return p
    for t in range(5):
        try: raw(fn,p);return p
        except Exception: time.sleep(3)
    return None
ns=sorted(own);print(len(ns),'sheets')
pairs=[]
for n in ns:
    name,fn=own[n];p=get(n,fn)
    a=Image.open(glob.glob('/home/claude/refs/img/'+D[n]['id']+'*')[0]).convert('RGB')
    cr=CROP.get(n)
    if cr: w_,h_=a.size;a=a.crop((int(cr[0]*w_),int(cr[1]*h_),int(cr[2]*w_),int(cr[3]*h_)))
    b=Image.open(p).convert('RGB')
    a=a.resize((int(a.width*PH/a.height),PH),Image.LANCZOS);b=b.resize((int(b.width*PH/b.height),PH),Image.LANCZOS)
    pairs.append((n,name,a,b))
G=12;head=int(PH*0.14)
cols=2
for pg in range((len(pairs)+PER-1)//PER):
    sub=pairs[pg*PER:(pg+1)*PER];cw=max(a.width+b.width for _,_,a,b in pairs)+3*G
    rows=(len(sub)+cols-1)//cols
    im=Image.new('RGB',(cols*cw+G,rows*(PH+head+G)+G),(246,245,242));dr=ImageDraw.Draw(im)
    for i,(n,name,a,b) in enumerate(sub):
        X=G+(i%cols)*cw;Y=G+(i//cols)*(PH+head+G)
        dr.text((X,Y),f"#{n:02d}  {name}",fill=(30,30,30),font=FB)
        s=SC.get(str(n))
        if s: dr.text((X+a.width+b.width+G-int(PH*0.5),Y),f"{s[0]}/10",fill=(0,120,0) if s[0]>=7 else (190,110,0) if s[0]>=5 else (190,0,0),font=FB)
        im.paste(a,(X,Y+head));im.paste(b,(X+a.width+G,Y+head))
    im.save(f'{out}/dash{pg+1}.jpg',quality=90)
print('pages',(len(pairs)+PER-1)//PER)
