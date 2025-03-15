#%% 
"""
Lungime subsir maxim din sir PD 
La if v[i]<v[j] and lung[j]>lmax: o data imi verifica daca numarul cu o pozitie mai mare e mai mare decat numarul meu actual + verifica cate numere in dreapta sunt mai mari decat numarul meu - 1
"""
#v=[5,3,7,8,6,10]
v=[8,3,1,4,6,5,11]
n=len(v)
lung=[1]*n
succ=[-1]*n #[None]*n



lung[n-1]=1 #stim direct
#ord de calcul - de la ultimul catre primul
for i in range(n-2,-1,-1):
    lmax=0
    for j in range(i+1,n):
        if v[i]<v[j] and lung[j]>lmax:
            lmax=lung[j]
            succ[i]=j
    lung[i]=1+lmax

print(*lung)
print(*succ)

pmax=0
for i in range(n):
    if lung[i]>lung[pmax]:
        pmax=i
print("lungimea maxima ",lung[pmax])

p=pmax
for i in range(lung[pmax]):
    print(v[p],end=" ")
    p=succ[p]

#numaram cate subsiruri optime exista
print(lung)

nr=[0]*n
nr[n-1]=1
for i in range(n-2,-1,-1):
    for j in range(i+1,n):
        if v[i]<v[j] and lung[j]==lung[i]-1:
            nr[i]+=nr[j]
    if nr[i]==0:
        nr[i]=1
print(nr)
nr_optim=0
for i in range(n):
    if lung[i]==lung[pmax]:
        nr_optim+=nr[i]
print(nr_optim)
#%%
"""
Problema monede PD 
"""
# S=12
S=17
v=[1,6,7]
inf=S+1
nr=[inf]*(S+1) #daca nu se poate descompune -> inf =S+1
nr[0]=0
desc=[inf]*(S+1)

for s in range(1,S+1):
    if s in v:
        nr[s]=1
        desc[s]=s # vectorul suma ramasa optim 
    else:
        nrmin=inf
        for moneda in v:
            if moneda<=s and nr[s-moneda]<nrmin:
                nrmin=nr[s-moneda]
                desc[s]=moneda
        if nrmin<inf:
            nr[s]=1+nrmin
print(nr)
print(desc)
if nr[S]==inf:
    print("nu se poate plati suma")
else:
    s=S
    while s!=0:
        print(desc[s],end=" ")
        s=s-desc[s]

def descompune(s):

    if nr[s] is not None:
        return nr[s]
    if s==0:
        nr[0]=0
        return 0
    nrmin = inf
    for moneda in v:
        if moneda <= s and  descompune(s - moneda)< nrmin: #ar fi mers memorat descompune(s - moneda) in variabia
            nrmin = descompune(s - moneda)
    if nrmin<inf:
        nr[s]=1+nrmin
    else:
        nr[s]=inf
    return nr[s]

nr=[None]*(S+1)
print()
print(descompune(S))
#%%
"""
Problema rucsac PD
"""
f=open(r"C:\Users\Ciprian\OneDrive - unibuc.ro\Desktop\facultate\Anul I sem I\PA (restanta)\Pentru examen\rucsac.in",'r')
g=[int(x) for x in f.readline().split()]
c=[int(x) for x in f.readline().split()]
G=int(f.readline())
f.close()
n=len(g)
g.insert(0,0) #obiectul 1 va fi pe pozitia 1
c.insert(0,0)
s=[[0 for i in range(G+1)] for j in range(n+1)]
#prima linie si prima coloana raman 0 (corespun 0 obiecte/greutate 0
for i in range(1,n+1):
    for gr in range(1, G+1):
        if g[i]>gr:
            s[i][gr]=s[i-1][gr] #nu putem lua obiectul i, are greutate prea amre
        else:
            s[i][gr] =max(s[i-1][gr], s[i-1][gr-g[i]]+c[i])
print(*s,sep="\n")
print(s[n][G])

#determinarea solutiei - de la coltul de jos inapoi
print("obiectele")
i=n
gr=G
while i>0 and gr >0:
    if s[i][gr]!=s[i-1][gr]: #luam obiectul i
        print(i)
        gr-=g[i]
        i-=1
    else:
        i-=1
#%%
"""
traseu triunghi PD
"""
# a=[[2],[4,5],[10,7,3],[1,5,2,1],[8,4,5,6,7,11]]
a=[[2],
   [4,5],
   [10,7,3],
   [1,5,2,1]]

#varianta recursiva
def suma(i,j):
    global nr #numarul de apeluri recursive<=2*nr de elemente
    nr=nr+1
    if s[i][j] is not None: #daca este deja rezolvata-returnam valoarea, nu mai apelam recursiv
        return s[i][j]
    if i==n-1:
        s[i][j]=a[i][j]
        return a[i][j]
    s[i][j]=a[i][j]+max(suma(i+1,j), suma(i+1,j+1))
    return s[i][j]
    #return a[i][j]+max(suma(i+1,j), suma(i+1,j+1))-: exponential

def suma_nerec():
    s = [[None for j in range(i + 1)] for i in range(n)]
    #s[n-1][:]=a[n-1]
    for j in range(n):
        s[n-1][j]=a[n-1][j]
    for i in range(n-2, -1,-1):
        for j in range(i+1):
            s[i][j]=a[i][j]+max(s[i+1][j],s[i+1][j+1])
    print(s[0][0])
    print(s)

nr=0
n=len(a)
s=[[None for j in range(i+1)] for i in range(n)]
print(suma(0,0))
print(s)
print(nr,"apeluri")
suma_nerec()

def traseu(i,j):
    if i==n-1:
        print(i,j)
    else:
        print(i,j)
        if s[i][j]==a[i][j]+s[i+1][j]: #if s[i+1][j]>s[i+1][j+1]
            traseu(i+1,j)
        else:
            traseu(i+1,j+1)


traseu(0,0)

#Observatii:
#1. Putem afisa traseul si nerecursiv
#2. Putem folosi tot matricea a pentru a caclula suma, in loc de s

