class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None




def transformtoSum(root):

    # empty tree
    if root is None:
        return 0

    # Save Original Value
    oldValue = root.data

    # get sum of left subtree
    leftsum = transformtoSum(root.left)


    # get sum of right subtree
    rightSum = transformtoSum(root.right)

    # Current Node ->
    root.data = leftsum + rightSum



    return oldValue + leftsum + rightSum


root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.right.left = Node(4)
root.right.right = Node(5)

print(transformtoSum(root))

