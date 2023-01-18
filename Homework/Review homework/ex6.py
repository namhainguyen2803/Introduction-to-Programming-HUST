a = int(input())
b = int(input())
cnt = 0
for i in range(a,b+1):
    if i %2==0:
        cnt += 1
print(cnt)