def diamond(n):
    for i in range(1,n+1):
        print(' '*(n-i)+ '*'*(2*i-1)+ ' '*(n-i))
    for i in range(n-1,0,-1):
        print(' '*(n-i)+ '*'*(2*i-1)+ ' '*(n-i))
    return None
n = int(input())
diamond(n)