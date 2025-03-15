def numar_cifre(x, k):
    if x<10:
        return k+1
    else:
        return(numar_cifre(x//10,k+1))



def invers(x, i):
    if i > 0:
        i -= 1
        k = x % 10
        x = x//10 
        return(invers(x, i))
    print (k)