"""Toolkit for the 50-reference pack on engine v3.2: normalized gestures + v3 recipes."""
import math,random
R=random.uniform
def lin(h):
    h=h.lstrip('#');v=[int(h[i:i+2],16)/255 for i in (0,2,4)]
    f=lambda c: c/12.92 if c<=0.04045 else ((c+0.055)/1.055)**2.4
    r,g,b=[round(f(c),4) for c in v];return {"r":r,"g":g,"b":b,"a":1}
def shade(h,k):
    h=h.lstrip('#');v=[int(h[i:i+2],16) for i in (0,2,4)]
    v=[max(0,min(255,int(x*k+(8 if k>1 else -5)))) for x in v];return '#%02x%02x%02x'%tuple(v)
class Ctx:
    W=800;H=800;K=2
C=Ctx()
def px(f): return f*C.W*C.K          # size as a fraction of width -> px
# ---------------- recipes ----------------
def _tool(kind="hairs",tip="flat",stiff=0.6,load=0.8,give=0.9,dry=0.3,clump=0.0,pick=0.05,ent=1.5,colors=None,pattern="streaks",shape=None):
    t={"kind":kind,"stiffness":stiff,"load":load,"give":give,"dryness":dry,"clump":clump,"pickup":pick,"bristle":1,"entropy":ent}
    if tip: t["tip"]=tip
    if shape: t["shape"]=shape
    if colors: t["colors"]=[lin(c) for c in colors];t["colorPattern"]=pattern
    return t
def _streak(c,s): return [shade(c,1+s),shade(c,1-s)] if s else None
def oil(c,s,tip="flat",load=0.8,dry=0.3,pick=0.05,ent=1.5,stiff=0.6,give=0.9,clump=0.0,dil=0.2,op=0.95,gloss=0.2,body=0.6,fluid=0.3,mix=0.5,streak=0.08,colors=None,solv="turpentine",p2s=0.45,tremor=0.5,weave=0.0,follow=None):
    r=dict(size=px(s),hand={"smoothing":0.3,"pressureToSize":p2s,"tremor":tremor},
      tool=_tool("hairs",tip,stiff,load,give,dry,clump,pick,ent,colors or _streak(c,streak)),
      paint={"color":lin(c),"fluidity":fluid,"body":body,"opacity":op,"gloss":gloss,"strength":0.5,"tack":0.4,"mix":mix,"solvent":solv,"dilute":dil},
      texture={"tool":"bristles","push":0.3,"depth":0.5},surface={"relief":0.0,"weave":weave,"weaveSize":6})
    if follow is not None: r["form"]={"follow":follow}
    return r
def acr(c,s,**k):
    k.setdefault("solv","water");k.setdefault("gloss",0.12);k.setdefault("body",0.55);return oil(c,s,**k)
def impasto(c,s,tip="flat",load=1.0,ent=1.2,body=0.85,gloss=0.3,dil=0.0,**k):
    return oil(c,s,tip=tip,load=load,ent=ent,body=body,gloss=gloss,dil=dil,fluid=0.15,**k)
def gouache(c,s,tip="round",load=0.9,dry=0.15,ent=0.7,stiff=0.45,dil=0.15,op=0.95,p2s=0.6,pick=0.1,**k):
    return dict(size=px(s),hand={"smoothing":0.3,"pressureToSize":p2s,"tremor":0.4},
      tool=_tool("hairs",tip,stiff,load,0.8,dry,0.2,pick,ent,k.get("colors")),
      paint={"color":lin(c),"fluidity":0.42,"body":0.3,"opacity":op,"gloss":0.05,"strength":0.6,"mix":0.5,"solvent":"water","dilute":dil})
