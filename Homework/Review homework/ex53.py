def set_union(a,b):
    res = {i for i in a}
    for i in b:
        res.add(i)
    return res

def set_intersection(a,b):
    res = set()
    for i in a:
        if i in b:
            res.add(i)
    return res

