# Problem
# is power of 2?
# if n is power of 2
# n & n-1 = 0
# not work for n = 0
def isPowerOf2_M1(n):
    if n!=0:
        return (not(n&(n-1)))
    # further simplify
    # return (n!=0) and not (n & n-1)
    # return n and not (n & n-1)
def isPowerOf2(n):
    return (n and not (n & n-1))

# print(isPowerOf2(8))

# Problem
# Swap 2 Nos
def swapNos(a,b):
    a ^= b
    b ^= a
    a ^= b
    return (a,b)

# print(swapNos(2,8))

def allBitsSet(n):
    return ((n+1) & n == 0)
# O(1) , O(1)

# print(allBitsSet(3))

# Problem
# Check Alternating Bits
def doBitsAlternate(n):
    return (allBitsSet(n ^ (n >> 1)))
# O(1) , O(1)

# print(doBitsAlternate(5))


# Problem
# XOR of all subsets of set
# answer is always 0 for more than 1 element set.
# for singular set answer is that single number



# Problem
# count 0s and 1s
# after int to bin
def count01(n,p):
    if p==1:
        return bin(n).count("1")
    if p==0:
        return len(bin(n))-2-count01(n,1)

# Problem
# count 0s and 1s
# in string
def count01Str(n,p):
    if p==1:
        return n.count("1")
    if p==0:
        return n.count("0")

# for i in [0,1,2,3,4,5,6,7,8]:
  #  print(bin(i),count01(i,0),count01(i,1))

# Problem
# in input binary string, check if all digit can be made 0 or 1
# by flipping 2 consecutive bits any number of times.
def problem72647(n):  # argument is binary string
    # observation is that if both number of 0s and 1s is odd.
    # then only it is false
    return not(count01Str(n,0)%2==1 and count01Str(n,1)%2==1)
print(problem72647("01011"))
# O(n) , O(1)

# XOR of numbers from 1 to n

def XOR_1ton_M1(n):
    xor = 0
    for i in range(1,n+1):
        xor = xor ^ i
    return xor
# O(n) , O(1)

def XOR_1ton_M2(n):
    # following logic is general observation.
    if n%4==0:
        return (n)
    if n % 4 == 1:
        return (1)
    if n % 4 == 2:
        return (n+1)
    if n % 4 == 3:
        return (0)
# O(1) , O (1)

# for i in range(1,10):
  #  print(XOR_1ton_M2(i))

# Problem
# Count numbers x so that n + x = n xor x

def problem5621(n):
    for i in range(1,n):
        pass
