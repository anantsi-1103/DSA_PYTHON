
def trap(height):
    n = len(height)

    water = 0

    for i in range(n):

        leftMax = 0
        rightMax = 0

        # find left max -> current -> left check
        for j in range(i, -1,-1):
            leftMax = max(leftMax, height[j])


        # find Right max -> current -> right
        for j in range(i, n):
            rightMax = max(rightMax, height[j])

        water += min(leftMax,rightMax) - height[i]

    return water



height = [4,2,0,6,3,2,5]
print(trap(height))

