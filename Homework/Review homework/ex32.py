def to_uppercase(st):
    lis = list(st)
    cnt = 0
    for i in range(4):
        if lis[i].isupper()==True:
            cnt +=1
    if cnt <2:
        return st
    else:
        return st.upper()