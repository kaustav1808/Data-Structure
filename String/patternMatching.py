"""
Matching pattern from a string
"""

def patternMatching(sourceString,patternString):
    pattern_cur  = 0
    cur = 0
    source_index = -1

    while cur <= len(sourceString)-1:
        if(sourceString[cur]==patternString[pattern_cur]):
            source_index = cur
            while(sourceString[cur]==patternString[pattern_cur]) and (pattern_cur<len(patternString)-1) and (cur<len(sourceString)-1):
                cur +=1
                pattern_cur +=1
            if pattern_cur == len(patternString)-1:
                return source_index
            else:
                source_index = -1
        else:
            pattern_cur = 0
        cur +=1   
    return source_index;     

"""
 Delete pattern from string
"""

def deletePattern(sourceString,patternString):
    pattern_cur  = 0
    cur = 0
    actualString = []
    subString = []

    while cur <= len(sourceString)-1:
        if(sourceString[cur]==patternString[pattern_cur]):
            while (pattern_cur<len(patternString)) and (cur<len(sourceString)) and (sourceString[cur]==patternString[pattern_cur]) :
                subString.append(sourceString[cur])
                cur +=1
                pattern_cur +=1
            if pattern_cur == len(patternString):
                subString = []
                pattern_cur = 0
            else:
                actualString += subString
                pattern_cur = 0
        else:
            actualString.append(sourceString[cur])
            pattern_cur = 0
            cur +=1   
    return actualString; 


sourceString  = str(input())
patternString = str(input())

firstIndex = patternMatching(sourceString,patternString)


if(firstIndex>=0):
    print("first index is "+str(firstIndex))
else:
    print("No pattern found")    

print("deleted pattern "+str(deletePattern(sourceString,patternString)))    
    

