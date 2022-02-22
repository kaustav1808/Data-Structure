def longestPalindrome( s):
    s = getModifiedString(s,'#')
    c = 0
    r = 0
    maxLengthPos = 0
    
    P = [0 for i in range(0,len(s))]
   

    for i in range(0,len(s)):
        mirror = 2*c-i

        if(i<r):
            P[i] = min(P[mirror],r-i)

        left  = i-(P[i]+1)    
        right = i+(P[i]+1)

        while(left>=0 and right<len(s) and(s[left]==s[right])):
            left  -= 1    
            right += 1
            P[i]  += 1

        if i+P[i] > r:
            c = i        
            r = i + P[i]

            if(P[i] > P[maxLengthPos]):
                maxLengthPos = i

    if(maxLengthPos and P[maxLengthPos]):
        s = getModifiedPalindrome(s,maxLengthPos,P[maxLengthPos])
        print(s)


def getModifiedPalindrome(s,pos,length):
    sPalin = ''
    for i in range(pos-length,pos+length+1):
        if(s[i] !='#'):
            sPalin +=s[i]
    return sPalin            


def getModifiedString(s,char):
    sNew = char

    for i in range(0,len(s)):
        sNew += s[i] + '#'

    return sNew

s = input()
longestPalindrome(s)