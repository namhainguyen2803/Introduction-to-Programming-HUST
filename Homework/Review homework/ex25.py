def square_sum(n):
    if n==1:
        return 1
    else:
        dp = [0]*(n+1)
        dp[0]=0
        dp[1]=1
        for i in range(2,n+1):
            dp[i] = dp[i-1] + i**2
        return dp[n]