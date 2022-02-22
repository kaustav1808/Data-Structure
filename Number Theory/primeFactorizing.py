import math
import leastPrimeFactor


"""
Running time is 0(sqrt(n))
"""
def factorization(n):
    factors = []

    while not(n%2):
        factors.append(2)
        n //=2

    for i in range(3,math.floor(math.sqrt(n))+1,2):
        while not(n%i):
            factors.append(i)
            n /=i

    if n>2:
        factors.append(int(n))        

    return factors

"""
running time of this algorithm is 0(logn), with pre-computation and space complexity of 0(logn) 
"""

def fastFactorization(n):
    """
    there is a pre computation which have running time of 0(nlogn)
    """
    leastPrimefactors = leastPrimeFactor.fastLeastPrimefactor(n)
    factors = []

    """
    this code is running as 0(log)
    """
    while n != 1:
        factors.append(leastPrimefactors[n-1])
        n //= leastPrimefactors[n-1]
    return factors    



if __name__ == "__main__":
    inpt = map(int,input().split(" "))

    for i in inpt:
        #print(factorization(i))
        print(fastFactorization(i))