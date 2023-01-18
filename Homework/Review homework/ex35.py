N, K = map(int, input().split())
lis = []
res = [1]*N
for i in range(K):
    a,b = map(int, input().split())
    lis.append([a,b])
    for i in range(a,b+1):
        res[i-1] = 0
res_str =''
for i in res:
    if i == 1:
        res_str = res_str + 'I'
    else:
        res_str = res_str + '.'
print(res_str)