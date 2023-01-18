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
m = Matrix([[1, 0], [0, 1]])
print(m)
print(m.size())
m = Matrix([[2, 0, 0], [0, 1, 10000]])
print(m)
print(m.size())
m = Matrix([[-10, 20, 50, 2443], [-5235, 12, 4324, 4234]])
print(m)
print(m.size())