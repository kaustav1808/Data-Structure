def dfsTravarsal(u):
    queue = []
    queue.append(u)

    while len(queue):
        node = queue.pop(0)
        visited[node] = True
        for key in g[node]:
            if not(visited[key]):
                visited[key] = True
                queue.append(key)
    return True        

def connectedComponent():
    component = 0

    for key in range(1,n+1):
        if not(visited[key]):
            component +=1
            dfsTravarsal(key)
    return component

n,m,k = map(int,input().split(' '))
g = dict((key,[]) for key in range(1,n+1))
visited = {key:False for key in range(1,n+1)} 

for _ in range(m):
    u,v = map(int,input().split(' '))
    g[u].append(v)
    g[v].append(u)
cmpt = connectedComponent()

if(cmpt>k):
    print(-1)
else:
    print(m-n+k)