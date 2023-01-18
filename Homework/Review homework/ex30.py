def combi(n,k):
    if n==0:
        return 1
    elif n==1:
        return n
    else:
        dp = [1]*(n+1)
        for i in range(1,n+1):
            dp[i] = dp[i-1]*i
    return dp[n]/(dp[n-k]*dp[k])
def substrings_count(st):
    lis = list(st)
    n = len(lis)
    di = {}
    for i in range(n):
        if lis[i] not in di:
            di[lis[i]] = 1
        else:
            di[lis[i]] = di[lis[i]] +1
    li = [a for a in di.values() if a!=1]
    res = n
    for i in li:
        res = res + combi(i,2)
    return round(res)
st ='toi la sinh vien bach khoa ha noi'
print(substrings_count(st))