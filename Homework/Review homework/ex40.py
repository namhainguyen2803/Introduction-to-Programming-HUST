def closest_tuple(tuple_list, query, k):
    num = query[k-1]
    lis = []
    for tup in tuple_list:
        a = 0
        for i in tup:
            a = a + abs(i-num)
        lis.append([tup,a])
    lis.sort(key=lambda x: x[1])
    return lis[0][0]
tuple_list = [(-3, 4, 9), (5, 6, 7), (10, 16, 70), (1, 6, -7)]
query = (1, 2, 5)
k = 3
print(closest_tuple(tuple_list, query, k))