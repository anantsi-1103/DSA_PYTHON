from collections import deque

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None




def zigzag(root):

    # tree is empty then return 
    if root is None:
        return
    
    # queue for level order -> 
    q = deque([root])

    # directional Flag
    leftToRight = True


    while q:
        # number of node at the current level
        levelSize = len(q)

        # store current level node
        currentLevel = []

        for i in range(levelSize):

            node = q.popleft()

            currentLevel.append(node.data)

            # add left child
            if node.left:
                q.append(node.left)

            # add right child
            if node.right:
                q.append(node.right)

            # reverse if needed

        if not leftToRight :
            currentLevel.reverse()
            
        print(currentLevel)
        leftToRight = not leftToRight

        

root = Node(1)


root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.right = Node(7)



zigzag(root)