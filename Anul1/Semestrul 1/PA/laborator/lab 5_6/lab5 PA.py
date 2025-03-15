#%%
fin = open(r'C:\Users\Ciprian\Desktop\PA\PA lab 5\test.in.txt','r')
fout = open(r'C:\Users\Ciprian\Desktop\PA\PA lab 5\test.out.txt', 'w')
nota = 1 
lines = fin.readlines()
for line in lines:
    line = line.strip()
    calcul, rez = line.split('=')
    var1, var2 = calcul.split('*')
    var1 = int(var1) 
    var2 = int(var2)
    if var1 * var2 == int(rez):
        fout.write(line + ' corect\n')  
        nota += 1 
    else: 
        fout.write(line + ' gresit\n')
print(nota)
fin.close()
fout.close()
#%%
n, m = [int(x) for x in input().split()]
a = []
for i in range(n):
    l = [int(x) for x in input().split()]
    a.append(l)
print(a)
#%%
# Pr 8 
n, m = [int(x) for x in input().split()]
a = [[int(x) for x in input().split()] for _ in range(n)]

l = [x for l in a for x in l if x % 2 == 0]
print(len(l))
#%%
# Pr 9 
n, m = [int(x) for x in input().split()]
a = [[int(x) for x in input().split()] for _ in range(n)]
print(a[0])
        