
def maxSubArray_bruteForce(num):

    n = len(num)

    # 
    max_sum = float('-inf')


    for i in range(n):
        cs = 0
        for j in range(i ,n):
            cs += num[j]

            max_sum  = max(max_sum , cs)
    return max_sum




def maxSubArray_Kadanes(num):

    max_sum = float('-inf')

    cs = 0

    for n in num:
        cs += n

        if cs > max_sum:
            max_sum = cs

        # reset if negative

        if cs < 0:
           cs = 0

    return max_sum




def maxSubArray_kadanes_Optimal(num):
    max_sum = num[0] # first index = 1  -> 6 -> 8
    cs = num[0] # first index =  1 -> -1 -> 6 -> 5 -> 8

#   1 , -2, 6, -1, 3
    for i in range(1 , len(num)):
    # cs = max(3, 8)
        cs = max(num[i], cs + num[i])
        # maxsum = max(6,8)
        max_sum = max(max_sum , cs)
    return max_sum







num = [1 , -2, 6, -1, 3]
# num = [-2 , -3, 4, -1, -2 , 1, 5, -3]

print(maxSubArray_bruteForce(num))
print(maxSubArray_Kadanes(num))
print(maxSubArray_kadanes_Optimal(num))

