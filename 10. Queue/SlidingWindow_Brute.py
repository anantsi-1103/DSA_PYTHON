from collections import deque

def slidingWindow(arr, k):

    result = []

    for i in range(len(arr) - k + 1):
        window = arr[i:i+k]

        result.append(max(window))

    return result


def slidingWindowMax(arr,key):

    dq = deque()
    result=[]

    for i in range(len(arr)):

        # remove out the index -> negative 
        # 1 <= -1
        while dq and dq[0] <= i-k:
            dq.popleft()

        # remove the smaller number
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()
        dq.append(i)

        # store -> 
        if i>= k-1:
            result.append(arr[dq[0]])

    return result



arr = [1,3,-1,-3,5,3,6,7]
k = 3

print(slidingWindowMax(arr,k))