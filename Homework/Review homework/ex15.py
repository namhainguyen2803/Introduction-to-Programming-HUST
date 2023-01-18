def rows(n):
    for i in range(1,n+1):
        a = ''
        for j in range(1,i+1):
            a = a + str(j)
        for j in range(i-1,0,-1):
            a = a + str(j)
        print(' '*(n-i)+str(a)+' '*(n-i))
rows(int(input()))