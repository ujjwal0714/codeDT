import math

def factorial(x):  # using math module.
    if x<0:
        return(-1)
    else:
        return(math.factorial(x))

def factorial2(x):  # using iterative multiplication.
    if x<0:
        return (-1)
    else:
        num = 1
        p = 1
        while num != x+1:
            p *= num
            num += 1
        return(p)

def factorial3(x):  # calculating factorial using recursive multiplication.
    if x<=0:
        if x==0:
            return 1
        return (-1)
    if x==1:
        return(x)
    else:
        return(x*factorial3(x-1))

def trailingZeros(x):  
    # count trailing zeroes by calculating factorial 
    # and then counting number of zeros.
    factorial = math.factorial(x)
    count=0
    while factorial%10==0:
        count+=1
        factorial//=10
    return(count)

def trailingZeros2(x):  
    # calculate trailing number of zeros of factorial by 
    # counting the pairs of 5 & 2 in the factors of the factorial. 
    # we only calculate the frequency of 5 
    # as 2 occurs enough number of time.
    count5=0
    while x!=1:
        variable=x
        while variable%5==0:
            variable//=5
            count5+=1
        x-=1
    return(count5)

def trailingZeros3(x):
    # formulating trailingzeros2() function. **
    n=1
    count=0
    while 5**n<=x:
        count+=x//(5**n)
        n+=1
    return(count)
