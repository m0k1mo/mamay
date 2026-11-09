"""50 references on engine v3.2. Each sheet copies the reference's composition with the right medium.
usage: python3 mkrefs3.py <version> <K> [n,n,...]"""
import json,sys,math,random,glob
sys.path.insert(0,'/home/claude/lab')
from refkit import *
from PIL import Image
D={x['n']:x for x in json.load(open('/home/claude/school/all_results.json'))}
def aspect(n):
    im=Image.open(glob.glob('/home/claude/refs/img/'+D[n]['id']+'*')[0]);return im.height/im.width
NM={1:"HW peach cloud",2:"HW cream strokes",3:"HW navy contours",4:"HW grey cloud",5:"HW green in rust loops",6:"HW scrubbed grey",
7:"HW blue L and zigzag",8:"HW lilac crown basket",9:"HW white loops",10:"HW maroon loops",11:"HW purple balls",12:"HW black-olive cage",
13:"HW blue streaky form",14:"HW olive totem",15:"Ultramarine script",16:"Shrigley strokes",17:"Krovostok dry brush",18:"Twombly blue sticks",
19:"Guston charcoal hand",20:"Orange crayon",21:"Gritty dog contours",22:"Wasilewski brush poster",23:"Report dry white mask",24:"Picasso flat oil",
25:"Yellow heavy stroke",26:"Ink caricature",27:"Orange impasto swatch",28:"Miles Davis lines",29:"Shrigley asterisk",30:"Red gouache face",
31:"Warhol blotted line",32:"Thick orange swipes",33:"Red wet-in-wet flames",34:"Magenta oil patches",35:"Red band with runs",36:"Magenta letters flat",
37:"Oil still life",38:"Sanguine drawing",39:"Thick impasto weave",40:"Watercolour blooms",41:"Coloured pencil",42:"Pink shaggy pastel",
43:"Dragged black blocks",44:"Blue looping ribbon",45:"Pastel pepper",46:"Ink lips on wet paper",47:"Pink knife slabs",48:"Black bands with drips",
49:"Magenta letters round",50:"Swipes on seaside"}
BR={};SH={}
def B(name,recipe): BR[name]=recipe;return name
def sheet(n,title,strokes,bg,wet=0,settle=12):
    s={"width":int(C.W*C.K),"height":int(C.H*C.K),"background":bg,"settle":settle,"strokes":strokes}
    if wet: s["wet"]=wet
    SH[n]=(title,s)
def setup(n,W=800):
    C.W=W;C.H=round(W*aspect(n));random.seed(n*101)
F={}
def ref(n):
    def deco(f): F[n]=f;return f
    return deco
pi=math.pi
# ======================= Henry Ward =======================
@ref(1)
def r1():
    g=B("#01 ground",oil("#e9c9bf",0.3,"filbert",load=1,ent=0.5,stiff=0.4,dil=0.35,streak=0.06))
    t=B("#01 teal",oil("#21403e",0.12,"flat",ent=1.4,dil=0.3,streak=0.15,colors=["#2c4a46","#3a2430"]))
    p=B("#01 peach",oil("#f0b89a",0.11,"flat",load=0.7,dry=0.5,ent=1.6,pick=0.15))
    pv=B("#01 peach legs",oil("#f2bea2",0.045,"filbert",load=0.9,ent=1.4,pick=0.2))
    nv=B("#01 navy",oil("#1c2238",0.03,"round",load=0.9,dry=0.1,ent=0.8,p2s=0.8,streak=0))
    s=ground(g)
    v=vrows(t,0.18,0.3,0.82,0.86,7,lean=0.02);v[0]["dry"]=True;s+=v
    h=hrows(p,0.12,0.06,0.88,0.34,6,tilt=0.02);h[0]["dry"]=True;s+=h
    s+=[st(ln(0.2+0.6*k/5+R(-0.02,0.02),0.3,0.2+0.6*k/5+R(-0.03,0.03),0.86,R(-0.01,0.01)),pv,sp=R(300,500)) for k in range(6)]
    s+=[st(ell(0.3,0.92,0.13,0.035,0.9),nv,[0.7,1,0.9,1,0.5],300),st(ell(0.68,0.92,0.13,0.035,0.9),nv,[0.7,1,0.9,1,0.5],300)]
    return s,"#e9c9bf"
@ref(2)
def r2():
    g=B("#02 ground",oil("#e4e2da",0.3,"filbert",load=1,ent=0.5,stiff=0.4,dil=0.35,streak=0.04))
    o=B("#02 olive",oil("#252c1c",0.12,"flat",ent=1.3,dil=0.3,streak=0.12,colors=["#1d2418","#3a4228"]))
    c=B("#02 cream",oil("#e6e4b8",0.1,"flat",load=0.85,dry=0.35,ent=1.6,pick=0.25,gloss=0.25))
    cs=B("#02 cream scrub",oil("#ecead0",0.11,"filbert",load=0.5,dry=0.7,ent=1.7,pick=0.3))
    m=B("#02 maroon",oil("#3a0e12",0.09,"filbert",ent=1.2,dil=0.25))
    s=ground(g)
    a=hrows(o,0.08,0.1,0.92,0.72,6,tilt=-0.02);a[0]["dry"]=True;s+=a
    s+=[st(ell(0.45,0.88,0.1,0.06,1.6,shrink=0.6),m,sp=350)]
    b=hrows(c,0.1,0.12,0.88,0.7,7,tilt=-0.03,bend=0.02);b[0]["dry"]=True;s+=b
    s+=hrows(cs,0.15,0.15,0.85,0.65,4,tilt=-0.02,sp=(700,1000))
    return s,"#e4e2da"
@ref(3)
def r3():
    g=B("#03 ground",oil("#ede7dd",0.3,"filbert",load=1,ent=0.5,stiff=0.4,dil=0.35,streak=0.03))
    m=B("#03 maroon",oil("#4a1a14",0.1,"flat",ent=1.2,dil=0.2))
    gb=B("#03 grey band",oil("#7c8a90",0.11,"flat",ent=1.5,dil=0.3,streak=0.12,colors=["#8e9aa0","#9c8aa0"]))
    nv=B("#03 navy",oil("#151a3a",0.035,"round",load=0.95,dry=0.15,ent=1.0,p2s=0.85,streak=0.05))
    s=ground(g)
    a=hrows(m,0.3,0.03,0.72,0.16,3);a[0]["dry"]=True;s+=a
    s+=hrows(gb,0.2,0.32,0.8,0.62,5,tilt=0.01)
    L=[(0.3,0.25),(0.12,0.2),(0.04,0.33),(0.12,0.45),(0.06,0.58),(0.15,0.72),(0.3,0.66),(0.32,0.52)]
    Rr=[(0.68,0.24),(0.85,0.18),(0.96,0.3),(0.88,0.42),(0.95,0.55),(0.86,0.7),(0.7,0.66),(0.68,0.52)]
    s+=[st(poly(L,8,0.004),nv,[0.6,1,0.9,1,0.85,0.5],300),st(poly(Rr,8,0.004),nv,[0.6,1,0.9,1,0.85,0.5],300)]
    s+=[st(ln(0.2,0.31,0.8,0.32,0.01),nv,[0.8,1,0.9,0.6],420),st(ln(0.2,0.63,0.8,0.62,-0.01),nv,[0.8,1,0.9,0.6],420)]
    s+=[st(ell(0.2,0.8,0.12,0.08,0.8),nv,sp=320),st(ell(0.8,0.8,0.12,0.08,0.8),nv,sp=320)]
    return s,"#ede7dd"
