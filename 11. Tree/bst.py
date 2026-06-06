class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.root = None


    # insert
    def insert(self,root,value):

        if root is None:
            return Node(value)
        
        if value < root.data:
            root.left = self.insert(root.left, value)

        else:
            root.right = self.insert(root.right, value)

        return root
    

    # search
    def search(self,root,key):

         if root is None:
             return "Not Found"
         
         if root.data == key:
             return "Found"
         
         if key < root.data:
             return self.search(root.left, key)

         else:
             return self.search(root.right, key)
             

    # count nodes
    def countNodes(self,root):

          if root is None:
             return 0
          
          return self.countNodes(root.left) + self.countNodes(root.right) + 1

      # count nodes
    def sumNode(self,root):

          if root is None:
             return 0
          
          return root.data +  self.sumNode(root.left) + self.sumNode(root.right)


    def height(self,root):

        if root is None:
             return 0
        
        left = self.height(root.left)
        right = self.height(root.right)

        return 1 + max(left,right)

    def countLeaf(self,root):
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            return 1
        
        return self.countLeaf(root.left) + self.countLeaf(root.right)

    def mirrorTree(self,root):
        if root is None:
             return 0
        
        root.left,root.right = root.right , root.left

        self.mirrorTree(root.left)
        self.mirrorTree(root.right)


    def identicalTree(self,root1,root2):

        if root1 is None and root2 is None:
            return True
        
        if root1 is None or root2 is None:
            return False
        
        return (
            root1.data == root2.data 
            and self.identicalTree(root1.left, root2.left)
            and self.identicalTree(root1.right, root2.right)
        )

    def maxNode(self,root):

        if root is None:
             return float("-inf")
        
        left = self.maxNode(root.left)
        right = self.maxNode(root.right)

        return max(root.data,left,right)

    def diameter(self,root):
        if root is None:
             return 0
        
        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)

        currDia = leftHeight + rightHeight + 1

        leftdia = self.diameter(root.left)
        rightdia = self.diameter(root.left)

        return max(currDia , leftdia , rightdia)








    def inorder(self,root):
        if root:
            self.inorder(root.left) # left 
            print(root.data, end=" ") # root
            self.inorder(root.right) # right 

    def preOrder(self,root):
        if root:
         print(root.data, end=" ") # root
         self.preOrder(root.left) # left 
         self.preOrder(root.right) # right 

    def postOrder(self,root):
        if root:
            self.postOrder(root.left) # left 
            self.postOrder(root.right) # right 
            print(root.data, end=" ") # root
            


tree = BST()

# values = [34,54,66,56,22,88]

# for i in values:
#     tree.root = tree.insert(tree.root, i)


# print("Search 22:", tree.search(tree.root,22))

# print("Total Nodes:", tree.countNodes(tree.root))

# tree.inorder(tree.root)
# print()
# tree.postOrder(tree.root)
# print()
# tree.preOrder(tree.root)
# print()

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Diameter : ", tree.diameter(root))