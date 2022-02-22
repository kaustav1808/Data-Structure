import math


"""
This code running time is 0(n)
"""
def leastPrimefactor(n):
    if not(n%2): return 2
    if n==1: return 1
    if n==3:return 3

    for i in range(3,n+1,2):
        if not(n%i):
            return i


"""
This code running time is 0(nlogn)
"""
def fastLeastPrimefactor(n):
    factors    = [0] *(n+1)
    factors[1] = 1

    for i in range(2,n):
        if factors[i]:
            continue
        else:
            for j in range(i,n+1,i):
                if not(factors[j]): factors[j] = i

    factors.pop(0)            
    return factors       
        


if __name__ == "__main__":
    """
    for 0(nlogn) solution
    """
    inpt = int(input())

    """
    for 0(n^2) solution
    """

    # for i in range(1,inpt+1):
    #     print(leastPrimefactor(i))

    print(fastLeastPrimefactor(inpt))