l=[]
global n
n=0 
def citire():
    n=int(input())
    for i in range(n):
        x=int(input())
        l.append(x)

def maxim(s,x, i=0, j=n):
    for poz in range(i,j):
        if x <= s[poz]:
            if (poz+1) == 1: 
                print("DA")
            else:
                print("NU")

citire()
x = max(l)
maxim(l, x,0,len(l))

