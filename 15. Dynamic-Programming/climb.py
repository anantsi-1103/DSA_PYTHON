def climb(n):
    if n == 0 or n == 1:
        return 1
    
    return climb(n-1) + climb(n-2)



#  n - 0
def climb_dp(n,dp):
    # 0 or 1
    if n == 0 or n ==1 :
        return 1
    

    # aagr us n ki value dp m already define hai toh us n ko aap wohi dp return krdoge 
    if(dp[n] != -1):
        return dp[n]
    

    # n-1 dp n-2 dp
    # dp[3] = 2  + 1
    dp[n] = climb_dp(n-1,dp) + climb_dp(n-2,dp)
    return dp[n]


#  0 --  n
def climb_tab(n):
    dp = [0] * (n + 1)

    dp[0]=1
    dp[1]=1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

# print(climb(5))

n = 5

# dp = [-1] * (n+1)

# print(climb_dp(n,dp))

print(climb_tab(5))

