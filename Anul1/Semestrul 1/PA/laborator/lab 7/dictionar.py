#1
#a

l = []
n = 0
def citire():
    global n
    n=int(input())
    for i in range(n):
        x=int(input())
        l.append(x)
#citire()
#print(l,n)

#b
def b(s,x,i=0,j=None):
    if j == None:
        j = len(s)
    for n in range(i,j):
        if s[n] > x:
            return s[n]
    return -1

#print(b([10,20,3,4,45,12,32],30,0,4))

#c
sortat = True
citire()
for i in range(len(l)):
    if b(l,l[i],i) != -1:
        sortat = False
if sortat == True:
    print('Da')
else:
    print('NU')
    
#%%
#2

#a
def a(*x):
    nr = ''
    for i in x:
        nr+= max(str(i))
    return nr
print(a(4251,73,8,133))
    
#b
def b(a,b,c):
    if max(str(a)) == '1' and max(str(b)) == '1' and max(str(c)) == '1':
        return True
    return False

print(b(1001,11,100))

print(b(1001,17,100))

#%%

#4

fin=open(r"C:\\Users\Ciprian\OneDrive - unibuc.ro\Desktop\facultate\Anul I sem I\PA\PA lab 7\cinema.in.txt",'r')
lines=fin.readlines()
d={}
for line in lines:
    line = line.strip()
    l=line.split(' % ')
    print(line)
    cinema = l[0]
    film = l[1]
    ore = set(l[2].split())
    if cinema not in d:
        d[cinema]={film:ore}
    else:
        d[cinema][film]=ore
print(d)

#%%
def sterge_ore(d,cinema,film,ore):
    if cinema in d:
        if film in d[cinema]:
            d[cinema][film].difference_update(ore)
            if len(d[cinema][film])==0:
                del d[cinema][film]
                if len(d[cinema])==0:
                    del d[cinema]
                    return []
            return d[cinema].keys()
    return []

sterge_ore(d,'Cinema 1','Elfii cofetari',{'12:30','10:00'})
print(d)
#%%

def cheie(x):
    return x[0],-len(x[2])
def cinema_film(d,*cinematografe,ora_minima,ora_maxima):
    rez=[]
    for cinema in cinematografe:
        if cinema in d:
            for film in d[cinema]:
                ore = []
                for ora in d[cinema][film]:
                    if ora_minima <= ora <= ora_maxima:
                        ore.append(ora)
                    if len(ore)!=0:
                        ore.sort()
                        rez.append((film,cinema,ore))
    rez.sort(key=cheie)
    return rez
            
print(cinema_film(d,"Cinema 1","Cinema 2",ora_minima='14:00',ora_maxima='22:00'))
            
#%% 


            
            
            
            
            
            
            
            
            
            
            
            









fin.close()







































