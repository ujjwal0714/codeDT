def arrSwap(arr,i,j):
    # in arr, swap elements at i , j th positions
    c = arr[i]
    arr[i] = arr[j]
    arr[j] = c
    return (arr)

def arrSwap2(arr,i,j):
    # in arr, swap elements at i , j th positions
    arr[i] , arr[j] = arr[j] , arr[i]
    return (arr)

def selectionSort(l):
    for i in range(0,len(l)):
        for j in range(i+1,len(l)):
            if l[i] > l[j]:
                arrSwap(l,i,j)
           # print(i,j)
        print(l)
    return(l)

l = [2,8,5,3,9,4,1]

print(selectionSort(l))

# [a , b ,c ,d]
# we will compare every element after a with a
# if < a, then swap them
# move to b, compare subsequent items.



    
        
