def longest_alternating_subsequences(lis):
    if len(lis)==1:
        return 1
    else:
        dp = [1]*len(lis)
        for i in range(1,len(lis)):
            for j in range(i):
                if lis[i]*lis[j]<0 and abs(lis[i])>abs(lis[j]):
                    dp[i] = max(dp[j] + 1,dp[i])
    return max(dp)
T = int(input())
inp = list(map(int,input().split()))[:T]
print(longest_alternating_subsequences(inp))