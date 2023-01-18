def consecutive_convert(stri):
    li = list(stri.lower())
    lis = []
    lis.append(li[0])
    for i in range(1,len(li)):
        if li[i] != li[i-1]:
            lis.append(li[i])
    return ''.join(lis)
print(consecutive_convert(input()))
            