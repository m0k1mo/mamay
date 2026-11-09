"""Paint by tracing a reference: colour masses -> rows of strokes along the brush direction; thin dark shapes -> centre lines.
Returns layers [(hex colour, kind 'mass'|'line', [ (points_norm, pressures) ...], size_norm)] in painting order, and the bg colour."""
import numpy as np,math,glob,json
from PIL import Image
from sklearn.cluster import KMeans
from scipy import ndimage as ndi
from skimage import color,morphology,measure
D={x['n']:x for x in json.load(open('/home/claude/school/all_results.json'))}
def load(n,gw=160,crop=None):
    im=Image.open(glob.glob('/home/claude/refs/img/'+D[n]['id']+'*')[0]).convert('RGB')
    if crop: w,h=im.size;im=im.crop((int(crop[0]*w),int(crop[1]*h),int(crop[2]*w),int(crop[3]*h)))
    gh=round(gw*im.height/im.width);return np.asarray(im.resize((gw,gh),Image.LANCZOS)).astype(float)/255,im
def hexc(rgb): return '#%02x%02x%02x'%tuple(int(max(0,min(1,c))*255) for c in rgb)
def clusters(a,k,seed=0):
    lab=color.rgb2lab(a).reshape(-1,3);km=KMeans(k,n_init=4,random_state=seed).fit(lab)
    lbl=km.labels_.reshape(a.shape[:2]);cols=[a[lbl==i].mean(0) for i in range(k)]
    return lbl,cols
def orient(a,mask):
    L=color.rgb2gray(a);gy,gx=np.gradient(ndi.gaussian_filter(L,1.0))
    m=ndi.binary_erosion(mask,iterations=1)
    if m.sum()<10: m=mask
    jxx=(gx*gx)[m].sum();jyy=(gy*gy)[m].sum();jxy=(gx*gy)[m].sum()
    th=0.5*math.atan2(2*jxy,jxx-jyy)   # gradient direction
    return th+math.pi/2                  # along the streaks
def rows(mask,ang,spacing,minlen,step=2.0,jit=0.0,rng=None):
    h,w=mask.shape;ca,sa=math.cos(ang),math.sin(ang);out=[]
    ys,xs=np.nonzero(mask)
    if len(xs)==0: return out
    # coordinates across (v) and along (u) the stroke direction
    u=xs*ca+ys*sa;v=-xs*sa+ys*ca
    v0,v1=v.min(),v.max();u0,u1=u.min()-2,u.max()+2
    k=0;vv=v0+spacing*0.5
    while vv<=v1:
        us=np.arange(u0,u1,step);px=us*ca-vv*sa;py=us*sa+vv*ca
        ok=(px>=0)&(px<w-0.5)&(py>=0)&(py<h-0.5)
        inside=np.zeros(len(us),bool);inside[ok]=mask[np.round(py[ok]).astype(int),np.round(px[ok]).astype(int)]
        # runs
        i=0
        while i<len(us):
            if inside[i]:
                j=i
                while j<len(us) and inside[j]: j+=1
                if (j-i)*step>=minlen:
                    seg=[(px[t],py[t]) for t in range(i,j,max(1,int(4/step)))]+[(px[j-1],py[j-1])]
                    if jit and rng is not None: seg=[(x+rng.normal(0,jit),y+rng.normal(0,jit)) for x,y in seg]
                    if k%2: seg=seg[::-1]
                    out.append(seg)
                i=j
            else: i+=1
        vv+=spacing;k+=1
    return out