def grey_cloud(tag,seed):
    random.seed(seed)
    g=B(f"#{tag} ochre",oil("#9a7a24",0.3,"filbert",load=1,ent=0.6,stiff=0.4,dil=0.3,streak=0.1))
    gr=B(f"#{tag} grey",oil("#b6babe",0.12,"flat",load=0.75,dry=0.45,ent=1.6,pick=0.1,dil=0.25,streak=0.06))
    gs=B(f"#{tag} grey scrub",oil("#c6cacc",0.13,"filbert",load=0.5,dry=0.75,ent=1.7,pick=0.15))
    rs=B(f"#{tag} rust",oil("#8a4c1c",0.1,"flat",ent=1.4,dil=0.3,colors=["#9a5c22","#6e3a18"]))
    oc=B(f"#{tag} ochre block",oil("#a88424",0.1,"flat",ent=1.4,dil=0.25))
    ol=B(f"#{tag} olive line",oil("#3a3a20",0.025,"round",ent=0.8,p2s=0.8))
    s=ground(g)
    a=hrows(oc,0.08,0.66,0.48,0.8,3);a[0]["dry"]=True;s+=a
    s+=hrows(rs,0.08,0.8,0.95,0.95,3)
    s+=hrows(oc,0.6,0.68,0.95,0.8,2)
    b=hrows(gr,0.06,0.07,0.94,0.64,9,tilt=0.01,bend=0.03);b[0]["dry"]=True;s+=b
    s+=hrows(gs,0.1,0.1,0.9,0.6,6,sp=(700,1000))
    s+=[st(ln(0.08,0.66,0.95,0.67,0.01),ol,sp=500),st(ln(0.08,0.81,0.95,0.8,-0.01),ol,sp=500)]
    return s,"#9a7a24"
@ref(4)
def r4(): return grey_cloud("04",4)
@ref(6)
def r6(): return grey_cloud("06",61)
@ref(5)
def r5():
    g=B("#05 paper",gouache("#f2ede6",0.3,"filbert",ent=0.3))
    bl=B("#05 sky",gouache("#8ad0ec",0.08,"flat",ent=0.8))
    rs=B("#05 rust",oil("#a33e1c",0.04,"round",ent=1.0,p2s=0.8,dil=0.3))
    gr=B("#05 green",oil("#3b6a50",0.06,"flat",ent=1.3,dil=0.3,colors=["#2e5a40","#5a7a50"]))
    pk=B("#05 pink",oil("#f2d6d6",0.12,"flat",load=0.7,dry=0.4,ent=1.5,dil=0.2))
    dg=B("#05 dark green",oil("#1d3628",0.1,"filbert",ent=1.2,dil=0.2))
    s=ground(g)+vrows(bl,0.0,0.0,0.06,1.0,2)+vrows(bl,0.94,0.0,1.0,1.0,2)
    a=hrows(gr,0.14,0.08,0.86,0.34,4);a[0]["dry"]=True;s+=a
    for cx in (0.3,0.62):
        s+=[st(ell(cx,0.21,0.17,0.13,1.3),rs,sp=320)]
    s+=hrows(pk,0.08,0.38,0.92,0.64,5)
    s+=[st(ell(0.32,0.82,0.18,0.12,2.2,shrink=0.7),dg,sp=300),st(ell(0.68,0.82,0.18,0.12,2.2,shrink=0.7),dg,sp=300)]
    return s,"#f2ede6"
@ref(7)
def r7():
    g=B("#07 lilac",oil("#e6e2ee",0.3,"filbert",load=1,ent=0.5,stiff=0.4,dil=0.35))
    w=B("#07 white scrub",oil("#f4f2f8",0.13,"filbert",load=0.5,dry=0.7,ent=1.7))
    bl=B("#07 blue",oil("#1e4a78",0.05,"flat",ent=1.2,dil=0.2))
    bk=B("#07 black",oil("#141414",0.04,"round",ent=1.0,p2s=0.8))
    pk=B("#07 pink",oil("#e88aa0",0.08,"flat",ent=1.3))
    oc=B("#07 ochre",oil("#c89038",0.035,"flat",ent=1.3,dry=0.4))
    yo=B("#07 yellow-olive",oil("#b8b030",0.08,"flat",ent=1.2))
    s=ground(g);a=hrows(w,0.05,0.05,0.95,0.7,7);a[0]["dry"]=True;s+=a
    s+=vrows(pk,0.72,0.1,0.95,0.32,3)
    s+=[st(poly([(0.2,0.08),(0.21,0.62),(0.24,0.78),(0.5,0.8)],6),bl,[0.9,1,1,0.95,0.8,0.5],350)]
    s+=[st(poly([(0.3,0.72),(0.4,0.45),(0.46,0.66),(0.56,0.42),(0.6,0.7),(0.72,0.5),(0.8,0.62)],5),bk,[0.8,1,0.9,1,0.9,0.5],380)]
    s+=[st(poly([(0.75,0.12),(0.86,0.1),(0.9,0.25),(0.8,0.3),(0.75,0.12)],6),bk,sp=330)]
    for k in range(7):
        a_=pi*0.6+k*0.18;s.append(st(ln(0.02,0.4,0.02+0.16*math.cos(a_-pi/2+pi),0.4+0.16*math.sin(a_),0.005),oc,sp=500))
    s+=hrows(yo,0.05,0.86,0.35,0.95,2)+hrows(yo,0.6,0.82,0.9,0.9,2)
    s+=[st(poly([(0.0,1.0),(0.1,0.82),(0.18,1.0)],8),bk,sp=400),st(poly([(0.38,1.0),(0.45,0.85),(0.5,1.0)],8),bk,sp=400)]
    return s,"#e6e2ee"
def crown_basket(tag,seed):
    random.seed(seed)
    g=B(f"#{tag} yellow",oil("#ece6b4",0.3,"filbert",load=1,ent=0.5,stiff=0.4,dil=0.35))
    li=B(f"#{tag} lilac",oil("#a69ad0",0.07,"filbert",ent=1.3,dil=0.15,colors=["#b8aee0","#8c80b8"]))
    dk=B(f"#{tag} olive-black",oil("#2a2618",0.06,"flat",ent=1.5,dil=0.3,colors=["#3a3424","#1a1810"]))
    wh=B(f"#{tag} white",oil("#f2f0e6",0.035,"filbert",load=0.8,ent=1.4))
    cr=B(f"#{tag} cream scrub",oil("#e8e2c0",0.1,"filbert",load=0.5,dry=0.7,ent=1.7))
    s=ground(g)+hrows(cr,0.05,0.4,0.95,0.95,4)
    for x0 in (0.18,0.42,0.66,0.86):
        s.append(st(poly([(x0,0.36),(x0-0.04,0.2),(x0+0.02,0.07)],6),li,sp=380))
    s.append(st(ln(0.12,0.36,0.9,0.35,0.01),li,sp=450))
    s[len(s)-5]["dry"]=True
    for k in range(9):
        y=0.42+k*0.05;s.append(st(arc(0.5,y,0.38+R(-0.03,0.03),0.04+R(0,0.03),pi*0.98,pi*0.02,26),dk,sp=R(350,550)))
    s.append(st(ell(0.5,0.62,0.4,0.25,1.0),dk,sp=350))
    for k in range(4):
        y=0.5+k*0.07;s.append(st(arc(0.5,y,0.26,0.03,pi*0.9,pi*0.1,20),wh,sp=420))
    return s,"#ece6b4"
