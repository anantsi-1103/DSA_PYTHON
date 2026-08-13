from collections import deque


class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def top_view(root):

    if root is None:
        return


    # Queue Contains (node, horizontal_distance)
    q = deque()
    q.append((root,0))

    # HD -> node Value
    top = {}

    while q:

        node, hd = q.popleft()

        # Store only the first node at this hd
        if hd not in top:
            top[hd] = node.data

        # left child -> hd - 1
        if node.left:
            q.append((node.left, hd - 1))


        # right child -> hd + 1
        if node.right:
            q.append((node.right, hd + 1))



    # print from the smallest hd to largest hd
    for hd in sorted(top):
        print(top[hd], end = " ")



root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.right.left = Node(4)
root.right.right = Node(5)


top_view(root)
