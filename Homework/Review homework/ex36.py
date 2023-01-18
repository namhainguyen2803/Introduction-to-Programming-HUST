for i in range(int(input())):
    lis = []
    for i in range(8):
        x, y = map(int, input().split())
        lis.append([x,y])
    print(lis)
    def checkmate(X,Y):
        x0 = X[0]
        x1 = X[1]
        y0 = Y[0]
        y1 = Y[1]
        if x0==y0 or x1==y1:
            return True
        elif x0+x1 == y0+y1:
            return True
        elif y0-x0==y1-x1:
            return True
        return False
    cnt = 0
    for i in range(len(lis)-1):
        for j in range(i+1,len(lis)):
            if checkmate(lis[i],lis[j])==True:
                cnt += 1
                
    if cnt ==0:
        print('NO')
    else:
        print('YES')