@ref(8)
def r8(): return crown_basket("08",8)
@ref(12)
def r12(): return crown_basket("12",121)
@ref(9)
def r9():
    g=B("#09 salmon",oil("#e8b2a6",0.3,"filbert",load=1,ent=0.4,stiff=0.4,dil=0.3))
    gb=B("#09 blue-grey",oil("#9aa0aa",0.08,"filbert",ent=1.2,dil=0.3))
    w=B("#09 white",oil("#f6f6f2",0.09,"filbert",load=0.9,dry=0.35,ent=1.6,pick=0.3,gloss=0.3))
    nv=B("#09 navy",oil("#1a2030",0.07,"flat",ent=1.2))
    gn=B("#09 green",oil("#2a5a38",0.07,"flat",ent=1.3))
    s=ground(g)+hrows(gb,0.08,0.06,0.3,0.18,2)+vrows(gn,0.94,0.25,1.0,0.75,2)
    s+=[st(ln(0.32,0.78,0.3,0.98,0.005),nv),st(ln(0.6,0.78,0.62,0.98,-0.005),nv),st(ln(0.46,0.8,0.46,0.98),nv)]
    a=[st(ell(R(0.25,0.75),R(0.25,0.55),R(0.12,0.25),R(0.1,0.2),R(0.7,1.2)),w,sp=R(450,700)) for k in range(9)];a[0]["dry"]=True;s+=a
    s+=hrows(w,0.12,0.15,0.88,0.7,5,bend=0.03)
    return s,"#e8b2a6"
@ref(10)
def r10():
    g=B("#10 lilac",oil("#e6e2f0",0.3,"filbert",load=1,ent=0.4,stiff=0.4,dil=0.35))
    yg=B("#10 yellow-green",oil("#a8b84a",0.09,"flat",ent=1.3,dil=0.25))
    gv=B("#10 green veil",oil("#4a8a60",0.08,"flat",ent=1.3,dil=0.6,op=0.6))
    mr=B("#10 maroon",oil("#4a1420",0.06,"flat",ent=1.5,dil=0.55,colors=["#5a1a28","#2a0a10"]))
    s=ground(g)
    a=vrows(yg,0.2,0.08,0.62,0.4,4,lean=0.1);a[0]["dry"]=True;s+=a+vrows(gv,0.3,0.15,0.6,0.42,3)
    for k in range(10):
        y=0.45+k*0.045;s.append(st(ell(0.5+R(-0.05,0.05),y,0.3+R(-0.05,0.08),0.05,R(0.8,1.4)),mr,sp=R(350,600)))
    s+=vrows(mr,0.38,0.7,0.6,0.95,3)+hrows(mr,0.22,0.9,0.78,0.97,2)
    return s,"#e6e2f0"
@ref(11)
def r11():
    g=B("#11 grey",oil("#d8d6cc",0.3,"filbert",load=1,ent=0.4,stiff=0.4,dil=0.35))
    cr=B("#11 cream",oil("#e6d6a8",0.12,"flat",load=0.8,dry=0.35,ent=1.6,pick=0.1,colors=["#efe2b8","#d6c290"]))
    cs=B("#11 cream scrub",oil("#f0e8cc",0.12,"filbert",load=0.5,dry=0.7,ent=1.7))
    pu=B("#11 purple",oil("#2a1428",0.05,"filbert",ent=1.2,dil=0.15))
    s=ground(g)
    a=hrows(cr,0.06,0.06,0.94,0.42,6);a[0]["dry"]=True;s+=a
    s+=vrows(cr,0.25,0.35,0.75,0.75,6)+hrows(cr,0.05,0.5,0.4,0.62,2)+hrows(cr,0.6,0.5,0.95,0.62,2)
    s+=hrows(cs,0.1,0.1,0.9,0.6,4,sp=(700,1000))
    for cx in (0.3,0.5,0.7):
        s.append(st(ell(cx,0.84,0.1,0.08,4.5,shrink=0.85),pu,sp=420))
    return s,"#d8d6cc"
@ref(13)
def r13():
    g=B("#13 pale",oil("#ece8e4",0.3,"filbert",load=1,ent=0.4,stiff=0.4,dil=0.35))
    rd=B("#13 red-black",oil("#8a2a18",0.05,"flat",ent=1.4,colors=["#a83a20","#2a0a08"]))
    bl=B("#13 pale blue",oil("#a8c8dc",0.12,"flat",load=0.8,dry=0.45,ent=1.6,pick=0.1,colors=["#c0d8e6","#8ab0c8"]))
    wh=B("#13 white scrub",oil("#e8f0f4",0.12,"filbert",load=0.5,dry=0.75,ent=1.7))
    pk=B("#13 pink",oil("#e8b8c0",0.06,"flat",ent=1.3))
    s=ground(g)+vrows(pk,0.0,0.3,0.06,0.9,2)
    for cx in (0.3,0.7):
        for k in range(5):
            x=cx-0.13+k*0.065;s.append(st(ln(x,0.2,x+R(-0.03,0.03),0.04,0.01),rd,sp=420))
        s.append(st(ln(cx-0.15,0.2,cx+0.15,0.2),rd,sp=500))
    a=hrows(bl,0.06,0.27,0.94,0.95,10,bend=0.03);a[0]["dry"]=True;s+=a+hrows(wh,0.1,0.3,0.9,0.9,6,sp=(700,1000))
    return s,"#ece8e4"
@ref(14)
def r14():
    g=B("#14 panel",oil("#e8e4d6",0.3,"filbert",load=1,ent=0.4,stiff=0.4,dil=0.35))
    dk=B("#14 dark under",oil("#3a3a34",0.1,"flat",ent=1.0,dil=0.2))
    ol=B("#14 olive",oil("#8a906a",0.1,"flat",load=0.85,dry=0.35,ent=1.6,pick=0.15,colors=["#9aa078","#6e7656"]))
    s=ground(g)
    sh=[(0.12,0.3,0.88,0.38),(0.4,0.1,0.6,0.62),(0.12,0.6,0.88,0.75),(0.42,0.75,0.58,0.95)]
    for (x0,y0,x1,y1) in sh: s+=hrows(dk,x0+0.02,y0+0.01,x1-0.02,y1-0.01,2)
    a=vrows(ol,0.4,0.08,0.6,0.62,4);a[0]["dry"]=True;s+=a
    s+=hrows(ol,0.1,0.28,0.9,0.4,3)+hrows(ol,0.1,0.58,0.9,0.78,4,bend=0.03)+vrows(ol,0.42,0.75,0.58,0.96,2)
    return s,"#e8e4d6"
# ======================= Ink, script, drawing =======================
@ref(15)
def r15():
    b=B("#15 ultramarine",ink("#1a2a9a",0.012,load=0.95,dry=0.15,ent=0.8,p2s=0.8))
    s=[];random.seed(15)
    for l in range(11):
        y=0.06+l*0.088;x=0.02
        while x<0.95:
            pts=[];n=random.randint(3,7)
            for j in range(n):
                h=R(0.018,0.03) if random.random()<0.75 else R(0.04,0.055);w=R(0.022,0.034)
                for i in range(7):
                    t=i/6;pts.append((x+w*t,y-h*math.sin(pi*t)+R(-0.001,0.001)))
                x+=w
            s.append(st(pts,b,[0.4,0.9,0.6,0.85,0.5],R(450,600),0.15));x+=R(0.03,0.05)
    return s,"#ffffff"
