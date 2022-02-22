class graphImplemantation :
    graph_node = {}

    def graph_create(self,node,neighbour):
        if node not in self.graph_node:
            self.graph_node[node] = [neighbour]
        else:
            self.graph_node[node].append(neighbour)

    def show_graph(self):
        for node in self.graph_node:
            for neighbour in self.graph_node[node]:
                print('(',str(node),' , ',neighbour,')')            

graph = graphImplemantation()

while(1):
    node,*neighbour = map(int,input().split())
    if node == -1:
        graph.show_graph()
        break
    graph.graph_create(node,neighbour)

