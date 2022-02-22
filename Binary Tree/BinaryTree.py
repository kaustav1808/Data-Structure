class BinaryTree:
    def __init__(self,val) -> None:
        self.left  = None
        self.right = None
        self.val = val
        print("New node ceated with value {val}".format(val=val))

    def createTree(self):
        node = self
        direction = None
        while(direction !='n'):
            print("Enter l(left) or r(right) or n(no) for no node")
            direction = input()
            if direction != 'n':
                print("enter a number to insert in {dir}".format(dir=direction))
                val = int(input())
                if (direction=='l') and not (node.left):
                    node.left=BinaryTree(val)
                    node.left.createTree()
                elif (direction=='r') and not (node.right):
                    node.right=BinaryTree(val)
                    node.right.createTree()
                else: return node    
        return node           

    def showBinaryTree(self):
        if not self.val: return None
       
        strng = ""
        if not self.left: strng += "."
        else: strng += "=>"+str(self.left.val)
        strng += "| "+str(self.val)+" |"
        if not self.right: strng += "."
        else: strng += "<="+str(self.right.val)
        print(strng)
        if self.left: self.left.showBinaryTree()
        if self.right: self.right.showBinaryTree()                 



if __name__ == '__main__':
    tree = BinaryTree(100)
    tree.createTree()
    tree.showBinaryTree()