@ref(16)
def r16():
    cols=[("#16 blue","#2a60d0"),("#16 violet","#8a4ad0"),("#16 teal","#0a9aa0")]
    bs=[B(nm,wc(c,0.06,0.3,0.0,0.1,strength=1.0,pick=0.1)) for nm,c in cols]
    s=[];random.seed(16)
    for k in range(30):
        x,y=R(0.05,0.95),R(0.05,0.95);a=R(0,pi);L=R(0.15,0.35)
        x1,y1=x+L*math.cos(a),y+L*math.sin(a)
        s.append(st(ln(x,y,min(0.97,max(0.03,x1)),min(0.97,max(0.03,y1)),R(-0.04,0.04),16),bs[k%3],[0.9,1,1,1,0.95],R(300,450),0.5))
    return s,"#fbfaf6"
@ref(17)
def r17():
    b=B("#17 dry black",drybrush("#0c0c0e",0.06,load=0.8,dry=0.55,ent=1.6))
    f=B("#17 face line",ink("#0c0c0e",0.008,p2s=0.7))
    s=[]
    for cx in (0.22,0.78):
        s.append(st(ell(cx,0.4,0.2,0.22,3.5,shrink=0.85),b,[0.9,1,1,0.95,0.8,0.6],500,0.3))
    s.append(st(ell(0.5,0.6,0.16,0.18,2.5,shrink=0.5),b,sp=500))
    s+=vrows(b,0.36,0.62,0.64,0.88,4)
    s+=[st(ln(0.38,0.88,0.38,0.97),b),st(ln(0.62,0.88,0.62,0.97),b)]
    s+=[st(ell(0.5,0.4,0.14,0.17,1.0,jit=0.03),f,[0.6,0.9,0.8,0.9,0.6],300)]
    s+=[st(ln(0.44,0.36,0.48,0.37),f),st(ln(0.52,0.37,0.56,0.36),f),st(ln(0.47,0.48,0.53,0.48),f)]
    return s,"#ffffff"
@ref(18)
def r18():
    b=B("#18 blue stick",stick("#2050a0",0.012,"wax",ent=1.0))
    s=[];random.seed(18)
    for k in range(14): s.append(st(scrib(0.08,0.36,0.92,0.82,70,0.08,0.05),b,[0.6,0.9,0.8,0.5],1300,0.2))
    s.append(st(ln(0.08,0.6,0.92,0.6,0.0),b,[0.5,0.7,0.7,0.5],900))
    s+=[st(scrib(0.1,0.2,0.4,0.3,12,0.04,0.02),b,[0.3,0.5,0.4],900)]
    return s,"#ece8da"
@ref(19)
def r19():
    b=B("#19 charcoal",stick("#141414",0.018,"charcoal",ent=1.0,p2s=0.7))
    s=[]
    fingers=[(0.42,0.18,0.5,0.55),(0.52,0.12,0.6,0.52),(0.62,0.16,0.69,0.55),(0.71,0.26,0.77,0.6)]
    for x0,y0,x1,y1 in fingers:
        s.append(st(poly([(x0,y1),(x0,y0+0.03),((x0+x1)/2,y0),(x1,y0+0.03),(x1,y1)],7,0.004),b,[0.8,1,0.9,1,0.7],260))
    s.append(st(poly([(0.42,0.5),(0.32,0.6),(0.3,0.75),(0.38,0.88),(0.6,0.92),(0.75,0.8),(0.77,0.58)],7,0.004),b,[0.7,1,0.9,1,0.6],250))
    s.append(st(poly([(0.42,0.6),(0.3,0.5),(0.26,0.56),(0.36,0.7)],7,0.004),b,sp=250))
    s.append(st(poly([(0.38,0.32),(0.7,0.32),(0.7,0.38),(0.38,0.38),(0.38,0.32)],5),b,sp=300))
    for k in range(10): s.append(st(ln(0.4+k*0.03,0.32,0.4+k*0.03,0.38),b,[0.9,1,0.9],600,0.05))
    s.append(st([(0.4+0.03*math.sin(t*0.9)+t*0.002,0.3-t*0.01) for t in range(26)],b,[0.4,0.7,0.5,0.4],400))
    s.append(st(poly([(0.35,0.88),(0.33,0.98)],6),b))
    s.append(st(poly([(0.65,0.9),(0.67,0.99)],6),b))
    return s,"#f1ede2"
@ref(20)
def r20():
    b=B("#20 crayon",stick("#f04018",0.022,"wax",ent=1.2,relief=0.6))
    s=[];random.seed(20)
    for k in range(10): s.append(st(scrib(0.0,0.0,1.0,0.62,80,0.2,0.06),b,[0.7,1,0.9,0.7],1500,0.1))
    for k in range(10):
        x=R(0.0,1.0);s.append(st(zig(x,0.55,x+R(-0.15,0.15),R(0.75,0.98),10,0.03),b,[0.7,0.9,0.6,0.3],1300,0.1))
    return s,"#ffffff"
@ref(21)
def r21():
    o=B("#21 orange",gouache("#f06a40",0.12,"flat",ent=0.5))
    k=B("#21 black grit",drybrush("#0c0c0e",0.012,load=0.8,dry=0.5,ent=1.3,tip="round"))
    s=[]
    body=[(0.25,0.92),(0.2,0.6),(0.3,0.4),(0.45,0.35),(0.7,0.4),(0.8,0.6),(0.78,0.92)]
    s+=hrows(o,0.25,0.38,0.78,0.9,6)+[st(ell(0.5,0.32,0.18,0.15,1.6,shrink=0.7),o,sp=400)]
    s+=hrows(o,0.36,0.12,0.6,0.22,2)
    s.append(st(poly(body,8,0.003),k,[0.8,1,0.9,1,0.6],280))
    s.append(st(ell(0.5,0.32,0.19,0.16,1.0,jit=0.05),k,sp=280))
    s+=[st(ell(0.43,0.3,0.03,0.025,1.0),k,sp=250),st(ell(0.57,0.3,0.03,0.025,1.0),k,sp=250),st(poly([(0.44,0.4),(0.5,0.44),(0.56,0.4)],6),k)]
    s.append(st(poly([(0.36,0.22),(0.48,0.04),(0.6,0.22),(0.36,0.22)],6),k,sp=300))
    s+=[st(ell(0.3,0.6,0.06,0.1,1.0),k),st(ell(0.7,0.62,0.06,0.1,1.0),k)]
    return s,"#1a9ad8"
@ref(22)
def r22():
    b=B("#22 black brush",ink("#0c0c0e",0.03,load=1,dry=0.35,ent=1.2,tip="flat",p2s=0.8,curve=1.0))
    s=[]
    s.append(st(poly([(0.42,0.98),(0.4,0.6),(0.42,0.3),(0.44,0.2)],6),b,sp=350))
    s.append(st(poly([(0.44,0.2),(0.44,0.08),(0.47,0.08),(0.47,0.2)],5),b,sp=300))
    s.append(st(poly([(0.47,0.2),(0.55,0.2),(0.55,0.3),(0.62,0.3)],5),b,sp=300))
    s.append(st(poly([(0.62,0.3),(0.62,0.98)],10),b,sp=350))
    s.append(st(poly([(0.3,0.45),(0.36,0.4),(0.44,0.45)],6),b,sp=300))
    s.append(st(poly([(0.32,0.62),(0.4,0.72),(0.5,0.68),(0.56,0.76),(0.5,0.9),(0.38,0.95)],6),b,sp=320))
    s.append(st(poly([(0.48,0.5),(0.52,0.58),(0.5,0.62)],6),b,sp=300))
    s.append(st(poly([(0.66,0.4),(0.7,0.36),(0.74,0.42)],6),b,sp=300))
    return s,"#ffffff"
