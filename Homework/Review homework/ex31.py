def transform_string(st):
    n = len(st)
    if n%4==0:
        return st[::-1]
    else:
        return st[1::2]