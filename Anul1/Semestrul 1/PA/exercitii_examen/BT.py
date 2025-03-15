#%% 
"""
Permutarile multimii {1,2,..,n}
1. Reprez solutiei
x=x_0,.., x_{n-1}
2) Fiecare element x_k poate lua valorile
x_k - 1,2..., n
3) Conditiile finale
elementele sa fie distincte x_i!=x_j
4) Conditiile de continuare la pasul k (!!) - cand ii dam valoare lui x_k
x_k!=x_0,...,x_{k-1}
"""
def continuare(k,x):
    for i in range(k): #x[k]in x[:k] x.index(x[k],0,k)...
        if x[i]==x[k]:
            return False
    return True

def back(k,x,n):
    if k == n: #daca am completat toate pozitiile si incerc sa completez x_n -> avem solutie
        #testam conditiile finale - doar in cazul in care cond de continuare nu au fost suficiente
        print(*x)
    else:
        #luam la rand valorile posibile pentru x_k
        for i in range(1,n+1):
            x[k]=i
            if continuare(k,x):
                back(k+1,x,n)
def permutari(n):
    x=[0]*n
    back(0,x,n)
permutari(3)

def permutari_nerecursiv(n):
    x=[0]*n
    k=0
    while k>=0: #cand k devine -1 => stop
        if k==n:
            print(*x,sep=",")
            k-=1
        else: #dam lui x[k] urmatarea valoare posibila, daca mai sunt valori
            if x[k]<n:
                x[k]=x[k]+1
                if continuare(k,x):
                    k+=1
            else:
                x[k]=0
                k-=1
# permutari_nerecursiv(3)

#%%
"""
Aranjamente de m din multimea {1,2,..,n}
1 2 3
2 3 1
3 2 1
1. Reprez solutiei
x=x_0,.., x_{m-1}
2) Fiecare element x_k poate lua valorile
x_k - 1,2..., n
3) Conditiile finale
elementele sa fie distincte x_i!=x_j
4) Conditiile de continuare la pasul k (!!) - cand ii dam valoare lui x_k
x_k!=x_0,...,x_{k-1}
"""
def continuare(k,x):
    for i in range(k): #x[k]in x[:k] x.index(x[k],0,k)...
        if x[i]==x[k]:
            return False
    return True

def back(k,x,n,m):
    if k == m: #daca am completat toate pozitiile si incerc sa completez x_m -> avem solutie
        #testam conditiile finale - doar in cazul in care cond de continuare nu au fost suficiente
        print(*x)
        #daca x retine indici din A(!!!de la 1 la n)
        for i in range(m):
            print(A[x[i]-1],end=" ")
        print()
    else:
        #luam la rand valorile posibile pentru x_k
        for i in range(1,n+1): #for i in A, daca x contine direct elemente din A
            x[k]=i
            if continuare(k,x):
                back(k+1,x,n,m)
def aranjamente(m,n):
    x=[0]*m
    back(0,x,n,m)
A=["s1","s2","s3","s4"]
aranjamente(3,4)
#%%
"""
Combinari  de m din multimea {1,2,..,n}
1 2 3 = 2 3 1 = 3 2 1 -> o generam doar pe cea ord crescator
1. Reprez solutiei
x=x_0,.., x_{m-1}
2) Fiecare element x_k poate lua valorile
x_k - 1,2..., n
3) Conditiile finale
elementele sa fie distincte x_i!=x_j +Crescator
4) Conditiile de continuare la pasul k (!!) - cand ii dam valoare lui x_k
x_k>x[k-1] (Deci x_k este diferit de x_0,..,x_{k-1}
"""
def continuare(k,x):
     return k==0 or x[k]>x[k-1]

def back(k,x,n,m):
    if k == m: #daca am completat toate pozitiile si incerc sa completez x_m -> avem solutie
        #testam conditiile finale - doar in cazul in care cond de continuare nu au fost suficiente
        print(*x)


    else:
        #luam la rand valorile posibile pentru x_k
        for i in range(1 if k==0 else x[k-1]+1,n+1):
        #for i in range(1,n+1):
            x[k]=i
            #if continuare(k,x):
            back(k+1,x,n,m)
def combinari(m,n):
    x=[0]*m
    back(0,x,n,m)

combinari(3,4)
#%%