@ref(23)
def r23():
    w=B("#23 white dry",drybrush("#ffffff",0.08,load=0.7,dry=0.6,ent=1.6,tip="flat"))
    k=B("#23 black",ink("#0c0c0e",0.025,load=1,dry=0.2,ent=1.2,p2s=0.9))
    s=[]
    shield=[(0.32,0.28),(0.62,0.22),(0.62,0.72),(0.5,0.82),(0.36,0.75)]
    s+=vrows(w,0.33,0.27,0.6,0.78,5,lean=0.02)+hrows(w,0.33,0.3,0.6,0.7,4)
    s.append(st(poly([(0.38,0.42),(0.46,0.4),(0.5,0.45)],6),k,sp=300))
    s.append(st(poly([(0.52,0.4),(0.58,0.38),(0.6,0.44)],6),k,sp=300))
    s.append(st(poly([(0.4,0.6),(0.48,0.58),(0.56,0.62)],6),k,sp=300))
    s.append(st(poly([(0.63,0.42),(0.78,0.38),(0.88,0.5),(0.92,0.9)],8),k,[0.6,1,0.9,0.8,0.5],380))
    return s,"#e85a10"
@ref(24)
def r24():
    bg=B("#24 blue ground",oil("#3a4a6a",0.3,"filbert",load=1,ent=0.6,stiff=0.4,dil=0.3,streak=0.1))
    gf=B("#24 green face",oil("#7a9a6a",0.06,"filbert",ent=1.2,dil=0.25,colors=["#8aa878","#5a7a50"]))
    hair=B("#24 hair",oil("#2a3a2a",0.06,"flat",ent=1.2))
    bod=B("#24 ochre body",oil("#9a8a3a",0.1,"flat",ent=1.4,dil=0.25,colors=["#aa9a48","#7a6a28"]))
    ln_=B("#24 contour",oil("#1a2420",0.015,"round",ent=0.8,p2s=0.8))
    tb=B("#24 table",oil("#5a7a6a",0.12,"flat",ent=1.2))
    s=ground(bg)
    a=vrows(bod,0.15,0.5,0.88,0.85,6,lean=0.05);a[0]["dry"]=True;s+=a+hrows(tb,0.0,0.86,1.0,0.98,2)
    s+=[st(ell(0.5,0.38,0.12,0.15,2.2,shrink=0.8),gf,sp=350)]+[st(ell(0.48,0.18,0.13,0.08,2.0,shrink=0.7),hair,sp=350)]
    s+=[st(ell(0.48,0.08,0.05,0.04,2,shrink=0.7),hair)]
    s+=[st(ell(0.5,0.38,0.12,0.16,1.0,jit=0.03),ln_,sp=300),st(poly([(0.2,0.85),(0.35,0.55),(0.5,0.6),(0.65,0.55),(0.85,0.85)],6),ln_,sp=320)]
    return s,"#3a4a6a"
@ref(25)
def r25():
    y=B("#25 yellow",impasto("#f4c20d",0.34,"flat",ent=1.3,gloss=0.35,streak=0.06,colors=["#ffd21a","#e8a800"]))
    return [st(ln(0.5+dx,0.1+abs(dx),0.49+dx,0.92-abs(dx)*0.5,0.01,30),y,[1,1,0.95,0.9,0.85,0.7],180,1.2) for dx in (-0.045,0.045,0.0)],"#f2f2f0"
@ref(26)
def r26():
    k=B("#26 ink brush",ink("#0c0c0e",0.025,load=1,dry=0.15,ent=0.9,p2s=0.95))
    s=[]
    s+=[st(ell(0.33,0.38,0.12,0.08,1.0,jit=0.03),k,sp=300),st(ell(0.67,0.38,0.12,0.08,1.0,jit=0.03),k,sp=300)]
    s+=[st(poly([(0.18,0.2),(0.3,0.12),(0.45,0.2)],6),k,sp=320),st(poly([(0.55,0.2),(0.72,0.1),(0.86,0.2)],6),k,sp=320)]
    s+=[st(poly([(0.5,0.38),(0.48,0.56),(0.54,0.62),(0.6,0.58)],6),k,sp=300)]
    for i in range(9):
        x=0.3+i*0.05;s.append(st(ln(x,0.68+R(0,0.03),x+R(-0.03,0.03),0.82+R(0,0.08),0.01),k,[0.9,1,0.7,0.3],450,0.1))
    s+=[st(poly([(0.12,0.3),(0.14,0.6),(0.3,0.9)],6),k,sp=350)]
    return s,"#eef0e6"
@ref(27)
def r27():
    o=B("#27 orange impasto",impasto("#e87a30",0.08,"flat",ent=1.4,colors=["#f08a40","#c86020"]))
    s=[];random.seed(27)
    for k in range(14):
        x,y=R(0.25,0.62),R(0.18,0.62);a=R(-0.6,0.6);L=R(0.12,0.2)
        s.append(st(ln(x,y,x+L*math.cos(a),y+L*math.sin(a),R(-0.01,0.01),10),o,[1,0.95,0.85,0.6],R(250,400),0.4))
    return s,"#ece8e0"
@ref(28)
def r28():
    k=B("#28 black line",ink("#0c0c0e",0.03,load=1,dry=0.05,ent=0.6,p2s=0.7,op=0.56))
    s=[]
    s+=[st(ell(0.55,0.72,0.12,0.1,1.0,jit=0.02),k,sp=300),st(ell(0.55,0.72,0.06,0.05,1.0,jit=0.02),k,sp=300),st(ell(0.6,0.9,0.1,0.08,1.0,jit=0.02),k,sp=300)]
    s+=[st(poly([(0.48,0.3),(0.48,0.6)],8),k),st(poly([(0.58,0.3),(0.58,0.6)],8),k),st(ell(0.53,0.3,0.06,0.03,1.0),k)]
    s+=[st(poly([(0.3,0.25),(0.42,0.18),(0.62,0.2),(0.7,0.3),(0.62,0.38),(0.45,0.36)],6),k,sp=320)]
    s+=[st(poly([(0.0,0.2),(0.1,0.1),(0.12,0.35),(0.05,0.6),(0.15,0.95)],8),k,sp=360)]
    s+=[st(poly([(1.0,0.15),(0.88,0.3),(0.95,0.5),(0.85,0.7),(0.92,0.98)],8),k,sp=360)]
    s+=[st(poly([(0.3,0.4),(0.36,0.5),(0.3,0.62),(0.4,0.7)],6),k,sp=320)]
    return s,"#f4f0e0"
@ref(29)
def r29():
    m=B("#29 magenta",wc("#d0209a",0.09,0.5,0.2,0.05,strength=0.95,colors=["#e8409f"]))
    s=[]
    for k in range(4):
        a=pi*k/4+0.08;s.append(st(ln(0.5-0.42*math.cos(a),0.52-0.42*math.sin(a)/C.H*C.W,0.5+0.42*math.cos(a),0.52+0.42*math.sin(a)/C.H*C.W,R(-0.01,0.01),16),m,[0.7,0.95,0.9,0.7],400,0.8))
    return s,"#ffffff"
