class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def validateBst(root):

    def check(node,min,max):

        if node is None:
            return True

        if node.data <= min or node.data >= max:
            return False


        # check left subtree
        leftValid = check(
            node.left, min, node.data
        )
        # check right subtree
        rightValid = check(
            node.right, node.data, max
        )

        return leftValid and rightValid

    return check(root, float('-inf'), float('inf'))



root = Node(10)

root.left = Node(12)
root.right = Node(15)

root.left.left = Node(2)
root.left.right = Node(7)

root.right.left = Node(12)
root.right.right = Node(20)


print(validateBst(root))