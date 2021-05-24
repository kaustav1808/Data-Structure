__author__ = "Kaustav Bhattacharya"
__credits__ = "Kaustav Bhattacharya"
__maintainer__ = "Kaustav Bhattacharya"
__email__ = "kaustavofficial1808@gmail.com"


class Graph:
    graphType   = None # "DIRECTED", "UNDIRECTED"
    vertices    = {}
    matrix      = []

    def __init__(self,graphType = 'DIRECTED'):
        if graphType not in ["DIRECTED", "UNDIRECTED"]:
            raise Exception("the graphType args should be either `DIRECTED` or `UNDIRECTED`")
        self.graphType = graphType
        self.vertices  = {}
        self.matrix    = []

    def addEdge(self,source,destination,cost=1):
        if (not source) or (not destination):
            raise Exception("need source and destination to add the edges.")

        if cost <=0:
            raise Exception("cost must be greater than equal to 0")

        self.addEdgeInLiSt(source,destination,cost)    
                

    def addEdgeInLiSt(self,source,sink,cost):
        if source not in self.vertices:
            self.vertices[source] = {}
        if sink not in self.vertices:
            self.vertices[sink]   = {}

        if sink not in self.vertices[source]:
            self.vertices[source][sink] = cost 

        if (self.graphType == 'UNDIRECTED') and (source not in self.vertices[sink]):
            self.vertices[sink][source] = cost

    def showList(self):
        for node in self.vertices.items():
            print("node ({node}) -> ".format(node=node[0]))
            for adjacentNode, cost in node[1].items():
                print(" node ({node}), cost({cost})".format(node=adjacentNode,cost=cost))

    def addEdgeInMatrix(self,source,sink,cost):
        pass


def main():
    graph = Graph()
    graph.addEdge("a","b")
    graph.addEdge("a","c")
    graph.addEdge("a","d")
    graph.addEdge("b","c")
    graph.addEdge("b","d")
    graph.addEdge("d","a")
    graph.showList()
           
    print("\n\n")

    graph2 = Graph("UNDIRECTED")
    graph2.addEdge("a","b",2)
    graph2.addEdge("a","c",3)
    graph2.addEdge("a","d",5)
    graph2.addEdge("b","c",7)
    graph2.addEdge("b","d",2)
    graph2.addEdge("d","a",13)
    graph2.showList()

if __name__ == "__main__":
    main()
