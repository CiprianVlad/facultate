#%%
pers = input().split()
n = len(pers) 
x=[0]*(n+1)

def afis():
    for i in range(1, n+1): 
        print(f"{pers[i-1]}-{pers[x[i]-1]}", end=" ")
    print()
def ok(k): 
    for i in range(1,k):
        if x[k]==x[i]:
            return False
    if x[k]==k: 
        return False    
    return True
def solutie(k):
    return k==n 
def back(k):
    for i in range(1, n+1): 
        x[k]=i
        if ok(k):
            if solutie(k):
                afis()
            else: 
                back(k+1)
back(1)
#%%
x=[0] * (n + 1)

def afis():
    for i in range(1, p+1): 
        print(x[i], end=" ")
    print()
def ok(k): 
    for i in range(1,k):
        if x[k]==x[i]:
            return False
    if k > 1: 
        if x[k] < x[k-1]: 
            return False    
    return True
def solutie(k):
    return k==n 
def back(k):
    for i in range(1, n+1): 
        x[k]=i
        if ok(k):
            if solutie(k):
                afis()
            else: 
                back(k+1)
for p in range(1, n+1, 2):            
    x=[0] * (n + 1)
    back(1)
#%%
b=int(input())
multimi=[]
for _ in range(n): 
    multime = [int(x) for x in input().split()]
    multimi.append(multime)
x=[0] * n 
def afis(): 
    for i in range(n):
        print(multimi[i][x[i]], end= " ")
    print()  
    
def solutie(k): 
    return k== n-1 
def back(k): 
    for i in range(len(multimi[k])):
        x[k] = i 
        if solutie(k):
            afis()
        else:
            back(k+1)
back(0)
#%% 
multime=[int(x) for x in input().split()]
n = len(multime)
p = 2
M = 5 
def afis():
    for i in range(1, p+1): 
        print(multime[x[i]-1], end=" ")
    print()
def ok(k): 
    for i in range(1,k):
        if x[k]==x[i]:
            return False
    if k > 1: 
        if x[k] < x[k-1]: 
            return False    
    return True
def suma(): 
    s = 0
    for i in range(1,p+1):
        s = s + multime[x[i] - 1]
    return s 
def solutie(k):
    return k==n 
def back(k):
    for i in range(1, n+1): 
        x[k]=i
        if ok(k):
            if solutie(k):
                    afis()
            else: 
                back(k+1)
for p in range(1, n+1, 2):            
    x=[0] * (n + 1)
    back(1)