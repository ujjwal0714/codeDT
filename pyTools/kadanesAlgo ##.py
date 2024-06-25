# Kadane's Algo
# Max Sum Contiguous Subarray of Array

def Kadane(l,k = 0):
    # pass list as argument
    # k = 0 by default
    # k = 1 is passed when all array passed is all negative.
    if k == 0:
        currentSum = 0
        maxSum = 0
        for i in l:
            currentSum += i
            if maxSum < currentSum:
                maxSum = currentSum
            if currentSum < 0:
                currentSum = 0
        return (maxSum)
    elif k == 1:
        for i in l:
            return(max(l))

l = [-2, -3, 4, 1, 2, -1, -5, 1,2,40]
l = [-2,1,-3,4,-1,2,1,-5,4]
print(Kadane(l,0))

# Procedure
# 2 variables: cSum , mSum set to 0.
# array is iterated and iter is added to cSum.
# if mSum become < cSum, mSum = cSum is largest some till that iteration
# if cSum get < 0, cSum set to 0.
    

