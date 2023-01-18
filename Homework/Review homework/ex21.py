def hanoi_tower(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        dp = [0]*(n)
        dp[0]=1
        for i in range(1,n):
            dp[i] = 2*dp[i-1]+1
        return dp[n-1]
print(hanoi_tower(int(input())))
'''
if we consider f(n,st,en) is the number of changes for n disks from the 'st'th start spike to the 'en'th end, 
then the recursive formula will be: f(n,st,en) = f(n-1,st,6-st-en) + 1 + f(n-1,6-st-en,en)
'''