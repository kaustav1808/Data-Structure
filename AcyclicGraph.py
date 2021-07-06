#User function Template for python3


class AcyclicGraph:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        visited = [0 for x in range(V)]
        for node in range(V):
            if not visited[node]:
                if self.cycleFindingDFS(node,visited,-1,adj): return True
        return False
        
    def cycleFindingDFS(self,v,visited,parent,adj):
	    visited[v] = 1 
	    for node in adj[v]:
	        if (node==v) or (visited[node]==1):
	            return True
	        elif not visited[node]:
	            if self.cycleFindingDFS(node,visited,v,adj):
	                return True
	    visited[v] = 2         
	    return False

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
        
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = AcyclicGraph()
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends