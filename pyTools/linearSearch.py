def linearSearch(l,key):
    for i in range(len(l)):
        if l[i]==key:
            return i
    return (-1)

def linearSearchRecursive(l,x,key):
    if x==-1:
        return (-1)
    if l[x]==key:
        return (x)
    return linearSearchRecursive(l,x-1,key)

# t = O(n)
# aux = O(1)
    
##print(linearSearchRecursive([1,2,3],2,20))

def binarySearch(l,key):
    # implemented in sorted array
    mid = len(l)//2
    if l[mid]==key:
        return(mid)
    if key>mid:
        print(l[mid+1:])
        return(binarySearch(l[mid+1:],key))
    if key<mid:
        print(l[:mid])
        return(binarySearch(l[:mid],key))

print(binarySearch([0,1,2,3,4,5,6,7,8,9],4))

    
        
