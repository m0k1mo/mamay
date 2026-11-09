import sys;sys.path.insert(0,'/home/claude/lab')
from mkfocus import build
F=dict(pickup=0.01,gloss=0.05,dilute=0.15,clump=0,tip="filbert",k=2,load=0.8,dryness=0.3,fluid=0.35)
V={"A F pick 0.01":dict(F),
   "B F pick 0 opaque":dict(F,pickup=0.0,opacity=1.0),
   "C F dry under":dict(F,dryfirst=True),
   "D F texture strong":dict(F,ent=1.5),
   "E F texture calm":dict(F,ent=0.4),
   "F F pick 0.35":dict(F,pickup=0.35),
   "G F sheen":dict(F,gloss=0.4),
   "H F scrub end":dict(F,load=0.6,dryness=0.6)}
print(build(V,int(sys.argv[1])))
