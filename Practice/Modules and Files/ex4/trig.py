import math
PI=math.pi
def exp(x):
	res=0
	y=0
	while (x**y/math.factorial(y))>1.0e-9:
		res+=x**y/math.factorial(y)
		y+=1	
	return float(format(res,'.6f'))
	
def sin(x):
	res=0
	y=0
	while abs((((-1)**y)*(x**(2*y+1))/math.factorial(2*y+1)))>1.0e-9:
		res+=((-1)**y)*(x**(2*y+1))/math.factorial(2*y+1)
		y+=1
	return float(format(res,'.6f'))

def cos(x):
	res=0
	y=0
	while abs((((-1)**y)*(x**(2*y))/math.factorial(2*y)))>1.0e-9:
		res+=((-1)**y)*(x**(2*y))/math.factorial(2*y)
		y+=1
	return float(format(res,'.6f'))			

'''
import math   
def sin(x):
    n = 0
    sum = 0
    while True:
        a = (((-1)**n) * (x**(2*n+1)))/math.factorial(2*n+1)
        sum = sum + a
        if abs(sum/math.sin(n))<10**(-9):
            break
        n = n + 1
    return round(sum,6)

def cos(x):
    n = 0
    sum = 0
    while True:
        a = (((-1)**n) * (x**(2*n)))/math.factorial(2*n)
        sum = sum + a
        if abs(sum/math.cos(n))<10**(-9):
            break
        n = n + 1
    return round(sum,6)

def exp(x):
    n = 0
    sum = 0
    while True:
        a = (x**n)/math.factorial(n)
        sum = sum + a
        if abs(summath.exp(n))<10**(-9):
            break
        n = n + 1
    return round(sum,6)'''