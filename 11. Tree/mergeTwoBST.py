class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def inOrder (root, result):

    if root is None:
        return

    inOrder(root.left,result)
    result.append(root.data)
    inOrder(root.right,result)



def mergeSortedArray(arr1, arr2):
    i = 0
    j = 0

    result = []

    while(i < len(arr1) and j < len(arr2)):

        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i+=1
        else:
            result.append(arr2[j])
            j+=1


    while i < len(arr1):
        result.append(arr1[i])
        i+=1

    while j < len(arr2):
        result.append(arr2[j])
        j+=1

    return result


def mergeTwoBST(root1, root2):
    arr1 = []
    arr2 = []


    # BST1 -> 
    inOrder(root1, arr1)

    # BST2 -> 
    inOrder(root2, arr2)

    # mergeSorted
    return mergeSortedArray(arr1, arr2)



# BST1

root1 = Node(3)
root1.left = Node(1)
root1.right = Node(5)

# BST2

root2 = Node(4)
root2.left = Node(2)
root2.right = Node(6)


# merge

result = mergeTwoBST(root1, root2)


print(result)