n = 5
subsets = []


def generatingSubsets(k):
    if k == n+1:
        print(subsets)
    else:
        subsets.append(k)
        generatingSubsets(k+1)
        subsets.pop()
        generatingSubsets(k+1)


generatingSubsets(1)
