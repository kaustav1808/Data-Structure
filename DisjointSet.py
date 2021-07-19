class DisjointSet:
    def __init__(self,element) -> None:
        self.element = element
        self.sets = [i for i in range(self.element)]
        self.size = [1 for _ in range(self.element)]

    def root(self,element):
        while element != self.sets[element]:
            element = self.sets[element]
        return element    

    def union(self,a,b):
        root_a = self.root(a)
        root_b = self.root(b)
        self.sets[root_a] = root_b

    def weightedUnion(self,a,b):
        root_a = self.root(a)    
        root_b = self.root(b)
        if (self.size[root_a] < self.size[root_b]):
            self.sets[root_a] = root_b    
            self.size[root_a] += self.size[root_b]
        else:
            self.sets[root_b] = root_a    
            self.size[root_b] += self.size[root_a]


    def find(self,a,b):
        return self.root(a)==self.root(b) 

if __name__== '__main__':
    dsjSet = DisjointSet(10)
    dsjSet.union(0,1)           
    dsjSet.union(1,2)           
    dsjSet.union(3,4)           
    dsjSet.union(1,4)           
    dsjSet.union(5,7)


    print("find {a} and {b} is {c}".format(a=1,b=4,c=dsjSet.find(1,4)))           
    print("find {a} and {b} is {c}".format(a=0,b=4,c=dsjSet.find(0,4)))           
    print("find {a} and {b} is {c}".format(a=6,b=4,c=dsjSet.find(6,4)))

    dsjSet2 = DisjointSet(10)
    dsjSet2.weightedUnion(0,1)           
    dsjSet2.weightedUnion(1,2)           
    dsjSet2.weightedUnion(3,4)           
    dsjSet2.weightedUnion(1,4)           
    dsjSet2.weightedUnion(5,7)


    print("find {a} and {b} is {c}".format(a=1,b=4,c=dsjSet2.find(1,4)))           
    print("find {a} and {b} is {c}".format(a=0,b=4,c=dsjSet2.find(0,4)))           
    print("find {a} and {b} is {c}".format(a=6,b=4,c=dsjSet2.find(6,4)))           


