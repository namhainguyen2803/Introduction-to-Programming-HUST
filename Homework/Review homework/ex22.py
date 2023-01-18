#lis_inp = list(map(int,input().split()))
mid = lambda a,b,c: a if a in range(min(b,c),max(b,c)+1) else b if b in range(min(a,c),max(a,c)+1) else c
print(mid(5,5,4))