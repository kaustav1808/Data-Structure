t = int(input())

def getLongestSubsequence(lcs_matrix,str1,str2,x,y):
    revseq = ""

    while (x>0) and (y>0):
        if str1[x-1] != str2[y-1]:
            if lcs_matrix[x-1][y] == lcs_matrix[x][y]: x -= 1
            elif lcs_matrix[x][y-1] == lcs_matrix[x][y]: y -= 1
        else:
            revseq += str1[x-1]
            x -= 1
            y -= 1
    return revseq[::-1]


while t:
    x, y = map(int, input().split(" "))
    first = input()
    second = input()
    t -= 1
    lcs = [[0] * (y + 1) for _ in range(x + 1)]

    for i in range(x + 1):
        for j in range(y + 1):
            if (not i) or (not j):
                None
            elif first[i - 1] == second[j - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
            else:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])
    print("Longets Common SubSequence length: ",lcs[x][y])
    print("Longets Common SubSequence: ",getLongestSubsequence(lcs,first,second,x,y))