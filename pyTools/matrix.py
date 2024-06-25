a = [[0,1,2],
     [10,11,3]]

b = [[3,4,2],
     [2,1,3]]

def matOp(op,a=0,b=0):
    if op == "itr":
        for i in a:
            for j in i:
                print(j)
    elif op == "#multiply":
        m1 = len(a)
        n1 = len(a[0])
        m2 = len(b)
        n2 = len(b[0])
        for i in range(m1):
            for j in range(n1):
                print(a[i][j]*b[j][i])
    return
    

matOp("#multiply",a,b)
