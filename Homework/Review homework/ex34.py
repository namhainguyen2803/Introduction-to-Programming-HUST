arr = list(map(int, input().split()))
res = []
for i in range(1,len(arr)):
    if arr[i]>arr[i-1]:
        res.append(arr[i])
if len(res)==0:
    print('None')
else:
    for i in res:
        print(i, end=' ')