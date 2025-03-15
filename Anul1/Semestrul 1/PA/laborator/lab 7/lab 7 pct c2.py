# ceva sigur crapa
l=[]
global n
global x
n=0 
def citire():
    n=int(input())
    for i in range(n):
        x=input()
        l.append(x)
# x e cea mai mare litera cu care incepe un cuvant
def maxim(s,x, i=0, j=n):
    for poz in range(i,j):
        if x < max(s[poz]):
            x = s[poz][0]
        if x <= s[poz][0]: # cea mai mare litera e prima litera
            if (poz+1) == 1: 
                return print("DA")
    return print("NU")

citire()
maxim(l, 'a',0,len(l))
