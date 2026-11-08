import sys;sys.path.insert(0,'/home/claude/lab')
from mkfocus import build
G=dict(pickup=0.15,gloss=0.05,dilute=0.15,clump=0,tip="filbert",k=2)
V={"A G x2":dict(G),
   "B G x2 soft":dict(G,ent=1.4,stiff=0.6),
   "C G x2 mix low":dict(G,mix=0.1),
   "D G x2 no pickup":dict(G,pickup=0.0),
   "E G x2 dilute 0.3":dict(G,dilute=0.3),
   "F G x2 wet load":dict(G,load=0.8,dryness=0.3,fluid=0.35),
   "G G x2 fine hairs":dict(G,ent=1.8,stiff=0.5,give=1.0),
   "H flat x2 soft":dict(G,tip="flat",ent=1.4,stiff=0.6)}
print(build(V,int(sys.argv[1])))
