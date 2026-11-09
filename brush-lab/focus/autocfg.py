"""Per-reference tracing config: trace params + mass / line recipe makers (colour, size as fraction of width)."""
from refkit import *
def HWm(c,s): return oil(c,s,"flat",load=0.85,dry=0.4,ent=1.6,dil=0.3,pick=0.15,streak=0.08,tremor=0.2)
def HWl(c,s): return oil(c,s,"round",load=0.95,dry=0.15,ent=1.0,p2s=0.9,dil=0.15,streak=0.05)
def INKl(c,s): return ink(c,s,load=1,dry=0.15,ent=0.9,p2s=1.0)
def INKm(c,s): return ink(c,s,tip="flat",load=1,dry=0.1,ent=0.6,p2s=0.6)
def DRYm(c,s): return drybrush(c,s,tip="flat",load=0.8,dry=0.55,ent=1.5)
def DRYl(c,s): return drybrush(c,s,tip="round",load=0.8,dry=0.45,ent=1.3)
def GOm(c,s): return gouache(c,s,"flat",ent=0.7,dry=0.2)
def GOl(c,s): return gouache(c,s,"round",ent=0.6,p2s=0.9)
def OILm(c,s): return oil(c,s,"filbert",load=0.85,dry=0.3,ent=1.5,dil=0.2,pick=0.1)
def OILl(c,s): return oil(c,s,"round",load=0.9,dry=0.2,ent=1.0,p2s=0.9)
def IMPm(c,s): return impasto(c,s,"flat",ent=1.3)
def WAXm(c,s): return stick(c,s,"wax",ent=1.1)
def PASm(c,s): return stick(c,s,"pastel",ent=1.1)
def CHl(c,s): return stick(c,s,"charcoal",ent=1.0,p2s=0.8)
def PENm(c,s): return stick(c,s,"pencil",ent=0.8)
def WCm(c,s): return wc(c,s,0.55,0.6,0.15,strength=1.0)
def WCl(c,s): return wc(c,s,0.45,0.2,0.1,strength=1.0)
HW=dict(k=6,mass=HWm,line=HWl,spacing=0.6,maxsize=13,ang=0.0,close=1,line_max=3.5)
CFG={
 1:dict(HW,ang=None,crop=(0.1,0.03,0.9,0.96)),2:dict(HW,crop=(0.03,0.04,0.97,0.98)),3:dict(HW,k=6),4:dict(HW,k=5,crop=(0.03,0.04,0.97,0.96)),5:dict(HW,k=7,crop=(0.04,0.02,0.96,0.98)),6:dict(HW,k=5,crop=(0.03,0.04,0.97,0.96)),7:dict(HW,k=8),8:dict(HW,k=6,ang=None,crop=(0.1,0.04,0.9,0.96)),
 9:dict(HW,k=6,crop=(0.02,0.03,0.98,0.97)),10:dict(HW,k=6,crop=(0.08,0.05,0.92,0.95)),11:dict(HW,k=5,crop=(0.03,0.03,0.97,0.97)),12:dict(HW,k=6,ang=None,crop=(0.1,0.04,0.9,0.96)),13:dict(HW,k=6,crop=(0.04,0.03,0.96,0.97)),14:dict(HW,k=5,crop=(0.06,0.04,0.94,0.96)),
 15:dict(lines_for=True,k=2,gw=260,line_max=9,close=0,blur=0,opn=0,mass=INKm,line=INKl),
 16:dict(lines_for=True,k=5,gw=200,line_max=12,close=1,mass=WCm,line=lambda c,s:wc(c,s,0.3,0.0,0.1,strength=1.0,pick=0.1),min_frac=0.002),
 17:dict(k=4,gw=240,mass=DRYm,line=INKl,line_max=2.5,close=0,opn=0,blur=0.5,maxsize=7,spacing=0.6,crop=(0.0,0.1,1.0,1.0)),
 18:dict(k=3,gw=220,mass=WAXm,line=lambda c,s:stick(c,s,"wax",ent=1.0,p2s=0.6),line_max=6,close=0,blur=0.6,opn=0,maxsize=5,spacing=0.9),
 19:dict(lines_for=True,k=2,gw=240,mass=CHl,line=CHl,line_max=20,close=0,blur=0.4,opn=0),
 20:dict(bg='light',k=2,gw=160,mass=WAXm,line=WAXm,maxsize=6,spacing=0.8),
 21:dict(k=4,gw=240,mass=GOm,line=lambda c,s:ink(c,s,load=0.9,dry=0.35,ent=1.2,p2s=0.9),line_max=6,maxsize=10,spacing=0.55),
 22:dict(lines_for=True,k=2,gw=240,mass=INKm,line=lambda c,s:ink(c,s,tip="flat",load=1,dry=0.35,ent=1.2,p2s=0.9),line_max=12,close=0,blur=0,opn=0,crop=(0.3,0.0,1.0,1.0)),
 23:dict(k=3,gw=200,mass=lambda c,s:drybrush(c,s,tip="flat",load=0.7,dry=0.6,ent=1.6),line=INKl,line_max=4,crop=(0.0,0.17,1.0,0.88)),
 24:dict(k=7,gw=200,mass=OILm,line=OILl,spacing=0.55,maxsize=8),
 26:dict(lines_for=True,k=2,gw=220,mass=INKm,line=INKl,line_max=9,close=0,blur=0,opn=0),
 27:dict(k=3,gw=160,mass=IMPm,line=IMPm,maxsize=10,spacing=0.6),
 28:dict(lines_for=True,k=3,gw=240,mass=INKm,line=INKl,line_max=8,close=0,blur=0,opn=0,crop=(0.0,0.06,1.0,1.0)),
 29:dict(lines_for=True,k=2,gw=200,mass=WCm,line=lambda c,s:wc(c,s,0.5,0.2,0.05,strength=0.95),line_max=20,close=1,crop=(0.0,0.05,1.0,1.0)),
 30:dict(k=4,gw=200,mass=lambda c,s:gouache(c,s,"flat",ent=0.9,dry=0.25),line=INKl,line_max=7,maxsize=12),
 31:dict(lines_for=True,k=2,gw=260,mass=INKm,line=lambda c,s:ink(c,s,load=0.8,dry=0.4,ent=1.2,p2s=0.8),line_max=6,close=0,blur=0,opn=0),
 32:dict(k=3,gw=160,mass=IMPm,line=IMPm,maxsize=14,spacing=0.6,ang=0.0),
 34:dict(k=7,mass=OILm,line=OILl,maxsize=12,spacing=0.6,ang=0.0),
 36:dict(lines_for=True,k=2,gw=200,mass=GOm,line=lambda c,s:gouache(c,s,"flat",ent=0.8,dry=0.3,p2s=0.8),line_max=12,close=1),
 37:dict(k=8,mass=OILm,line=OILl,maxsize=10,spacing=0.6),
 38:dict(k=3,gw=200,mass=PENm,line=PENm,maxsize=2.5,spacing=1.4,line_max=1.5),
 39:dict(k=5,gw=160,mass=IMPm,line=IMPm,maxsize=12,spacing=0.6),
 40:dict(k=6,gw=160,mass=WCm,line=WCm,maxsize=14,spacing=0.7),
 41:dict(k=6,gw=200,mass=PENm,line=PENm,maxsize=2.5,spacing=1.3,line_max=1.5),
 42:dict(k=6,gw=200,mass=PASm,line=PASm,maxsize=6,spacing=0.7),
 43:dict(bg='light',k=2,gw=160,mass=DRYm,line=DRYl,maxsize=14,spacing=0.6),
 44:dict(close=0,opn=0,blur=0.6,maxsize=9,spacing=0.55,flowlen=14,k=3,gw=200,mass=lambda c,s:oil(c,s,"flat",load=1,dry=0.25,ent=1.4,dil=0.1,gloss=0.45),line=OILl,line_max=2),
 45:dict(k=5,gw=160,mass=PASm,line=PASm,maxsize=8,spacing=0.65),
 47:dict(k=3,gw=160,crop=(0.12,0.08,0.87,0.96),mass=lambda c,s:knife(c,s),line=lambda c,s:knife(c,s),ang=0.0,maxsize=14,spacing=0.6,close=2),
 48:dict(bg='light',k=2,gw=160,mass=lambda c,s:gouache(c,s,"flat",ent=0.9,dry=0.3,dil=0.35),line=GOl,maxsize=14,ang=0.0,spacing=0.6),
 49:dict(lines_for=True,k=2,gw=200,mass=INKm,line=lambda c,s:ink(c,s,load=1,dry=0.1,ent=0.8,p2s=0.9),line_max=12,close=1),
 50:dict(k=6,gw=160,mass=GOm,line=IMPm,maxsize=10,ang=0.0),
}
