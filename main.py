import json as j,os,sys,urllib.request as r
I=os.environ.get("MAKEFUN_ENV_URL") or sys.exit("!")
def p(a,b):
 q=r.Request(I+a,data=j.dumps(b).encode())
 with r.urlopen(q) as x:return j.load(x)
V=[0,100,325,330,500,900,0];M=10000;L=60000
N=[-33,-31,-18,-14,14,18,31,33];G=[-17,-16,-15,-1,1,15,16,17]
R=[-16,-1,1,16];D=[-17,-15,15,17];Z=[i*16+f for i in range(8)for f in range(8)]
P=[0,0,N,D,R,R+D,G];W=[0,0,1,8,8,8,1]
b=[0]*128;s=1;c=0;k=[0,0];n=0;T={}
def Y(x):return chr(97+(x&7))+str((x>>4)+1)
def l(f):
 global b,s,c
 b=[0]*128;a=f.split();r=7;g=0
 for ch in a[0]:
  if ch=="/":r-=1;g=0
  elif ch.isdigit():g+=int(ch)
  else:
   i="PNBRQK".find(ch.upper());v=(i+1)*(1 if ch.isupper() else-1);x=r*16+g;b[x]=v
   if abs(v)==6:k[v>0]=x
   g+=1
 s=1 if a[1]=="w" else-1;c=0
 c=sum(1<<i for i,ch in enumerate("KQkq")if ch in a[2])
def J(x,y):
 for o in(15,17):
  z=x-o*y
  if not z&136 and b[z]==y:return 1
 for o in N+G:
  z=x+o
  if not z&136 and b[z]==(y*2 if o in N else y*6):return 1
 for d in R+D:
  z=x+d
  while not z&136:
   v=b[z]
   if v:
    if v==y*5 or(v==y*4 and d in R)or(v==y*3 and d in D):return 1
    break
   z+=d
 return 0
def g(o=False):
 m=[]
 for x in Z:
  v=b[x]
  if v*s<=0:continue
  t=abs(v)
  if t==1:
   d=16*s
   for y in(x+d,x+15*s,x+17*s):
    if y&136:continue
    w=b[y];u=y==x+d
    if u:
     if w:continue
    elif w*s<0:pass
    else:continue
    if(y>>4)==(7 if s>0 else 0):
     for q in(5,4,3,2):m.append(x|(y<<7)|(q<<14))
    elif u:
     if not o:m.append(x|(y<<7))
    else:m.append(x|(y<<7))
    if u and not o and(x>>4)==(1 if s>0 else 6):
     z=x+2*d
     if b[z]==0:m.append(x|(z<<7))
  else:
   for d in P[t]:
    y=x+d
    for _ in range(W[t]):
     if y&136:break
     w=b[y]
     if w==0:
      if not o:m.append(x|(y<<7))
     else:
      if w*s<0:m.append(x|(y<<7))
      break
     y+=d
   if t==6 and not o:
    kf=k[s>0]
    for kt,ma,dr in((6,1,1),(2,2,-1))if s>0 else((118,4,1),(114,8,-1)):
     if c&ma and not b[kf+dr]and not b[kf+2*dr]and(dr>0 or not b[kf-3])and not J(kf,-s)and not J(kf+dr,-s)and not J(kf+2*dr,-s):m.append(kf|(kt<<7))
 return m
def m(v):
 global s,c
 f=v&127;t=(v>>7)&127;w=v>>14;z=(list(b),s,c,list(k));p=b[f];y=b[t];q=t
 if abs(p)==1:
  if w:p=w*s
 else:
  if abs(p)==6 and abs(t-f)==2:
   if t>f:b[f+1]=b[f+3];b[f+3]=0
   else:b[f-1]=b[f-4];b[f-4]=0
 if abs(p)==6:c&=~(3 if p>0 else 12)
 for sq,ma in((0,2),(7,1),(112,8),(119,4)):
  if f==sq or t==sq:c&=~ma
 b[t]=p;b[f]=0
 if abs(p)==6:k[p>0]=t
 s=-s
 return z+(y,q)
def U(z):
 global s,c
 b[:]=z[0];s,c=z[1],z[2];k[:]=z[3]
def E():
 z=0
 for x in Z:
  v=b[x]
  if not v:continue
  t=abs(v);o=v>0;r=x>>4
  if not o:r=7-r
  z+=(V[t]+(r*5 if t==1 else 0))*(1 if o else-1)
 return z if s>0 else-z
B=StopIteration
def O(r):
 r.sort(key=lambda v:V[abs(b[(v>>7)&127])],reverse=True)
def S(d,a,c,y):
 global n
 n+=1
 if n>=L:raise B
 k_=(tuple(b),s,c)
 z=T.get(k_)
 if z and z[0]>=d:return z[1]
 x=J(k[s>0],-s)
 if d<=0:
  if not x:
   t=E()
   if t>=c:return t
   if t>a:a=t
   w=t
  else:w=-M-1
  r=g()if x else g(True)
  O(r)
  for v in r:
   z=m(v)
   if J(k[(-s)>0],s):U(z);continue
   o=-S(0,-c,-a,y+1);U(z)
   if o>w:w=o
   if o>=c:return o
   if o>a:a=o
  if x and w==-M-1:return-M+y
  return w
 r=g();O(r);w=-M-1;q=0
 for v in r:
  z=m(v)
  if J(k[(-s)>0],s):U(z);continue
  q+=1
  o=-S(d-1,-c,-a,y+1)
  U(z)
  if o>w:w=o
  if o>a:a=o
  if a>=c:break
 if not q:return-M+y if J(k[s>0],-s)else 0
 T[k_]=(d,w)
 return w
def C():
 global n
 r=g();z=[]
 for v in r:
  w=m(v)
  if not J(k[(-s)>0],s):z.append(v)
  U(w)
 if len(z)==1:return z[0]
 n=0;W=z[0];o={v:0 for v in z}
 for d in range(1,13):
  n=0;a=-M-1;X=W
  try:
   for v in z:
    w=m(v);s2=-S(d-1,-M-1,-a,1);U(w);o[v]=s2
    if s2>a:a=s2;X=v
   z.sort(key=lambda v:-o[v]);W=X
   if a>=M-100:break
  except B:break
 return W
def main():
 while True:
  g=p("/game",{})
  if g["status"]=="done":break
  while g["status"]=="your_move":
   l(g["fen"]);v=C()
   f=v&127;t=(v>>7)&127;w=v>>14
   u=Y(f)+Y(t)+("nbrq"[w-2]if w else"")
   g=p("/move",{"game":g["game"],"move":u})
if __name__=="__main__":main()