def skeleton_paths(mask,minlen=6):
    sk=morphology.skeletonize(mask);dt=ndi.distance_transform_edt(mask)
    pts=set(zip(*np.nonzero(sk)))
    def nb(p):
        y,x=p;return [(y+dy,x+dx) for dy in (-1,0,1) for dx in (-1,0,1) if (dy or dx) and (y+dy,x+dx) in pts]
    deg={p:len(nb(p)) for p in pts};seen=set();paths=[]
    starts=[p for p in pts if deg[p]==1]+[p for p in pts if deg[p]>2]+list(pts)
    for s in starts:
        for n0 in nb(s):
            if (s,n0) in seen: continue
            path=[s,n0];seen.add((s,n0));seen.add((n0,s));prev,cur=s,n0
            while deg.get(cur,0)==2:
                nx=[q for q in nb(cur) if q!=prev]
                if not nx: break
                q=nx[0]
                if (cur,q) in seen: break
                seen.add((cur,q));seen.add((q,cur));path.append(q);prev,cur=cur,q
            if len(path)>=minlen: paths.append(path)
    out=[]
    for p in paths:
        p=p[::2] if len(p)>12 else p
        out.append(([(x,y) for y,x in p],[float(dt[y,x]) for y,x in p]))
    return out,dt
def trace(n,k=6,gw=160,crop=None,bg=None,order="area",line_max=2.6,spacing=0.75,minarea=12,min_frac=0.004,seed=0,merge=8.0,lines_for=None,mass_size=None,dark_last=True,blur=1.2,ang=None,close=2,minrun=None,maxsize=14.0,opn=1):
    a,_=load(n,gw,crop);h,w=a.shape[:2]
    ab=np.stack([ndi.median_filter(a[...,c],size=3) for c in range(3)],-1) if blur else a
    if blur: ab=np.stack([ndi.gaussian_filter(ab[...,c],blur) for c in range(3)],-1)
    lbl,cols=clusters(ab,k,seed)
    # merge near colours
    lab=[color.rgb2lab(np.array([[c]]))[0,0] for c in cols];alias=list(range(k))
    for i in range(k):
        for j in range(i):
            if np.linalg.norm(lab[i]-lab[j])<merge: alias[i]=alias[j];break
    lbl=np.vectorize(lambda t: alias[t])(lbl)
    ids=sorted(set(alias),key=lambda i:-(lbl==i).sum())
    border=np.concatenate([lbl[0],lbl[-1],lbl[:,0],lbl[:,-1]])
    bgid=max(ids,key=lambda i:(border==i).sum()) if bg is None else (max([i for i in ids if (lbl==i).sum()>0.08*h*w],key=lambda i:color.rgb2lab(np.array([[a[lbl==i].mean(0)]]))[0,0,0]) if bg=='light' else bg)
    cols={i:a[lbl==i].mean(0) for i in ids}
    rest=[i for i in ids if i!=bgid and (lbl==i).sum()>=min_frac*h*w]
    if dark_last: rest.sort(key=lambda i:(-(lbl==i).sum()*(1 if color.rgb2lab(np.array([[cols[i]]]))[0,0,0]>35 else 0.001)))
    layers=[];rng=np.random.default_rng(seed)
    for i in rest:
        m=lbl==i
        if opn: m=ndi.binary_opening(m,iterations=opn)
        m=morphology.remove_small_objects(m,max_size=minarea)
        if close: m=ndi.binary_closing(m,iterations=close)
        if m.sum()<minarea: continue
        dt=ndi.distance_transform_edt(m);comp,nc=ndi.label(m)
        masses=[];lines=[];msizes=[]
        csz=mass_size or (max(3.0,min(maxsize,np.percentile(dt[m],75)*1.6)) if m.any() else 4)
        for c in range(1,nc+1):
            cm=comp==c;th=dt[cm].max()
            if th<=line_max or lines_for is True:
                for pts,wd in skeleton_paths(cm)[0]: lines.append((pts,wd))
            else:
                sz=csz
                an=orient(a,cm) if ang is None else ang
                for seg in rows(cm,an,sz*spacing,minrun or max(sz*1.2,5),jit=0.12,rng=rng): masses.append(seg)
                msizes.append(sz)
        hc=hexc(cols[i])
        if masses: layers.append((hc,"mass",masses,float(np.median(msizes))/w))
        if lines:
            wmax=max(max(wd) for _,wd in lines);layers.append((hc,"line",lines,2*wmax/w))
    return hexc(cols[bgid]),layers,(w,h)
