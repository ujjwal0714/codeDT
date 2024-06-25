# factors

def listFactors(m):  # returns list of all factors
    l=[]
    for i in range(1,m+1):
        if m%i == 0:
            l.append(i)
    return(l)

def listPerfectFactors(m):  # returns list of all perfect factors
    l=[]
    for i in range(1,m):
        if m%i == 0:
            l.append(i)
    return(l)

def isPerfect(i):
    return(sum(listPerfectFactors(i)) == i)

def isTriPerfect(i):
    return(sum(listFactors(i)) == 3*i)
    # return(sum(listPerfectFactors(i)) == 2*i)

def isQuadPerfect(i):
    return(sum(listPerfectFactors(i)) == 4*i)
    # return(sum(listPerfectFactors(i)) == 3*i)

    

    



