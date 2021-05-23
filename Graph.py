class Graph:
    grapthTypes = {"DIRECTED":"DIRECTED","UNDIRECTED":"UNDIRECTED"}
    buildTypes  = {"MATRIX":"MATRIX", "LIST":"LIST"}
    buildType   = 'MATRIX'
    graphType   = 'DIRECTED'

    def __init__(self, buildType = 'MATRIX', graphType = 'DIRECTED'):
        self.buildType = buildType
        self.graphType = graphType
        self.vertices  = {}
        self.edges     = []
        self.matrix    = []

                

