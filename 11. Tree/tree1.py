class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)



# traversal -> 
def inorder(root):

    if root:
        inorder(root.left) # left 
        print(root.data, end=" ") # root
        inorder(root.right) # right 

def preOrder(root):

    if root:
        print(root.data, end=" ") # root
        preOrder(root.left) # left 
        preOrder(root.right) # right 

def postOrder(root):

    if root:
        postOrder(root.left) # left 
        postOrder(root.right) # right 
        print(root.data, end=" ") # root



print("Inorder Traversal : ", inorder(root))
print("PreOrder Traversal : ", preOrder(root))
print("PostOrder Traversal : ", postOrder(root))
        


