import math

__author__ = "Kaustav Bhattacharya"
__credits__ = "Kaustav Bhattacharya"
__maintainer__ = "Kaustav Bhattacharya"
__email__ = "kaustavofficial1808@gmail.com"


class Graph:
    graphType = None  # "DIRECTED", "UNDIRECTED"
    vertices = {}
    matrix = []
    visited = []
    root = None

    def __init__(self, graphType='DIRECTED'):
        if graphType not in ["DIRECTED", "UNDIRECTED"]:
            raise Exception(
                "the graphType args should be either `DIRECTED` or `UNDIRECTED`")
        self.graphType = graphType
        self.vertices = {}
        self.matrix = []
        self.visited = {}
        self.root = None

    def addEdge(self, source, destination, cost=1):
        if (not source) or (not destination):
            raise Exception("need source and destination to add the edges.")

        if cost <= 0:
            raise Exception("cost must be greater than equal to 0")

        self.addEdgeInLiSt(source, destination, cost)

    def addEdgeInLiSt(self, source, sink, cost):
        if source not in self.vertices:
            self.vertices[source] = {}
        if sink not in self.vertices:
            self.vertices[sink] = {}

        if sink not in self.vertices[source]:
            self.vertices[source][sink] = cost

        if (self.graphType == 'UNDIRECTED') and (source not in self.vertices[sink]):
            self.vertices[sink][source] = cost

    def showList(self):
        for node in self.vertices.items():
            print("node ({node}) -> ".format(node=node[0]))
            for adjacentNode, cost in node[1].items():
                print(" node ({node}), cost({cost})".format(
                    node=adjacentNode, cost=cost))

    def addEdgeInMatrix(self, source, sink, cost):
        pass

    def bfsTraversal(self, s, d, recreate=True):
        if s not in self.vertices or d not in self.vertices:
            raise Exception(
                "node {s} or {d} not in the graph".format(s=s, d=d))
        if recreate:
            self.visited = {}
            self.root = s
            for node in self.vertices:
                self.visited[node] = {"distance": -
                    1, "status": 0, "parent": None}
            self.visited[s] = {"distance": 0, "status": 0, "parent": None}
            queue = []
            queue.append(s)
            while len(queue):
                v = queue.pop(0)
                for node in self.vertices[v]:
                    if not self.visited[node]["status"]:
                        self.visited[node]["status"] = 1
                        self.visited[node]["distance"] = self.visited[v]["distance"] + 1
                        self.visited[node]["parent"] = v
                        queue.append(node)
                self.visited[v]["status"] = 2

        if s != self.root:
            raise Exception("the root vertices is not same.")
        self.pathFromSource(s, d)

    def dfsTraversal(self):
        self.visited = {}
        for node in self.vertices:
            self.visited[node] = {"distance": -1, "status": 0, "parent": None}

        for node in self.vertices:
            if not self.visited[node]["status"]:
                self.dfsVisit(node)

    def dfsVisit(self, u):
        self.visited[u]["status"] = 1
        print("{node}".format(node=u), end="->")
        for each in self.vertices[u]:
            if not self.visited[each]["status"]:
                self.visited[each]["parent"] = u
                self.dfsVisit(each)
        self.visited["status"] = 2
    
    def isCycle(self):
        self.visited = {}
        for node in self.vertices:
            self.visited[node] = 0
        for node in self.vertices:
            if not self.visited[node]:
                if self.cycleFindingDFS(node, -1): return True
        return False
    
    def cycleFindingDFS(self,v,parent):
        self.visited[v] = 1
        for node in self.vertices[v]:
	        if parent == node:
	            continue
	        if (node == v) or (self.visited[node] == 1):
	            return True
	        else:
	            if self.cycleFindingDFS(node, v):
	                return True
        self.visited[v] = 2
        return False

    def pathFromSource(self,s,v):
        if s==v:
            print("{v} ".format(v=v),end=".")
            print("\n")
        elif not v:
            print("No parent found",end=".")
        else:
            print("{v} ".format(v=v),end="-> ")
            self.pathFromSource(s,self.visited[v]["parent"])
                                     
    def dijkstraAlgorithm(self,s):
        d = {}
        u = {}
        p = {} 
        for i in self.vertices:
            d[i] = math.inf
            u[i] = False
            p[i] = -1
        d[s] = 0
        for node in self.vertices:
            v = -1 
            for j in self.vertices:
                if not u[j] and (v==-1 or (d[j] < d[v])):
                    v = j

            if math.isinf(d[v]):
                break;   

            u[v]  = True
            for each in self.vertices[v]:
                if d[each] > self.vertices[v][each]+d[v]:
                    d[each] =  self.vertices[v][each]+d[v]
                    p[each] = v
        print(d)            






def main():
    graph = Graph()
    graph.addEdge("a","b")
    graph.addEdge("a","c")
    graph.addEdge("a","d")
    graph.addEdge("b","c")
    graph.addEdge("b","d")
    graph.addEdge("d","a")
    graph.showList()
           
    if graph.isCycle():
        print("Graph is cyclic")
    else:
        print("Graph is acyclic")       
    print("\n\n")
    graph.dijkstraAlgorithm("a")
    print("\n\n")

    graph2 = Graph("UNDIRECTED")
    graph2.addEdge("a","b",2)
    graph2.addEdge("a","c",3)
    graph2.addEdge("a","d",5)
    graph2.addEdge("b","c",7)
    graph2.addEdge("b","d",2)
    graph2.addEdge("d","a",13)
    graph2.showList()

    graph.bfsTraversal("a","d")
    graph.bfsTraversal("a","c",False)
    graph.bfsTraversal("b","d")

    graph2.dfsTraversal()
    print("\n\n")

    graph2.dijkstraAlgorithm("a")
    print("\n\n")

    if graph2.isCycle():
        print("Graph is cyclic")
    else:
        print("Graph is acyclic")

    graph3 = Graph("DIRECTED")
    graph3.addEdge("a","b")     
    graph3.addEdge("b","c")     
    graph3.addEdge("c","d")     
    if graph3.isCycle():
        print("Graph is cyclic")
    else:
        print("Graph is acyclic")

    print("\n\n")

    graph3.dijkstraAlgorithm("a")
    print("\n\n")    

if __name__ == "__main__":
    main()