@ref(30)
def r30():
    r=B("#30 red gouache",gouache("#c02818",0.1,"flat",ent=0.9,dry=0.25,colors=["#d03a20","#a01c10"]))
    k=B("#30 black",ink("#141414",0.018,load=1,dry=0.25,ent=1.0,p2s=0.9))
    s=hrows(r,0.18,0.12,0.82,0.85,8,bend=0.03)
    s[0]["rest"]=1.0
    s+=[st(poly([(0.2,0.25),(0.18,0.55),(0.3,0.8),(0.5,0.9),(0.7,0.8),(0.8,0.55),(0.8,0.25)],6),k,sp=300)]
    s+=[st(poly([(0.2,0.2),(0.35,0.06),(0.6,0.04),(0.82,0.18)],6),k,sp=330)]
    s+=[st(ln(0.3,0.38,0.44,0.37,0.01),k),st(ln(0.56,0.37,0.7,0.38,-0.01),k),st(ln(0.32,0.45,0.42,0.45),k),st(ln(0.58,0.45,0.68,0.45),k)]
    s+=[st(poly([(0.5,0.42),(0.48,0.58),(0.54,0.6)],6),k),st(ln(0.42,0.7,0.6,0.7,0.01),k)]
    s+=[st(poly([(0.38,0.88),(0.42,0.98)],6),k),st(poly([(0.62,0.88),(0.58,0.98)],6),k)]
    return s,"#ece2cc"
@ref(31)
def r31():
    k=B("#31 blotted",ink("#121212",0.008,load=0.8,dry=0.4,ent=1.2,p2s=0.8))
    s=[]
    s+=[st(poly([(0.15,0.8),(0.3,0.5),(0.55,0.35),(0.75,0.3),(0.95,0.15)],6,0.003),k,sp=300)]
    s+=[st(poly([(0.3,0.75),(0.45,0.55),(0.65,0.48),(0.95,0.35)],6,0.003),k,sp=300)]
    s+=[st(poly([(0.05,0.88),(0.95,0.88)],10,0.002),k,sp=400),st(poly([(0.05,0.94),(0.95,0.94)],10,0.002),k,sp=400)]
    for i in range(16): s.append(st(ln(0.08+i*0.055,0.88,0.08+i*0.055,0.94),k,[0.8,1,0.8],500,0.05))
    for fx in (0.2,0.3,0.4,0.5,0.6):
        s.append(st(poly([(fx+0.05,0.6),(fx,0.75),(fx+0.02,0.86)],6),k,sp=300))
    s+=[st(poly([(0.7,0.25),(0.75,0.4),(0.86,0.42),(0.88,0.2)],6),k)]
    return s,"#f4f0e4"
@ref(32)
def r32():
    o=B("#32 orange",impasto("#ff7a10",0.16,"flat",ent=1.3,colors=["#ff9030","#e06000"]))
    lg=B("#32 linen",oil("#8c8c88",0.3,"filbert",load=1,ent=0.3,stiff=0.4,dil=0.5,weave=0.6))
    s=ground(lg,6)
    s+=[st(ln(0.28,0.3,0.72,0.28,0.01),o,[1,0.95,0.9,0.7],300,1.0,dry=True),st(ln(0.3,0.5,0.7,0.52,-0.01),o,[1,0.95,0.9,0.7],300,1.0),st(ln(0.3,0.7,0.7,0.68,0.01),o,[1,0.95,0.9,0.7],300,1.0)]
    return s,"#8c8c88"
@ref(33)
def r33():
    rd=B("#33 red band",wc("#b8141e",0.12,0.6,0.7,0.1,tilt=0.5))
    pf=B("#33 pink flame",wc("#e05a7a",0.08,0.8,0.8,0.0,tilt=1.5,down=270,strength=0.9))
    s=[st(ln(0.0,0.55,1.0,0.56,0.01,16),rd,[0.9,1,1,0.9],250,2)]
    for k in range(7):
        x=0.08+k*0.14+R(-0.03,0.03);s.append(st(ln(x,0.52,x+R(-0.05,0.05),R(0.08,0.25),R(-0.03,0.03),10),pf,[0.8,0.6,0.3],300,0.5))
    return s,"#f4f0f0"
@ref(34)
def r34():
    cols=["#c02a6a","#e8a0b8","#8a1a3a","#f0c0c8","#d04880"]
    bs=[B(f"#34 patch {i}",oil(c,0.12,"flat",ent=1.4,dil=0.15,load=0.85,pick=0.3)) for i,c in enumerate(cols)]
    s=[];random.seed(34)
    for k in range(16):
        x,y=R(0.0,0.75),R(0.0,0.9);s+=hrows(bs[k%5],x,y,x+R(0.2,0.4),y+R(0.06,0.14),2)
    return s,"#6a1a3a"
@ref(35)
def r35():
    rd=B("#35 red runs",wc("#e02a2a",0.22,0.7,0.8,0.1,tilt=3.0,colors=["#f07a20"]))
    return [st(ln(0.0,0.4+dy,1.0,0.38+dy,0.01,16),rd,[0.9,1,1,0.9],280,1.5) for dy in (-0.03,0.03,0.0)],"#f8f6f4"
LET={'I':[[(0.5,0),(0.5,1)]],'T':[[(0,0),(1,0)],[(0.5,0),(0.5,1)]],'W':[[(0,0),(0.25,1),(0.5,0.4),(0.75,1),(1,0)]],
 'A':[[(0,1),(0.5,0),(1,1)],[(0.25,0.6),(0.75,0.6)]],'S':[[(1,0.1),(0.5,0),(0,0.25),(0.5,0.5),(1,0.75),(0.5,1),(0,0.9)]],
 'F':[[(0,1),(0,0),(1,0)],[(0,0.5),(0.8,0.5)]],'N':[[(0,1),(0,0),(1,1),(1,0)]],'C':[[(1,0.1),(0.5,0),(0,0.5),(0.5,1),(1,0.9)]]}
def letters(b,sp=330):
    out=[];rows=("IT","WAS","FAN","TAS","TIC");h=0.15
    for r,word in enumerate(rows):
        w=0.27;x0=0.5-len(word)*w/2
        for i,ch in enumerate(word):
            for s_ in LET[ch]:
                pts=[(x0+i*w+0.03+px_*(w-0.07),0.03+r*(h+0.045)+py*h) for px_,py in s_]
                out.append(st(poly(pts,6,0.002),b,[0.7,1,0.9,0.7],sp,0.3))
    return out
@ref(36)
def r36():
    return letters(B("#36 magenta gouache",gouache("#f02aa0",0.055,"flat",ent=0.8,dry=0.3,colors=["#f850b0","#d01890"]))),"#f2f0f4"
@ref(49)
def r49():
    return letters(B("#49 magenta round",ink("#f02aa0",0.05,load=1,dry=0.1,ent=0.8,p2s=0.9,op=0.56,colors=["#f850b0"]))),"#f2f0f4"
@ref(37)
def r37():
    g=B("#37 brown",oil("#3a1a12",0.3,"filbert",load=1,ent=0.6,stiff=0.4,dil=0.3,streak=0.1))
    tp=B("#37 teapot",oil("#7a8a2a",0.05,"filbert",ent=1.3,colors=["#9aa840","#4a5a18"]))
    bw=B("#37 bowl",oil("#b8742a",0.05,"flat",ent=1.3,colors=["#d09040","#8a4a18"]))
    bx=B("#37 box",oil("#5a2a1a",0.05,"flat",ent=1.2))
    rd=B("#37 red",oil("#c82a1a",0.02,"filbert",ent=1.0))
    wh=B("#37 white",oil("#f0ece0",0.035,"filbert",ent=1.0))
    oc=B("#37 ochre",oil("#c8a060",0.025,"flat",ent=1.2))
    s=ground(g)
    a=[st(ell(0.62,0.32,0.07,0.1,2.5,shrink=0.7),tp,sp=350)];a[0]["dry"]=True;s+=a
    s+=[st(ln(0.69,0.26,0.78,0.18),tp),st(arc(0.55,0.3,0.05,0.06,pi*0.5,pi*1.5,12),tp)]
    s+=[st(ell(0.25,0.55,0.16,0.08,2.5,shrink=0.7),bw,sp=380)]
    for k in range(4): s.append(st(ell(0.2+k*0.04,0.52,0.03,0.025,1.5,shrink=0.5),oc))
    s+=hrows(bx,0.5,0.6,0.8,0.82,4)+[st(poly([(0.5,0.6),(0.8,0.6),(0.8,0.82),(0.5,0.82),(0.5,0.6)],5),oc,sp=350)]
    s+=[st(ln(0.58+k*0.06,0.68,0.6+k*0.06,0.72),rd) for k in range(3)]
    s+=[st(ell(0.12,0.8,0.025,0.02,1.5,shrink=0.5),wh),st(ell(0.3,0.82,0.025,0.02,1.5,shrink=0.5),oc)]
    return s,"#3a1a12"
@ref(38)
def r38():
    b=B("#38 sanguine",stick("#8a3010",0.006,"pencil",ent=0.8,p2s=0.6))
    s=[];random.seed(38)
    s.append(st(arc(0.48,0.32,0.28,0.24,pi*1.0,pi*2.0,30),b,sp=300))
    s.append(st(ln(0.18,0.32,0.8,0.3,0.0),b,sp=400))
    s.append(st(ell(0.5,0.48,0.16,0.2,1.0,jit=0.04),b,sp=280))
    for k in range(60):
        x,y=R(0.2,0.8),R(0.12,0.95);a=R(-1.0,-0.6);L=R(0.03,0.07)
        s.append(st(ln(x,y,x+L*math.cos(a),y+L*math.sin(a),0,4),b,[0.5,0.9,0.5],900,0.05))
    s.append(st(poly([(0.3,0.7),(0.45,0.66),(0.62,0.72),(0.7,0.95)],6),b,sp=280))
    s.append(st(poly([(0.42,0.56),(0.5,0.6),(0.58,0.56)],6),b,sp=280))
    return s,"#efe6d4"
@ref(39)
def r39():
    cols=[("#39 red","#c01818"),("#39 blue","#1838b0"),("#39 yellow","#f0c020")]
    bs=[B(nm,impasto(c,0.08,"flat",ent=1.3,body=0.9)) for nm,c in cols]
    s=[];random.seed(39)
    for k in range(18):
        b=bs[k%3]
        if k%2: x=R(0.05,0.95);s.append(st(ln(x,R(0.0,0.3),x+R(-0.08,0.08),R(0.6,1.0),R(-0.02,0.02)),b,[1,0.95,0.9,0.7],R(250,380),0.5))
        else: y=R(0.05,0.95);s.append(st(ln(R(0.0,0.3),y,R(0.6,1.0),y+R(-0.08,0.08),R(-0.02,0.02)),b,[1,0.95,0.9,0.7],R(250,380),0.5))
    return s,"#f0c020"
@ref(40)
def r40():
    o=B("#40 olive",wc("#5a6a1a",0.12,0.55,0.7,0.2,strength=1.0))
    se=B("#40 sepia",wc("#8a6038",0.1,0.6,0.7,0.2,strength=1.0))
    k=B("#40 dark",wc("#1a1a14",0.04,0.4,0.5,0.1,strength=1.0))
    s=[st(ell(0.25,0.3,0.2,0.18,1.0),o,[0.9,1,0.9],220,2),st(ell(0.45,0.7,0.2,0.12,1.0),se,[0.8,1,0.8],220,3)]
    s+=[st(ell(0.82,0.25,0.08,0.06,1.0),k,[0.9,1,0.9],250,1),st(ell(0.62,0.15,0.04,0.03,1.0),k,[0.9,1,0.9],250,1)]
    return s,"#f4f2ee"
@ref(41)
def r41():
    rd=B("#41 red pencil",stick("#b03a28",0.005,"pencil",ent=0.8))
    br=B("#41 brown pencil",stick("#8a5a30",0.005,"pencil",ent=0.8))
    gr=B("#41 grey pencil",stick("#6a6a5a",0.004,"pencil",ent=0.8))
    s=[];random.seed(41)
    for k in range(60):
        x=R(0.0,1.0);s.append(st(ln(x,0.0,x+R(-0.02,0.02),1.0,0,6),gr,[0.3,0.5,0.4],1500,0.02))
    for cx,cy in ((0.3,0.28),(0.7,0.28)):
        s.append(st(ell(cx,cy,0.18,0.16,1.0,jit=0.03),rd,sp=300))
        for k in range(25):
            x,y=R(cx-0.15,cx+0.15),R(cy-0.13,cy+0.13);s.append(st(ln(x,y,x+0.04,y-0.03,0,4),rd,[0.4,0.8,0.4],900,0.02))
    for cx,cy in ((0.25,0.65),(0.5,0.7),(0.75,0.65),(0.5,0.88)):
        s.append(st(ell(cx,cy,0.12,0.1,1.0,jit=0.06),br,sp=300))
        for k in range(20):
            x,y=R(cx-0.1,cx+0.1),R(cy-0.08,cy+0.08);s.append(st(ln(x,y,x+0.03,y+0.02,0,4),br,[0.4,0.8,0.4],900,0.02))
    return s,"#e8dcc4"
@ref(42)
def r42():
    bk=B("#42 black",gouache("#141414",0.1,"flat",ent=0.5))
    pk=B("#42 pink",gouache("#e070a0",0.12,"flat",ent=0.6))
    sh=B("#42 shaggy pastel",stick("#f8c0d8",0.02,"pastel",ent=1.2))
    dk=B("#42 nose",gouache("#1a1a1a",0.03,"round",ent=0.5))
    s=hrows(bk,0.0,0.02,1.0,0.98,8)
    a=hrows(pk,0.08,0.06,0.92,0.94,8);a[0]["dry"]=True;s+=a
    random.seed(42)
    for k in range(70):
        a_=R(0,2*pi);r0=R(0.05,0.3);cx,cy=0.5+r0*math.cos(a_)*0.8,0.48+r0*math.sin(a_)
        s.append(st(ln(cx,cy,cx+R(-0.03,0.03),cy+R(0.04,0.1),R(-0.01,0.01),5),sh,[0.6,0.9,0.5],900,0.03))
    s+=[st(ell(0.5,0.46,0.03,0.02,2.5,shrink=0.7),dk,sp=300)]
    return s,"#e070a0"
@ref(43)
def r43():
    k=B("#43 dragged black",drybrush("#0c0c0e",0.16,tip="flat",load=0.9,dry=0.55,ent=1.5))
    s=[];random.seed(43)
    for i in range(10):
        if i%2: x=R(0.05,0.95);s.append(st(ln(x,R(0.0,0.2),x+R(-0.05,0.05),R(0.5,0.95)),k,[0.9,1,0.9,0.6],R(600,900)))
        else: y=R(0.0,0.9);s.append(st(ln(R(0.0,0.2),y,R(0.6,1.0),y+R(-0.05,0.05)),k,[0.9,1,0.9,0.6],R(600,900)))
    return s,"#f0a020"
