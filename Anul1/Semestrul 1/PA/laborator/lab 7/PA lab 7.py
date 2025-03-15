l=[]
n=0 
def citire():
    global n
    n=int(input())
    for i in range(n):
        x=int(input())
        l.append(x)

def maxim(s,x, i=0, j=n):
    for poz in range(i,j):
        if x < s[poz]:
            return poz+1
    return -1

citire()
a = maxim(l, 15, 0, len(l))
print("Pozitia este: ",a)