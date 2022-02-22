import random

def checkIsPrime(n,k):
    if n<2: return False
    if n <=3: return True
    if not (n%2): return False

    s = 0
    d = n-1

    while not (d%2):
        s += 1
        d //=2
    
    while k:
        k -= 1
        a  = random.randint(2,n-2) 
        x  = (a**d)%n
        if x == 1: continue

        for _ in range(s):
            if x==(n-1): break
            x = (x ** 2) % n
        else: return False
    return True  

for i in range(1,100):
    if(checkIsPrime(i,5)):
        print(i," ")          