@ref(44)
def r44():
    b=B("#44 ribbon",oil("#1028b0",0.11,"flat",load=1,dry=0.25,ent=1.4,dil=0.1,gloss=0.45,body=0.62,colors=["#2848d0","#081878"]))
    random.seed(9);pts=[];n=220
    for i in range(n):
        t=i/(n-1);a=t*7*pi;r=0.2+0.1*math.sin(t*5)
        pts.append((0.5+r*math.cos(a)+0.12*math.sin(t*3),0.5+r*0.8*math.sin(a*1.3)*C.W/C.H+t*0.2-0.1))
    return [st(pts,b,[0.85,0.95,0.9,0.85,0.7],450,1)],"#ffffff"
@ref(45)
def r45():
    o=B("#45 orange pastel",stick("#f04010",0.05,"pastel",ent=1.0))
    k=B("#45 black pastel",stick("#141414",0.04,"pastel",ent=1.0))
    gr=B("#45 green",stick("#1a7a3a",0.03,"pastel",ent=1.0))
    fi=B("#45 finger",finger("#f04010",0.05))
    s=[];random.seed(45)
    for cx in (0.35,0.65):
        for k_ in range(8): s.append(st(ell(cx,0.6,0.17-k_*0.012,0.3-k_*0.02,1.0,jit=0.04),o,[0.8,1,0.9,0.8],700,0.1))
    s+=[st(ln(0.5,0.32,0.5,0.95,0.02),k,sp=500),st(ln(0.2,0.45,0.25,0.85,0.03),k,sp=500),st(ln(0.8,0.45,0.75,0.85,-0.03),k,sp=500)]
    s+=[st(ln(0.47,0.32,0.52,0.08,0.03),gr,sp=400),st(arc(0.56,0.12,0.06,0.05,pi,2*pi,12),gr,sp=400)]
    for k_ in range(6): s.append(st(scrib(0.2,0.4,0.8,0.9,10,0.05,0.05),fi,[0.8,1,0.9],500))
    return s,"#e8e4dc"
@ref(46)
def r46():
    b=B("#46 lips",wc("#8a1a10",0.07,0.65,0.8,0.1,strength=0.95))
    return [st(ln(0.28,0.42,0.72,0.41,-0.04,10),b,[0.5,1,0.5],220,2),st(ln(0.3,0.56,0.7,0.57,0.035,10),b,[0.5,1,0.5],220,2)],"#f6ecd0"
@ref(47)
def r47():
    y=B("#47 yellow",gouache("#e8f020",0.3,"flat",ent=0.3))
    p=B("#47 pink knife",knife("#f0a8d0",0.22))
    s=ground(y,5)
    for k in range(4):
        e=st(ln(0.12,0.17+k*0.22,0.88,0.16+k*0.22+R(-0.02,0.02),R(-0.02,0.02),14,0.006),p,[0.9,1,0.95,0.8],260,1);s.append(e)
    s[5]["dry"]=True
    return s,"#e8f020"
@ref(48)
def r48():
    k=B("#48 black bands",gouache("#0c0c0e",0.12,"flat",ent=0.9,dry=0.3,load=1,dil=0.35))
    BR["#48 black bands"]["time"]={"tilt":1.0,"downhill":90}
    s=[st(ln(0.0,0.1+i*0.17,1.0,0.12+i*0.17+R(-0.03,0.03),R(-0.02,0.02),16),k,[0.95,1,1,0.9],650,1.5) for i in range(5)]
    return s,"#ff6a10"
@ref(50)
def r50():
    sky=B("#50 sky",gouache("#a8c8e0",0.3,"filbert",ent=0.3))
    sea=B("#50 sea",gouache("#2a5a7a",0.3,"filbert",ent=0.4,colors=["#3a6a8a","#1a4a6a"]))
    sand=B("#50 sand",gouache("#3a3a38",0.3,"filbert",ent=0.4))
    cols=["#f0a0b0","#f8e040","#ffffff","#5a8ad0","#f0c0a0"]
    bs=[B(f"#50 swipe {i}",impasto(c,0.06,"flat",ent=1.2)) for i,c in enumerate(cols)]
    s=hrows(sky,-0.05,0.0,1.05,0.4,4,pr=[1,1,1,1])+hrows(sea,-0.05,0.42,1.05,0.8,4,pr=[1,1,1,1])+hrows(sand,-0.05,0.82,1.05,1.0,2,pr=[1,1,1,1])
    random.seed(50);sw=[]
    for i in range(13):
        x,y=R(0.1,0.75),R(0.05,0.9);sw.append(st(ln(x,y,x+R(0.08,0.15),y+R(-0.01,0.01),0.005,8),bs[i%5],[1,0.95,0.8,0.5],300,0.4))
    sw[0]["dry"]=True
    return s+sw,"#a8c8e0"

# ======================= auto (traced) =======================
import warnings;warnings.filterwarnings("ignore")
from trace import trace
from autocfg import CFG
def auto(n):
    cfg=dict(CFG[n]);mk_m=cfg.pop("mass");mk_l=cfg.pop("line")
    bg,layers,(gw,gh)=trace(n,**cfg)
    C.H=round(C.W*gh/gw);random.seed(n*7)
    out=[];first=True
    for li,(hc,kind,items,sz) in enumerate(layers):
        if kind=="mass":
            b=B(f"#{n:02d} L{li} {hc}",mk_m(hc,min(0.15,sz*MS.get(n,1.6))))
            ss=[st([(x/gw,y/gh) for x,y in it],b,sp=R(450,750),rest=0.2) for it in items if len(it)>=2]
        else:
            wmax=max(max(wd) for _,wd in items) or 1
            b=B(f"#{n:02d} L{li} {hc} line",mk_l(hc,min(0.08,sz*LS.get(n,1.0))))
            ss=[]
            for pts,wd in items:
                if len(pts)<2: continue
                k=max(1,len(wd)//20);pr=[round(max(0.3,min(1.0,w/wmax*1.1)),2) for w in wd[::k]]
                ss.append(st([(x/gw,y/gh) for x,y in pts],b,pr=pr if len(pr)>=2 else [1,1],sp=R(260,360),rest=0.15))
        if ss and not first: ss[0]["dry"]=True
        if ss: first=False
        out+=ss
    return out,bg

# ======================= build =======================
MANUAL={25,33,35,46,47}
MS={38:1.0,41:1.0,18:1.1}
LS={19:0.7,31:0.8,28:0.9}
def build(ver,K,only=None):
    C.K=K;names=[]
    for n in sorted(F):
        if only and n not in only: continue
        setup(n)
        strokes,bg=auto(n) if (n in CFG and n not in MANUAL) else F[n]()
        title=f"#{n:02d} "+NM[n]
        sheet(n,title,strokes,bg,wet=0.8 if n in (33,35,40,46) else 0)
    out=[]
    for n,(title,s) in sorted(SH.items()):
        main=next(x["brush"] for x in s["strokes"])
        out.append({"name":title,"recipe":BR[main],"sheet":s});names.append(f"refs v3 · {title}".lower())
    out+=[{"name":k,"recipe":v} for k,v in BR.items()]
    json.dump({"id":"refs-v3","version":ver,"folder":"Refs v3","brushes":out},open('/home/claude/lab/packs/refs-v3.json','w'),ensure_ascii=False)
    return names
if __name__=="__main__":
    only=set(int(x) for x in sys.argv[3].split(',')) if len(sys.argv)>3 else None
    names=build(int(sys.argv[1]),int(sys.argv[2]),only)
    open('/tmp/claude-0/only.txt','w').write(",".join(names));print(len(names),"sheets;",len(BR),"brushes")