def ink(c,s,tip="round",load=0.9,dry=0.1,ent=0.6,stiff=0.35,p2s=1.0,op=0.55,fluid=0.5,curve=1.2,tremor=0.3,**k):
    return dict(size=px(s),hand={"smoothing":0.3,"pressureToSize":p2s,"lightestTouch":0.0,"pressureCurve":curve,"tremor":tremor},
      tool=_tool("hairs",tip,stiff,load,0.8,dry,0.2,0.1,ent,k.get("colors")),
      paint={"color":lin(c),"fluidity":fluid,"body":0.1,"opacity":op,"gloss":0.1,"strength":0.9,"staining":0.6,"mix":0.5})
def drybrush(c,s,tip="worn",load=0.5,dry=0.75,ent=1.6,**k):
    return ink(c,s,tip=tip,load=load,dry=dry,ent=ent,stiff=0.75,p2s=0.6,op=0.56,**k)
def wc(c,s,dil=0.6,soft=0.3,gran=0.2,tip="round",dry=0.0,load=1.0,pick=0.4,tilt=0,down=90,strength=0.85,colors=None,p2s=0.8):
    r=dict(size=px(s),hand={"smoothing":0.3,"pressureToSize":p2s,"tremor":0.4},
      tool=_tool("hairs",tip,0.2,load,0.7,dry,0.3,pick,0.7,colors),
      paint={"color":lin(c),"fluidity":0.85,"body":0.05,"opacity":0.15,"gloss":0.0,"strength":strength,"granulation":gran,"staining":0.5,"drying":0.5,"mix":0.6,"solvent":"water","dilute":dil},
      form={"source":"round","round":1,"soft":soft},surface={"relief":0.4,"grain":6})
    if tilt: r["time"]={"tilt":tilt,"downhill":down}
    return r
def stick(c,s,kind="pastel",op=None,relief=0.55,ent=0.8,p2s=0.65):
    # pastel / charcoal / crayon(wax): dry sticks
    grain={"pastel":0.8,"charcoal":0.8,"wax":0.7,"pencil":0.75}[kind]
    body={"pastel":0.2,"charcoal":0.1,"wax":0.6,"pencil":0.15}[kind]
    o=op if op is not None else {"pastel":0.85,"charcoal":0.6,"wax":0.85,"pencil":0.7}[kind]
    return dict(size=px(s),hand={"smoothing":0.2,"pressureToSize":p2s,"pressureCurve":1.0,"tremor":0.5},
      tool={"kind":"solid","shape":{"source":"charcoal" if kind=="charcoal" else "round","round":0.7,"rag":1.5},"stiffness":1,"load":1,"entropy":ent},
      paint={"color":lin(c),"fluidity":0.0,"body":body,"opacity":o,"gloss":0.05,"grain":grain,"strength":0.7},
      surface={"relief":relief,"grain":6})
def knife(c,s,body=0.8):
    return dict(size=px(s),hand={"smoothing":0.35,"pressureToSize":0.3},tool={"kind":"knife","stiffness":1,"load":1,"entropy":0.4},
      paint={"color":lin(c),"fluidity":0.1,"body":body,"opacity":1,"gloss":0.3,"strength":0.6},texture={"tool":"knife","push":1})
def finger(c,s):
    return dict(size=px(s),hand={"pressureToSize":0.5},tool={"kind":"finger","load":0,"stiffness":0.9,"entropy":0.3},
      paint={"color":lin(c),"fluidity":0.0,"body":0.2,"opacity":0.85,"grain":0.8})
# ---------------- gestures (normalized 0..1) ----------------
def P(pts):return [[round(x*C.W*C.K,1),round(y*C.H*C.K,1)] for x,y in pts]
def ln(x0,y0,x1,y1,bend=0.0,n=20,wob=0.0):
    ph=R(0,6);out=[]
    ax,ay=(x1-x0)*C.W,(y1-y0)*C.H;L=math.hypot(ax,ay) or 1;nx,ny=-ay/L,ax/L
    for i in range(n):
        t=i/(n-1);b=bend*math.sin(math.pi*t)+wob*math.sin(t*6+ph)
        out.append((x0+(x1-x0)*t+nx*b,y0+(y1-y0)*t+ny*b*C.W/C.H))
    return out
