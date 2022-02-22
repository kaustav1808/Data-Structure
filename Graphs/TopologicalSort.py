class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        toporder = []
        visited  = [0]*V

        for i in range(V):
            if not visited[i]:
                toporder = self.dfs(i,visited,toporder,adj)
        toporder.reverse()
        return toporder
    
    def dfs(self,v,visited,toporder,adj):
        visited[v] = 1
        
        for i in adj[v]:
            if not visited[i]:
                toporder = self.dfs(i,visited,toporder,adj)
        visited[v] = 2
        toporder.append(v)
        return toporder
        


#{ 
#  Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
	map=[0]*N
	for i in range(N):
		map[res[i]]=i
	for i in range(N):
		for v in graph[i]:
			if map[i] > map[v]:
				return False
	return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]
        
        for i in range(e):
            u,v=map(int,input().split())
            adj[u].append(v)
            
        ob = Solution()
        
        res = ob.topoSort(N, adj)
        
        if check(adj, N, res):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends