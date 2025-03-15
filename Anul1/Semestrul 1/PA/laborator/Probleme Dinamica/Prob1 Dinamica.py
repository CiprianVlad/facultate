l = [1, -2, 3, -1, 5, 2, -6, 1, 3]

def pb1_1(l):
    s = l[0]
    smax = l[0]
    start = 0
    end = 0 
    temp_start = 0 
    
    for i in range (1, len(l)):
        if s + l[i] > l[i]:
            s = s + l[i]
        else:
            s = l[i]
            temp_start = i
        if s > smax: 
            smax = s 
            start = temp_start
            end = i 
    return l[start:end+1]
#%%
def pb1_2(l):
    d = [0] * len(l)
    d[0] = l[0]
    start = 0
    end = 0 
    temp_start = 0 
    for i in range (1, len(l)):
        if d[i - 1] + l[i] > l[i]: 
            d[i] = d[i-1] + l[i]
        else: 
            d[i]=l[i]
            temp_start = i 
        if d[end] < d[i]: 
            start = temp_start 
            end = i 
    return l[start:end+1] 
print(pb1_2(l))
#%%
a = [[2, 1, 4],
     [1, 3, 2], 
     [1, 6, 1]]
n,m=len(a), len(a[0])
d = [[0] * m for _ in range(n)]
d[0][0] = a[0][0]

for j in range(1,m):
    d[0][j] = a[0][j] + d[0][j-1]
for i in range(1, n): 
    d[i][0] = a[i][0] + d[i -1][0]
for i in range(1, n): 
    for j in range(1, m): 
        d[i][j] = a[i][j] + max(d[i][j -1], d[i -1][j])
path = []
i, j = n-1, m-1
while i > 0 & j > 0: 
    path.append((i+1, j+1))
    if d[i-1][j] > d[i][j-1]: 
        i = i - 1 
    else: 
        j = j - 1
while i > 0: 
    path.append((i+1,1))
    i = i - 1 
while j > 0: 
    path.append((1, j+1))
    j = j - 1 
path.append((1,1))
path.reverse()
print(path) 
#%%
cuvinte = ["masa", "carte", "sac", "teatru", "tema", "rustic", "sare"]
d = {cuv:(1,[cuv]) for cuv in cuvinte}
for i in range(len(cuvinte) - 1, -1, -1):
    for j in range(len(cuvinte) - 1, i, -1):
        if cuvinte[i][-2:]==cuvinte[j][:2]: 
            if d[cuvinte[i]][0] < d[cuvinte[j]][0] + 1: 
                d[cuvinte[i]] = (d[cuvinte[j]][0] + 1,[cuvinte[i]]+d[cuvinte[j]][1])
print(d)