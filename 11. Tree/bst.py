
class TreeNode:
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
            return TreeNode(value)

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


    # node , sum , height
    def countNode(self,root):

        if root is None:
            return 0


        return  self.countNode(root.left)+ self.countNode(root.right) + 1
    
    # node , sum , height
    def SumNode(self,root):

        if root is None:
            return 0


        return  self.SumNode(root.left)+ self.SumNode(root.right) + root.data
    # node , sum , height
    def Height(self,root):

        if root is None:
            return 0


        left = self.Height(root.left)
        right = self.Height(root.right)

        return 1 + max(left, right)

    def leafNode(self,root):

        if root is None:
                    return 0

        if self.root.left is None and self.root.right is None:
            return 1


        return self.leafNode(root.left) + self.leafNode(root.right)

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

    def maxNode(self,root):
        if root is None:
            return float("-inf")

        left = self.maxNode(root.left)       
        right = self.maxNode(root.right)       

    def mirrorTree(self,root):
        if root is None:
            return 0

        root.left , root.right = root.right, root.left


        self.mirrorTree(root.left)
        self.mirrorTree(root.right)

    def identicalTree(self,root1, root2):

        if root1 is None and root2 is None:
            return True

        if root1 is None or root2 is None:
            return False

        return (
            root1.data == root2.data
            and self.identicalTree(root1.left , root2.left)
            and self.identicalTree(root1.right , root2.right)
        )

    def diameter(self,root):
        if root is None:
            return 0

        leftheight = self.Height(root.left)
        rightheight = self.Height(root.right)

        currDia = leftheight + rightheight + 1


        leftdia = self.diameter(root.left)
        rightdia = self.diameter(root.right)


        return max(currDia, leftdia, rightdia)
    
    # Mirror, identical, max, diameter, zigzag



tree = BST()


# values = [34,54,66,56,22,88]

# for i in values:
#     tree.root = tree.insert(tree.root, i)

# print(tree.search(tree.root,23))
# print(tree.countNode(tree.root))
# print(tree.SumNode(tree.root))
# print(tree.leafNode(tree.root))


# print(tree.inorder(tree.root))
# tree.mirrorTree(tree.root)
# print(tree.inorder(tree.root))


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("diameter: ", tree.diameter(root))