#%%
fin=open("C:\\Users\Ciprian\OneDrive-unibuc.ro\Desktop\PA\PA lab 9_10\matrice.in.txt",'r')
fout=open("matrice.out",'w')
lines=fin.readlines()
m=[[int(x) for x in line.strip().split()] for line in lines]
for line in m: 
    line.remove(max(line))
    line.remove(max(line))
for line in m: 
    for x in line: 
        fout.write(str(x) + " ")
    fout.write("\n")
fin.close()
fout.close()
#%%
fin=open("C:\\Users\Ciprian\OneDrive - unibuc.ro\Desktop\PA\PA lab 9_10\exemplu.in.txt", 'r')
lines=fin.readlines()
d={}
for line in lines: 
    line=line.strip()
    cuvinte=line.lower().split()
    for cuvant in cuvinte:
        if cuvant not in d: 
            d[cuvant]=1
        else:
            d[cuvant]+=1
df={}
for cuv, frecv in d.items():
    if frecv not in df:
        df[frecv] = [cuv]
    else: 
        df[frecv].append(cuv)
chei_frecv=sorted(df.keys(), reverse=True)
for frecv in chei_frecv: 
    cuvinte =sorted(df[frecv])
    print(f"Frecventa {frecv}: {','.join(cuvinte)}")
fin.close    
#%% 
filme=[("Interstelar",9.0, 2014, 'sf'),
       ("The notebook",9.0,2006,'romantic'),
       ("Pianistul",8.8,2002,'drama'),
       ("Wall-E",8.5,2010,'sf')]
sortare1=sorted(filme, key=lambda x:(x[1], x[0]), reverse=True)
# print(sortare1)
sortare2=sorted(filme, key=lambda x:(x[3], -x[1]), reverse=True)
print(sortare2)
#%%
fin=open("C:\\Users\Ciprian\OneDrive - unibuc.ro\Desktop\PA\PA lab 9_10\studenti.txt", 'r')
lines=fin.readlines()
d={}
for line in lines: 
    # line=line.strip()
    # date = line.lower().split()
    for date in line: 
        if date not in d: 
            d[date]=1
        else: 
            d[date]+=1
print(d)
    