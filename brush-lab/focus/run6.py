import sys;sys.path.insert(0,'/home/claude/lab')
from mkfocus import build
B=dict(pickup=0.01,gloss=0.2,dilute=0.15,clump=0,tip="filbert",k=2,load=0.8,dryness=0.3,fluid=0.35,ent=1.5)
V={"A best filbert":dict(B),
   "B flat":dict(B,tip="flat"),
   "C round":dict(B,tip="round"),
   "D worn":dict(B,tip="worn"),
   "E swell":dict(B,p2s=0.8),
   "F steady hand":dict(B,tremor=0,smooth=0.6),
   "G soft hairs":dict(B,stiff=0.5,give=1.0),
   "H narrow":dict(B,size=100)}
print(build(V,int(sys.argv[1])))
