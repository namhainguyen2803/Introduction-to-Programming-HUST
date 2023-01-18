def binary(n):
    if n ==1:
        return 2
    elif n==2:
        return 3
    elif n==3:
        return 5
    else:
        return 2*binary(n-1) - binary(n-3)

# 1     0
# 11 10     01 00
#111 110    101 100     