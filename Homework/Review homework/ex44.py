def change_order(lis):
    for i in range(len(lis)):
        if lis[i][1] < lis[i][0]:
            lis[i] = (lis[i][1],lis[i][0])
    return lis
def common_pairs(lis1,lis2):
    ord_lis1 = change_order(lis1)
    ord_lis2 = change_order(lis2)
    res = []
    for tup in ord_lis1:
        if tup in lis2:
            res.append(tup)
    return len(res)
lis = [(3, 4), (5, 6), (9, 10), (4, 5), (10, 20), (2, 3)]
lis2 = [(5, 4), (3, 4), (6, 5), (9, 11)]
print(common_pairs(lis,lis2))