class MinHeap:
    data= []
    def __init__(self) -> None:
        self.data = []

    def swap(self,i,j) -> None:
        self.data[i],self.data[j] = (self.data[j],self.data[i])

    def parent(self,i) -> int:
        return (i-1) // 2

    def left(self,i) -> int:
        return 2*i+1

    def right(self,i) -> int:
        return 2*i+2

    def hasLeft(self,i):
        return 2*i+1 < len(self.data)

    def hasRight(self,i):
        return 2*i+2 < len(self.data)        

    def insert(self,num) -> None:
        self.data.append(num)
        j = len(self.data) - 1 
        while j>0 and self.data[self.parent(j)] > self.data[j]:
            self.swap(j,self.parent(j))
            j = self.parent(j)

    def min(self) -> int:
        return self.data[0]

    def smallChild(self,i):
        if self.hasLeft(i):
            smallchild = self.left(i)
            if self.hasRight(i) and self.data[self.left(i)] > self.data[self.right(i)]:
                smallchild = self.right(i)
            if self.data[smallchild] < self.data[i]:return smallchild
            else: return i 
        else:return i


    def removeMin(self) -> int:
        if not len(self.data):
            raise Exception("Heap are empty cannot remove an element.")

        self.swap(0,len(self.data)-1)
        min = self.data.pop()
        j = 0
        smallChild = self.smallChild(j)
        while j != smallChild:
            self.swap(j,self.smallChild(j))
            j = smallChild
            smallChild = self.smallChild(j)
        return min;

def main():
    minHeap = MinHeap()
    minHeap.insert(50)    
    minHeap.insert(20)    
    minHeap.insert(90)    
    minHeap.insert(19)    
    minHeap.insert(31)    
    minHeap.insert(32)    
    minHeap.insert(30)    
    minHeap.insert(42)    
    minHeap.insert(48)

    try:
        print("min element from min heap {a}.".format(a=minHeap.removeMin()))  
        print("min element from min heap {a}.".format(a=minHeap.removeMin()))    
        print("min element from min heap {a}.".format(a=minHeap.removeMin())) 
        print("min element from min heap {a}.".format(a=minHeap.removeMin()))  
        print("min element from min heap {a}.".format(a=minHeap.removeMin()))
        print("min element from min heap {a}.".format(a=minHeap.removeMin()))
        print("min element from min heap {a}.".format(a=minHeap.removeMin())) 
        print("min element from min heap {a}.".format(a=minHeap.removeMin())) 
        print("min element from min heap {a}.".format(a=minHeap.removeMin())) 
        print("min element from min heap {a}.".format(a=minHeap.removeMin())) 
        print("min element from min heap {a}.".format(a=minHeap.removeMin())) 
    except Exception as err:
        print (err)       

if __name__ == "__main__":
    main()                                            