#%%
from math import sqrt
def f(x):
    s=0
    while x!=0:
        s+=x%10
        x=x//10
    return s
v = [10, 22, 11, 15, 9, 16, 17, 6, 4]
v.sort()
x=sorted(v,key=f)
print(x)
#%%
# Sortare dupa prima cifra si in caz de egal cresc
# Sortare dupa primalitate (intai prime apoi neprime)
# Sortare dupa numarul de cifre si in caz de egal descrescator
# Dupa divizibilitatea cu 3 (intai  cele nedivizibilitate apoi divizibile)

# Sortare dupa prima cifra 

def f(x):
    while x>9:
        x=x//10
    return x
v = [10, 22, 11, 15, 9, 16, 17, 6, 4]
v.sort()
x=sorted(v,key=f)
print(x)
#%%
def f(x):
    k = 0
    while x != 0:
        k += 1
        x//=10
    return k
v = [10, 22, 11, 15, 9, 16, 17, 6, 4, 102, 131, 306]
v.sort(reverse=True)
x=sorted(v,key=f)
print(x)
#%%

#%%
# Sortate dupa primalitate
def f(x):
    for d in range(2,x):
        if x % d == 0:
            return 1
    else: 
        return 0
v = [10, 7, 11, 15, 9, 16, 17, 6, 4]
v.sort()
x=sorted(v,key=f)
print(x) 
#%%
fin=open(r"C:\\Users\Ciprian\OneDrive - unibuc.ro\Desktop\facultate\Anul I sem I\PA\PA lab 5\eleve.in.txt",'r')
lines=fin.readlines()
d={}
for line in lines:
    line=line.strip()
    line_split=line.split()
    d[line_split[0]]={
        'nume':line_split[1],
        'prenume':line_split[2],
        'note':[int(x) for x in line_split[3:]]        
        }

x = '2501910000034'
if x in d:
    d[x]['note'][0] += 1
    print(d[x])
else:
    print('None')
fin.close()
#%%
fin=open('C:/Users/Ciprian/Desktop/PA/PA lab 5/eleve.in.txt','r')
lines=fin.readlines()
d={}
for line in lines:
    line=line.strip()
    line_split=line.split()
    d[line_split[0]]={
        'nume':line_split[1],
        'prenume':line_split[2],
        'note':[int(x) for x in line_split[3:]]        
        }
l_note=[10,8]
x = '2501910000034'
if x in d:
    d[x]['note'] += l_note
    print(d[x])
else:
    print('None')
fin.close()
#%%
"""
fin=open('C:/Users/Ciprian/Desktop/PA/PA lab 5/eleve.in.txt','r')
lines=fin.readlines()
d={}
for line in lines:
    line=line.strip()
    line_split=line.split()
    d[line_split[0]]={
        'nume':line_split[1],
        'prenume':line_split[2],
        'note':[int(x) for x in line_split[3:]]        
        }
l_note=[10,8]
x = '2501910000034'
if x in d:
    del d[x]
else:
    print('None')
print(d)
fin.close()
"""
#%%
fin=open('C:/Users/Ciprian/Desktop/PA/PA lab 5/eleve.in.txt','r')
lines=fin.readlines()
d={}
for line in lines:
    line=line.strip()
    line_split=line.split()
    d[line_split[0]]={
        'nume':line_split[1],
        'prenume':line_split[2],
        'note':[int(x) for x in line_split[3:]]        
        }
lista_elevi=[]
for x in d: 
    l=[]
    l.append(d[x]['nume'])
    l.append(d[x]['prenume'])
    l.append(d[x]['note'])
    lista_elevi.append(l)
print(lista_elevi)
def fm(x):
    return sum(x[2])/len(x[2])
def fn(x):
    return x[0]
lista_elevi=sorted(lista_elevi,key=fn)
lista_elevi=sorted(lista_elevi,key=fm,reverse=True)
print(lista_elevi)
#%% 
import string 
import random
for i in d:
    litere = string.ascii_letters
    cifre=string.digits
    
    litere3=random.choices(litere, k=3)
    cifre3=random.choices(cifre, k=3)
    
    litere3.extend(cifre3)
    x=''.join(litere3)
    d[i]['cod']=x
print(d)
#%%
# Pr 6 !!!