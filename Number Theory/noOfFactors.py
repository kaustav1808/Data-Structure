import leastPrimeFactor

def getDistinctFactorCount(n):
    leastPrimeFactors = leastPrimeFactor.fastLeastPrimefactor(n)
    factor            = {}

    while n !=1:
        if leastPrimeFactors[n-1] not in factor:
            factor[leastPrimeFactors[n-1]]  = 1
        else:
            factor[leastPrimeFactors[n-1]] += 1

        n //= leastPrimeFactors[n-1]

    return factor 


def noOfFactors(n):
    distinctFactorsNo   = getDistinctFactorCount(n) 
    print(distinctFactorsNo)
    no_of_factors     = 1 

    for i in distinctFactorsNo:
        no_of_factors  *= distinctFactorsNo[i]+1

    return no_of_factors

def sumOfFactors(n):
    distinctFactorsNo   = getDistinctFactorCount(n)
    sum_of_factors      = 1

    for i in distinctFactorsNo:
        sum_of_factors  *= (i**(distinctFactorsNo[i]+1)-1)/(i-1)

    return sum_of_factors    


if __name__ == "__main__":
    inpt = int(input())
    print(noOfFactors(inpt))                  
    print(sumOfFactors(inpt))                  
