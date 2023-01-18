def digit_sum_greater(a,b):
    sum_a = sum(map(int,list(str(a))))
    sum_b = sum(map(int,list(str(b))))
    if sum_a>sum_b:
        return 'YES'
    return 'NO'
print(digit_sum_greater(int(input()),int(input())))