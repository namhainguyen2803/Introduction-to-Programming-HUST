def process(filepath):
    lst = []
    with open(filepath, 'r') as f:
        for i in f:
            a = i.split()
            lst.append([a[0], [a[1], a[2]]])
    
    res = {}
    for i in lst:
        if i[0] not in res:
            res[i[0]] = {}
        if i[0] in res:
            if i[1][0] not in res[i[0]]:
                res[i[0]][i[1][0]] = int(i[1][1])
            else:
                res[i[0]][i[1][0]] += int(i[1][1])
    a = list(res.items())
    a.sort()
    res = dict(a)
    for i in res:
        a = list(res[i].items())
        a.sort()
        res[i] = dict(a)
        print(i,":", sep="")
        for j in res[i]:
            print(j, res[i][j])