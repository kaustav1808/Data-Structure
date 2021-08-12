__author__ = "Kaustav Bhattacharya"
__credits__ = "Kaustav Bhattacharya"
__maintainer__ = "Kaustav Bhattacharya"
__email__ = "kaustavofficial1808@gmail.com"

class MinHeap:
    data= []
    def __init__(self) -> None:
        self.data = []

    def swap(self,i,j) -> None:
        self.data[i],self.data[j] = (self.data[j],self.data[i])

    def parent(self,i) -> int:
        return (i-1) // 2

   # return the left child node of the current node i's.
    def left(self,i) -> int:
        return 2*i+1

    # return the right child node of the current node i's.
    def right(self,i) -> int:
        return 2*i+2

    # check if the current node i's has any left child node.
    def hasLeft(self,i):
        return 2*i+1 < len(self.data)

    # check if the current node i's has any right child node.
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
        # take the left child as we set up a complete binary tree
        if self.hasLeft(i):
            smallchild = self.left(i)
            # check if the right child is less than the left one, if it is than we take the right 
            # one as the small child for further comparing.
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
        # move down the max value until found a proper position where,
        # the child node will be greater than the current node
        while j != smallChild:
            #swap the value of smallest child with current node
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