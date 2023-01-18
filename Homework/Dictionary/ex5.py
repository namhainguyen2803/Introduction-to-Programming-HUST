'''
You are given a sequence of integers. A subsequence is a sequence of elements obtained by removing some elements (or removing nothing) from the original one. An alternating subsequence is a subsequence, whose values change sign, i.e. every two successive elements in the subsequence must have opposite signs. 
Your task is to find the longest alternating subsequence with elements whose absolute values are strictly increasing.
Input:
The first line contains the number of elements N (1 ≤ N ≤ 1000).
The second line contains N elements of the sequence separated by spaces.
Output: 
Print out the length of the longest alternating subsequence.
Hints:
In the example below, one of the longest alternating subsequences is 17 -20 23 -32 38 -40
input:
16
17 -20 -21 11 39 23 -24 5 3 -32 38 22 -14 -40 9 32
output:
6
'''

n = int(input())
a = list(map(int,input().split()))
b = [0 for _ in range(n)]
# b[i] : độ dài dãy con lớn nhất kết thúc ở i
b[0] = 1 
for i in range(1,n):
    for j in range(i):
        if a[i] * a[j] < 0 and abs(a[j]) < abs(a[i]): 
            # với mỗi i, ta xác định độ dài dãy con dài nhất trước đó có thể nhận thêm a[i] vào 
            b[i] = max(b[i], b[j] + 1)
    if b[i] == 0:
        b[i] = 1 
ans = 1 
for i in range(n):
    ans = max(ans, b[i])
print(ans)