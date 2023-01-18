def remove_duplicates(lst):
    di1 = {}
    di2 = {}
    for i in range(len(lst)):
        if lst[i] not in di1:
            di1[lst[i]] = 1
            di2[lst[i]] = i
        else:
            di1[lst[i]] = di1[lst[i]] + 1
    lis = []
    for k in di1:
        if di1[k]==1:
            lis.append(k)
        else:
            del di2[k]
    def hello(n):
        return di2[n]
    lis.sort(key=hello,reverse=False)
    return lis
print(remove_duplicates([4, 3, 5, 2, 5, 1, 3, 5]))