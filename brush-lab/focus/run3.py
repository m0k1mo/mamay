import sys;sys.path.insert(0,'/home/claude/lab')
from mkfocus import build
H=dict(pickup=0.15,gloss=0.05,dilute=0.15,clump=0.2)
V={"A H x2":dict(H,k=2),
   "B H soft merge":dict(H,clump=0,ent=1.4,stiff=0.6),
   "C H streak colors":dict(H,colors=["#ece6c0","#cfc79c","#f6f1d8"]),
   "D H dry under":dict(H,dryfirst=True),
   "E H no gloss no relief":dict(H,gloss=0,depth=0,push=0),
   "F H dry end":dict(H,load=0.7,dryness=0.75),
   "G H filbert merge":dict(H,tip="filbert",clump=0),
   "H H opaque body":dict(H,opacity=1.0,body=0.8,mix=0.2)}
print(build(V,int(sys.argv[1])))
