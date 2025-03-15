#%%
# Pr 9 
n, m = [int(x) for x in input().split()]
a = [[int(x) for x in input().split()] for _ in range(n)]
l = [sum(line) - max(line) for line in a]
print(l)
#%%
# Pr 10 
n, m = [int(x) for x in input().split()]
a = [[int(x) for x in input().split()] for _ in range(n)]
for i in range(len(a)):
    if i % 2 ==0: 
        print(a[i])
    else: 
        print(a[i][::-1])
#%% 
# Pr 5 
n, m = [int(x) for x in input().split()]
a = [[int(x) for x in input().split()] for _ in range(n)]
for i in range(len(a)):
    p = [prod for l in a for x in l prod *= x]