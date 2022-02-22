n = int(input())
permutations = list()
chosen = [False for _ in range(n+1)]


def search():
    if len(permutations) == n:
        print(permutations)
    else:
        for i in range(1, n+1):
            if chosen[i]:
                continue
            else:
                chosen[i] = True
                permutations.append(i)
                search()
                chosen[i] = False
                permutations.pop()


search()
