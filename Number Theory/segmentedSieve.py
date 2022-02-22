from math import floor, sqrt

def sievePrimeGenerator(limit,prime):
    mark = [False]*(limit+1)

    for isPrime in range(2,limit+1):
        if not mark[isPrime]:
            prime.append(isPrime)
            for j in range(isPrime,limit+1,isPrime):
                mark[j] = True
    return prime            

def segmentedPrimeGen(low,high):
    primes = sievePrimeGenerator(floor(sqrt(high)),list())
    mark   = [False]*(high-low+1)

    for prime in primes:
        lowLimit = floor(low/prime) * prime
        if lowLimit < low: 
            lowLimit += prime
        if lowLimit ==prime: 
            lowLimit += prime

        for j in range(lowLimit,high+1,prime):
            mark[j-low] = True

    for i in range(low,high+1):
        if not mark[i-low]:
            print(i)
    return True;        

if __name__ == '__main__':
    t = int(input())

    while t :
        low , high = map(int,input().split(' '))
        if low < 2:
            low = 2
        segmentedPrimeGen(low,high)
        t -= 1