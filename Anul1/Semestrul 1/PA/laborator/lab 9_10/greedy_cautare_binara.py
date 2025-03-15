# Cautare binare 
#%%
def cautare_binara(l, st, dr, x):  
    if st <= dr: 
        mij = (st + dr) // 2 
        if(l[mij]==x):
            return 1
        if l[mij] > x:
            return cautare_binara(l, st, mij -1, x)
        return cautare_binara(l, mij + 1, dr, x) 
    return 0 
print(cautare_binara([2, 11, 15, 22, 36, 45, 58], 0, 6, 7))
#%% 
# Pr 1 (Nu am gasit fisierul corect)
def maxim(l, st, dr):
    if st == dr:
        return l[st]
    mij = (st + dr) // 2
    if l[mij] > l[mij + 1] and l[mij] > l[mij - 1]: 
        return l[mij]
    if l[mij] < l[mij + 1]: 
        return maxim(l, mij + 1, dr)
    return maxim(l, st, mij - 1)
print(maxim([4,8,10,11,5],0,4))
#%% 
def prima_ap(l, x):
    st = 0 
    dr = len(l) - 1
    p = -1
    while(st <= dr):
        mij = (st + dr) // 2
        if(l[mij] == x):
            p = mij
            dr = mij - 1 
        else: 
            if l[mij] > x:
                dr = mij - 1
            else:
                st = st + 1 
    return p 
def ultima_ap(l, x):
    st = 0 
    dr = len(l) - 1
    u = -1
    while(st <= dr):
        mij = (st + dr) // 2
        if(l[mij] == x):
            u = mij
            st = mij + 1  
        else:
            if l[mij] < x: 
                st = mij + 1 
            else: 
                dr = dr - 1
    return u
print(ultima_ap([1, 1, 2, 2, 2, 2, 6, 9, 9, 20], 9) - prima_ap([1, 1, 2, 2, 2, 2, 6, 9, 9, 20], 9) + 1)
# Nu judeca 
#%%
def f(a,N,l,c,nr):
    if N == 0 :
        a[l][c]=nr
        return 
    elem=2**N // 2
    #zona 1 
    f(a,N-1,l,c+elem,nr)
    #zona 2
    f(a,N-1,l+elem,c, nr +elem**2)
    #zona 3
    f(a,N-1,l,c,nr + 2 * elem**2)
    #zona 4 
    f(a,N-1,l+elem,c+elem,nr + 3 * elem**2)
    
    
N=3
a=[[0]*2**N for _ in range(2**N)]
f(a,N,0,0,1)
for x in a: 
    for y in x: 
        print(y, end=' ')
    print()
#%%