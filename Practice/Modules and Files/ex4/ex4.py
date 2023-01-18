import math
import trig
n = int(input())
sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0

for i in range(1,20,2):
    sum1 = sum1 + trig.sin(n+i)
    sum3 = sum3 + math.sin(n+i)

for j in range(2,21,2):
    sum2 = sum2 + trig.cos(n+j)
    sum4 = sum4 + math.cos(n+j)


sum = float(format(sum1+sum2,'.6f'))
res = float(format(sum3+sum4,'.6f'))
print("{:<28} {:<10}".format("Your own implementation:", format(sum,".6f")))
print("{:<28} {:<10}".format("Math module implementation:", format(res,".6f")))
