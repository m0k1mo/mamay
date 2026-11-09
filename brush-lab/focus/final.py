"""Final deliverables: high-res dashboard pages + artifact assets/page."""
import sys,os,json,glob,textwrap
sys.path.insert(0,'/home/claude/lab');sys.path.insert(0,'/home/claude/lab/art')
from PIL import Image,ImageDraw,ImageFont
from autocfg import CFG
from scores import S,GROUP,MED
D={x['n']:x for x in json.load(open('/home/claude/school/all_results.json'))}
NM=__import__('mkrefs3').NM
CROP={k:v['crop'] for k,v in CFG.items() if 'crop' in v}
OURS={n:f'/home/claude/lab/d4/o{n:02d}.png' for n in range(1,51)}
for n in map(int,(sys.argv[1].split(',') if len(sys.argv)>1 and sys.argv[1] else [])): OURS[n]=f'/home/claude/lab/d5/o{n:02d}.png'
def ref(n):
    a=Image.open(glob.glob('/home/claude/refs/img/'+D[n]['id']+'*')[0]).convert('RGB');cr=CROP.get(n)
    if cr: w,h=a.size;a=a.crop((int(cr[0]*w),int(cr[1]*h),int(cr[2]*w),int(cr[3]*h)))
    return a
OUT='/home/claude/lab/final';os.makedirs(OUT,exist_ok=True)
# ---- dashboard pages
PH=1000;G=36;FB=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',40)
FS=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',28);FL=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',22)
COL={'g':(47,125,75),'m':(168,112,14),'l':(184,52,28)}
pairs=[]
for n in range(1,51):
    a=ref(n);b=Image.open(OURS[n]).convert('RGB')
    a2=a.resize((int(a.width*PH/a.height),PH),Image.LANCZOS);b2=b.resize((int(b.width*PH/b.height),PH),Image.LANCZOS)
    pairs.append((n,a,b,a2,b2))
cw=max(a2.width+b2.width for *_,a2,b2 in pairs)+G*3;head=150;cols=2;rows=3;per=cols*rows
pages=[]
for pg in range((50+per-1)//per):
    sub=pairs[pg*per:(pg+1)*per];r=(len(sub)+1)//2
    im=Image.new('RGB',(cols*cw+G,r*(PH+head+G)+G+70),(236,238,237));d=ImageDraw.Draw(im)
    d.text((G,G-6),f"Brush Lab — 50 references · page {pg+1} of {(50+per-1)//per} · left: reference, right: Mamay",fill=(90,96,95),font=FS)
    for i,(n,a,b,a2,b2) in enumerate(sub):
        X=G+(i%cols)*cw;Y=G+60+(i//cols)*(PH+head+G);sc,note=S[n]
        d.text((X,Y),f"#{n:02d}  {NM[n]}",fill=(27,30,31),font=FB)
        c=COL['g'] if sc>=7 else COL['m'] if sc>=5 else COL['l']
        d.text((X+a2.width+b2.width+G-150,Y),f"{sc}/10",fill=c,font=FB)
        d.text((X,Y+56),textwrap.shorten(note,120),fill=(70,76,75),font=FL)
        d.text((X,Y+90),f"{GROUP[n]} · {MED.get(n,MED[GROUP[n]])}",fill=(120,126,125),font=FL)
        im.paste(a2,(X,Y+head-20));im.paste(b2,(X+a2.width+G,Y+head-20))
    p=f'{OUT}/brush-lab-50-page{pg+1}.jpg';im.save(p,quality=88);pages.append(p)
print('pages',pages)
# ---- artifact assets
A='/home/claude/lab/art/site';
for sub in ('r','o','rt','ot'): os.makedirs(f'{A}/{sub}',exist_ok=True)
data=[]
for n,a,b,_,_ in pairs:
    def save(img,path,W,q):
        im=img.copy();im.thumbnail((W,W*2),Image.LANCZOS);im.save(path,quality=q,optimize=True);return im.size
    # same box for both so the wipe lines up
    W=1400;bw=b.resize((W,int(b.height*W/b.width)),Image.LANCZOS);aw=a.resize(bw.size,Image.LANCZOS)
    aw.save(f'{A}/r/{n:02d}.jpg',quality=86,optimize=True);bw.save(f'{A}/o/{n:02d}.jpg',quality=86,optimize=True)
    t=(600,int(bw.height*600/W));aw.resize(t,Image.LANCZOS).save(f'{A}/rt/{n:02d}.jpg',quality=82);bw.resize(t,Image.LANCZOS).save(f'{A}/ot/{n:02d}.jpg',quality=82)
    g=GROUP[n];data.append(dict(n=n,name=NM[n],group=g,medium=MED.get(n,MED[g]),score=S[n][0],note=S[n][1],
        r=f'r/{n:02d}.jpg',o=f'o/{n:02d}.jpg',rt=f'rt/{n:02d}.jpg',ot=f'ot/{n:02d}.jpg',tw=t[0],th=t[1]))
meta=dict(lede="Each sheet copies its reference with the matching medium — oil, ink, watercolour, gouache, dry sticks — painted by Mamay's own paint engine (v3.2) in the Brush Lab at 1600 px. Tap a pair to compare side by side or with the wipe slider. Notes are the Brush Artist's honest verdicts.",prev="4.9",res="1600 px")
html=open('/home/claude/lab/art/template.html').read().replace('__DATA__',json.dumps(data,ensure_ascii=False)).replace('__META__',json.dumps(meta,ensure_ascii=False))
open(f'{A}/index.html','w').write(html)
tot=sum(os.path.getsize(p) for p in glob.glob(f'{A}/*/*.jpg'));print('assets MB',round(tot/1e6,1),len(glob.glob(f'{A}/*/*.jpg')))
