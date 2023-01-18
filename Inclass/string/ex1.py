def last_repeat(s):
    lis = list(s)
    lis = lis[::-1]
    len_s = len(lis)
    for i in range(len_s):
        if lis[i] != ' ':
            for j in range(i+1,len_s):
                if lis[i]==lis[j]:
                    return lis[i]
    return None

print(last_repeat('BKHN'))
print(last_repeat('Dai hoc bach khoa ha noi'))