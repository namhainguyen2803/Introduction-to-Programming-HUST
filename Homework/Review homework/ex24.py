#sol 1:
def power(a,b):
    if b==0:
        return 1
    elif b==1:
        return a
    else:
        dp = [0]*(b+1)
        dp[0]=1
        dp[1]=a
        for i in range(2,b+1):
            dp[i] = dp[i-1]*a
        return dp[b]
print(power(5,4))
#sol 2:
power = lambda x,y: x**y