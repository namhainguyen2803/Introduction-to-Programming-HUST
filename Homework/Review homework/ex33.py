T = int(input())
lis_inp = list(map(int,input().split()))[:T]
x = int(input())
min = abs(x-lis_inp[0])
num = lis_inp[0]
for i in range(len(lis_inp)):
    if min > abs(x-lis_inp[i]):
        min = abs(x-lis_inp[i])
        num = lis_inp[i]
print(num)