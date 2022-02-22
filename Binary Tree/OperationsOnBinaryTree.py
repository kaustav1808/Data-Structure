from BinaryTree import BinaryTree

def createBinaryTree():
    print("enter the root node")
    tree = BinaryTree(int(input()))
    tree.createTree()
    tree.showBinaryTree()

def createBTreeFromPREINR(pre,inr,pl,ph,il,ih):
    if (pl>ph) or (il>ih):return None
    
    node = pre[pl]
    i=il
    
    while i<=ih:
        if (inr[i]== node):break
        i += 1
    node = BinaryTree(node)
    nel  = i - il 
    node.left = createBTreeFromPREINR(inr,pre,pl+1,pl+nel,il,i-1)    
    node.right = createBTreeFromPREINR(inr,pre,pl+nel+1,ph,i+1,ih)   
    return node 
    


def createBinaryTreeFromInorderPreorderString():
    print("enter the preorder string")
    pre = input()
    print("enter the inorder string")
    inr = input()

    root = createBTreeFromPREINR(pre,inr,0,len(pre)-1,0,len(inr)-1)
    root.showBinaryTree()

print("create a binary tree Y/N")
status = input()
if status == 'Y':
    createBinaryTree()

print("create a binary tree from inorder and preorder string Y/N")
status = input()
if status == 'Y':
    createBinaryTreeFromInorderPreorderString()   


