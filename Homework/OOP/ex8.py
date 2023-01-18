class Matrix():
    def __init__(self, lst):
        self.lst = lst
    def size(self):
        return (len(self.lst), len(self.lst[0]))
        #     (number of rows, number of columns)  
    def __str__(self):
        s = ''
        for row in range(self.size()[0]):
            s += '\t'.join(list(map(str,self.lst[row])))
            if row < self.size()[0] -1:
                s += '\n'
        return s
    def __add__(self,other):
        res = []
        def addwise(x,y):
            return x+y
        if self.size() == other.size():
            for row in range(self.size()[0]):
                res_row = list(map(addwise, self.lst[row], other.lst[row]))
                res.append(res_row)
            return Matrix(res)
        else:
            return 'Cannot sum two matrices that are not in the same size.'
    def __mul__(self,scalar):
        res = []
        def mulwise(x,y):
            return x*y
        for row in range(self.size()[0]):
            res_row = list(map(mulwise, self.lst[row], [scalar]*len(self.lst[row] )))
            res.append(res_row)
        return Matrix(res)
    def __rmul__(self, scalar):
        return self.__mul__(scalar)

m = Matrix([[1, 0], [0, 1]])
print(m)
print(m.size())
m2 = Matrix([[2, 0], [1, 10000]])
print(m2)
print(m+m2)
print(m*5)