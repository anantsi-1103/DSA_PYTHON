from collections import deque



class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(8)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.right.right.left = TreeNode(9)
root.right.right.right = TreeNode(10)



# root = TreeNode('A')
# root.left = TreeNode('B')
# root.right = TreeNode('C')
# root.left.left = TreeNode('D')
# root.left.right = TreeNode('E')
# root.right.left = TreeNode('F')


# print(root.data)
# print(root.left.data)

def preOrder(root):
    if root:
        print(root.data, end=" ")
        preOrder(root.left)
        preOrder(root.right)


def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data, end=" ")
        inOrder(root.right)

def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data, end=" ")


def levelOrder(root):

    queue = deque([root])

    while queue:

        node = queue.popleft()

        print(node.data , end=" ")


        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)



print("PreOrder: ")
preOrder(root)
print()
print("Inorder: ")
inOrder(root)
print()
print("PostOrder: ")
postOrder(root)
print()
print("LevelOrder")
levelOrder(root)
print()
