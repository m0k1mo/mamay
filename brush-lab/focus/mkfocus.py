import json,sys,math,random
def lin(h):
    h=h.lstrip('#');v=[int(h[i:i+2],16)/255 for i in (0,2,4)]
    f=lambda c: c/12.92 if c<=0.04045 else ((c+0.055)/1.055)**2.4
    r,g,b=[round(f(c),4) for c in v];return {"r":r,"g":g,"b":b,"a":1}
BASE=dict(size=130,stiff=0.8,load=1.0,give=0.8,dryness=0.5,clump=0.8,pickup=0.4,ent=0.9,tip="flat",
          fluid=0.2,body=0.6,opacity=0.95,gloss=0.3,mix=0.5,dilute=0.25,solvent="turpentine",relief=0.0,weave=0.0,push=0.3,depth=0.5,tex="bristles")
def recipe(c,p):
    r=dict(size=p["size"],path={"smoothing":p.get("smooth",0.3),"pressureToSize":p.get("p2s",0.45),"tremor":p.get("tremor",0.8)},
      tool={"kind":"hairs","tip":p["tip"],"stiffness":p["stiff"],"load":p["load"],"give":p["give"],"dryness":p["dryness"],"clump":p["clump"],"pickup":p["pickup"],"bristle":1,"entropy":p["ent"]},
      
      material={"color":lin(c),"fluidity":p["fluid"],"body":p["body"],"opacity":p["opacity"],"gloss":p["gloss"],"strength":0.5,"tack":0.4,"mix":p["mix"],"solvent":p["solvent"],"dilute":p["dilute"]},
      counterform={"tool":p["tex"],"push":p["push"],"depth":p["depth"]},
      surface={"relief":p["relief"],"weave":p["weave"],"weaveSize":8})
    if p.get("colors"): r["tool"]["colors"]=[lin(x) for x in p["colors"]]; r["tool"]["colorPattern"]=p.get("pattern","streaks")
    return r
def pl(p):return [[round(x,1),round(y,1)] for x,y in p]
def stroke(x0,y0,x1,y1,bend,n=24,k=1):
    return pl([(k*(x0+(x1-x0)*t),k*(y0+(y1-y0)*t+bend*math.sin(math.pi*t))) for t in [i/(n-1) for i in range(n)]])
def sheet(name,k=1,dryfirst=False):
    st=[{"points":stroke(300,40,320,620,10,k=k),"pressure":[1,1,1,1],"speed":700*k,"rest":0.2,"brush":name+" under"},
        {"points":stroke(560,40,540,620,-10,k=k),"pressure":[1,1,1,1],"speed":700*k,"rest":0.5,"brush":name+" under"}]
    st+=[{"points":stroke(60,150,940,130,-25,k=k),"pressure":[1,0.9,0.85,0.6,0.25],"speed":550*k,"rest":0.4,"brush":name},
         {"points":stroke(80,330,900,360,30,k=k),"pressure":[0.95,0.7,0.8,0.5,0.1],"speed":800*k,"rest":0.4,"brush":name},
         {"points":stroke(120,520,520,505,8,k=k),"pressure":[1,1,0.9,0.7],"speed":350*k,"rest":0.4,"brush":name}]
    if dryfirst: st[2]["dry"]=True
    return {"width":1000*k,"height":660*k,"background":"#2b2f1c","settle":8,"strokes":st}
def build(variants,ver,pid="oil-focus",folder="Oil focus"):
    B=[];names=[]
    for nm,ch in variants.items():
        p=dict(BASE);p.update(ch);full=f"{nm}";k=p.pop("k",1);p["size"]*=k
        under=recipe("#45607a",dict(p,dilute=0.5,dryness=0.2,size=110*k,colors=None,dryfirst=None));
        B.append({"name":full+" under","recipe":under})
        B.append({"name":full,"recipe":recipe("#ece6c0",p),"sheet":sheet(full,k,bool(p.get("dryfirst")))})
        names.append(f"{folder} · {full}".lower())
    json.dump({"id":pid,"version":ver,"folder":folder,"brushes":B},open(f'/home/claude/lab/packs/{pid}.json','w'),ensure_ascii=False,indent=1)
    return ",".join(names)
if __name__=="__main__":
    V={"A base":{},
       "B no solvent body 0.45":{"dilute":0.0,"body":0.45},
       "C dilute 0.4":{"dilute":0.4},
       "D worn tip":{"tip":"worn","dilute":0.3},
       "E stiff dry":{"stiff":0.95,"load":0.7,"give":0.6,"dryness":0.7},
       "F texture deep":{"depth":0.9,"push":0.6},
       "G soft clump":{"clump":0.5,"ent":1.3,"stiff":0.6},
       "H linen in brush":{"relief":0.5,"weave":0.7}}
    print(build(V,int(sys.argv[1])))
