def check_prime(n):
    if n==1:
        return False
    elif n==2:
        return True
    else:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        return True

def find_prime(n):
    lis = []
    for i in range(1,n+1):
        if check_prime(i)==True:
            lis.append(i)
    return lis

def check_sum_prime(n):
    lis = find_prime(n)
    for i in lis:
        a = n - i
        if a in lis:
            return True
    return False

T = int(input())
for i in range(T):
    a = int(input())
    if check_sum_prime(a) == False:
        print('NO')
    else:
        print('YES')