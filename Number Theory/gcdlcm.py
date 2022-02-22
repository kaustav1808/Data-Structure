#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def gcd(a,b):
    while(b>0):
        temp = b
        b = a%b
        a = temp
    return a

def lcm(a,b):
    if(a>b): 
        return (a*b)/gcd(a,b) 
    else: 
        return (a*b)/gcd(b,a)

def getTotalX(a, b):
    leastLcm = a[0]
    leastGcd = b[0]
    total = 0

    for i in range(len(a)-2):
        leastLcm = lcm(leastLcm,a[i+1])
  
    for i in range(len(b)-2):
        leastGcd = gcd(leastGcd,b[i+1])

    for i in range(int(leastGcd/leastLcm)):
        if (leastLcm * (i+1)) <= leastGcd:
            if not(leastGcd % leastLcm):
                total +=1
        else:
            break        
    return total;            


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
