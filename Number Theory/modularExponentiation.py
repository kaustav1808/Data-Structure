def fastExponentiation(base,exponent):
    res = 1
    while exponent:
        if(exponent%2):
            res = res * base
        exponent //= 2
        base *= base
        print("-----")
    return res        

if __name__ == '__main__':
    base, exponent = map(int,input().split(" "))
    print(fastExponentiation(base,exponent))