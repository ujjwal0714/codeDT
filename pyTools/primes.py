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

def isPrimeNumber(x):  # myOriginalApproach
    if x<=1:
        return False
    else:
        for i in range(2,x):
            if x%i==0:
                return False
        else:
            return True

def isPrimeNumber2(x):  # modification to make myOriginalApproach better.
    if x<=1:
        return False
    if x%2==0 and x!=2:
        return False
    else:
        for i in range(3,x//2,2):  # leaving all factors of two, hence halving the range.   
            if x%i==0:
                return False
        else:
            return True

def listPrime2(x,y):  # myOriginalApproach
    l=[]
    for i in range(x,y):
        if isPrimeNumber2(i):
    # using isPrimeNumber2 instead of isPrimeNumber reduces time taken upto 3.5x times.
            l.append(i)
    return(l)

def sieveOfEratosthenes(n):
    # return list of primes in range 1 to n+1
    primeList=[]
    prime=[True for i in range(n+1)]
    p=2
    while p**2<=n:
        if (prime[p]==True):
            for i in range(p*2,n+1,p):
                prime[i]=False
        p+=1
    prime[0],prime[1]=False,False
    for p in range(n+1):
        if prime[p]:
            primeList.append(p)
    return(primeList)

    



