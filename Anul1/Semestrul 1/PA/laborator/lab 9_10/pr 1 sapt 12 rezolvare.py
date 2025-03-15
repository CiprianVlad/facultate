#%%
fin=open("C:\\Users\Ciprian\OneDrive - unibuc.ro\Desktop\PA\PA lab 9_10\matrice.in.txt",'r')
fout=open("C:\\Users\Ciprian\OneDrive - unibuc.ro\Desktop\PA\PA lab 9_10\matrice.out.txt",'w')
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