def poly(pts,d=6,j=0.0):
    out=[]
    for a,b in zip(pts,pts[1:]):
        for t in range(d): out.append((a[0]+(b[0]-a[0])*t/d+R(-j,j),a[1]+(b[1]-a[1])*t/d+R(-j,j)))
    out.append(pts[-1]);return out
def ell(cx,cy,rx,ry,turns=1.0,a0=None,n=60,jit=0.1,shrink=0.0):
    a0=R(0,6.28) if a0 is None else a0;ph=[R(0,6),R(0,6)];out=[]
    for i in range(n):
        t=i/(n-1);a=a0+2*math.pi*turns*t;k=(1+jit*math.sin(3*a+ph[0])+0.6*jit*math.sin(5*a+ph[1]))*(1-shrink*t)
        out.append((cx+rx*k*math.cos(a),cy+ry*k*math.sin(a)))
    return out
def arc(cx,cy,rx,ry,a0,a1,n=24):
    return [(cx+rx*math.cos(a0+(a1-a0)*i/(n-1)),cy+ry*math.sin(a0+(a1-a0)*i/(n-1))) for i in range(n)]
def scrib(x0,y0,x1,y1,n=60,sx=0.12,sy=0.08,seed=None):
    if seed is not None: random.seed(seed)
    x,y=R(x0,x1),R(y0,y1);out=[]
    for i in range(n):
        x=min(x1,max(x0,x+R(-sx,sx)));y=min(y1,max(y0,y+R(-sy,sy)));out.append((x,y))
    return out
def zig(x0,y0,x1,y1,n=12,amp=0.05,ang=0.0):
    out=[]
    for i in range(n):
        t=i/(n-1);out.append((x0+(x1-x0)*t+R(-0.01,0.01),y0+(y1-y0)*t+(amp if i%2 else -amp)+R(-0.01,0.01)))
    return out
def press(a=None,e=None):return [a or R(0.85,1.0),R(0.7,0.95),R(0.65,0.95),R(0.55,0.9),e or R(0.2,0.5)]
def st(pts,b,pr=None,sp=None,rest=0.3,dry=False):
    s={"points":P(pts),"pressure":list(pr or press()),"speed":round((sp or R(400,800))*C.K,1),"rest":rest,"brush":b}
    if dry: s["dry"]=True
    return s
def hrows(b,x0,y0,x1,y1,n,bend=0.015,tilt=0.0,alt=True,sp=None,pr=None,jit=0.25,over=0.03):
    out=[]
    for i in range(n):
        y=y0+(y1-y0)*(i+R(-jit,jit))/max(1,n-1);a=x0+R(-over,over*2);c=x1-R(-over,over*2);dy=tilt*(c-a)+R(-0.01,0.01)
        p=ln(a,y,c,y+dy,R(-bend,bend)) if (i%2==0 or not alt) else ln(c,y+dy,a,y,R(-bend,bend))
        out.append(st(p,b,pr,sp and R(*sp)))
    return out
def vrows(b,x0,y0,x1,y1,n,bend=0.015,lean=0.0,alt=True,sp=None,pr=None,jit=0.25,over=0.03):
    out=[]
    for i in range(n):
        x=x0+(x1-x0)*(i+R(-jit,jit))/max(1,n-1);a=y0+R(-over,over*2);c=y1-R(-over,over*2);dx=lean*(c-a)+R(-0.01,0.01)
        p=ln(x,a,x+dx,c,R(-bend,bend)) if (i%2==0 or not alt) else ln(x+dx,c,x,a,R(-bend,bend))
        out.append(st(p,b,pr,sp and R(*sp)))
    return out
def ground(b,n=7,sp=(900,1200)):
    return hrows(b,-0.05,0.03,1.05,0.97,n,0.005,sp=sp,pr=[1,1,1,1],jit=0.1)
