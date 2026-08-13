class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def kthLevel(root,k):

    # tree is empty
    if root is None:
        return


    if k == 0:
        print(root.data, end = " ")
        return


    # go the next level\
    kthLevel(root.left,k-1)
    kthLevel(root.right,k-1)



root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(7)

root.right.left = Node(4)
root.right.right = Node(5)


kthLevel(root,2)