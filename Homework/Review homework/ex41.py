def sum_and_count(inp):
    sum1 = []
    cnt1 = []
    inp = list(inp)
    for i in range(len(inp)):
        if type(inp[i])==int:
            sum1.append(inp[i])
            cnt1.append(1)
        else:
            sum1.append(sum(list(inp[i])))
            cnt1.append(len(inp[i]))
    return sum1, cnt1
inp = ((1,2,5), (3,7,5,10), (1))
sum_list, cnt_list = sum_and_count(inp)
print(*sum_list)
print(*cnt_list)