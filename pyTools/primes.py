def isPrime2(x):
    if x > 1: # not 0 or 1 or < 0
        for i in range(2,x):
            if x%i==0:
                return(0)
        return(1)
    return(0)

# check every number from 2 to x-1 if it divides x.

def isPrime3(x):
    if x > 1: # not 0 or 1 or < 0
        for i in range(2,(x//2)+1):
            if x%i==0:
                return(0)
        return(1)
    return(0)

# check every number from 2 to (x-1)/2 if it divides x.
# Aux = O(1)
# t = O(n)

def isPrime(x):
    if x > 1: # not 0 or 1 or < 0
        for i in range(2,int(x**0.5)+1):
            if x%i==0:
                return(0)
        return(1)
    return(0)

# https://www.desmos.com/calculator/oa9sczylsv
# Aux = O(1)
# t = O(sqrt(n))

def isPrimeRecursive(x,m): # recursive
    if m==1:
        return(1)
    if x%m==0:
        return(0)
    if isPrimeRec(x,m-1)==0:
        return (0)
    return(1)

# Aux = O(sqrt(n))
# t = O(sqrt(n))

def listPrime(a,b):
    l = []
    for i in range(a,b):
        if isPrime4(i):
            l.append(i)
    return (l)

print(listPrime(10,100))

##for a in range(1,100):
##    if (isPrimeRecursive(a,int(a**0.5)+1)):
##        print(a)
        

    



