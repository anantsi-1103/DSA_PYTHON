def fibo(n):
    if n <= 1:
        return n
    
    return fibo(n-1) + fibo(n-2)


# recursion ->
def fibo_Mem(n, dp={}):
    if n <= 1:
        return n
    
    if n in dp:
        return dp[n]
    

    dp[n] = fibo_Mem(n-1,dp) + fibo_Mem(n-2,dp)
    return dp[n]


# tabulation
def fibo_tab(n):
    dp = [0] * (n+1)

    if n >= 1:
        dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

print(fibo(5))
print(fibo_Mem(5))
print(fibo_tab(5))