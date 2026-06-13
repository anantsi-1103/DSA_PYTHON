
def knapsnack(index,capacity, wt, val):
    if index == 0 or capacity == 0:
        return 0
    
    if(wt[index-1] <= capacity):
        # include
        # take

        take = val[index-1] + knapsnack(index-1,capacity-wt[index-1],wt,val)
        # skip
        skip =  knapsnack(index-1,capacity,wt,val)

        return max(take,skip)
    

    # exlude
    return knapsnack(index-1,capacity,wt,val)

def knapsnack_DP(index,capacity, wt, val, dp):
    if index == 0 or capacity == 0:
        return 0
    
    if(dp[index][capacity] != -1):
        return dp[index][capacity]
    
    if wt[index-1] <= capacity:
        # include
        take = val[index-1] + knapsnack_DP(index-1,capacity-wt[index-1],wt,val,dp)
        # skip
        skip = knapsnack_DP(index-1,capacity,wt,val,dp)

        dp[index][capacity] = max(take,skip)
    # exlude
    else:
        dp[index][capacity] = knapsnack_DP(index-1,capacity,wt,val,dp)

    return dp[index][capacity]

def knapsnack_Tab(wt,val,capacity):

    n = len(wt)

    dp = [[0] * (capacity+1) for _ in range(n+1) ]


    for i in range(1, n+1):

        for w in range(1,capacity+1):
            if wt[i-1]  <= w:
                # include
                # dp[2][1] = 3
                dp[i][w] = max(
                    # take
                    # val[1] + dp[1][2-1]
                val[i-1] + dp[i-1][w-wt[i-1]],
                # skip
                # dp[1][2-1]
                dp[i-1][w]
                )

            else:
                # exlude
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]


wt = [1,3,4,5]
val = [1,4,5,7]

capacity = 7

print(knapsnack_Tab(wt,val,capacity))

# n = len(wt)

# dp = [[-1] * (capacity + 1) for _ in range(n+1)]

# print(knapsnack_DP(n, capacity,wt,val,dp))