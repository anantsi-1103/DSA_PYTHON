from binarytree import Node

root = Node(10)
root.left = Node(20)
root.right = Node(40)

print(root)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)



inorder(root)