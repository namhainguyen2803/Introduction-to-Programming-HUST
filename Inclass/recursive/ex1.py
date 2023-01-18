def gd(a,b):
    if a%b==0:
        return b
    else:
        return gd(b,a%b)