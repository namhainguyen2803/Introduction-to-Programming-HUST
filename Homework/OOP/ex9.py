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
    
    
    def transform_to_triangle(self):
        def mul(lis,scalar):
            res = []
            for i in lis:
                res.append(i*scalar)
            return res
        res = self.lst.copy()
        def subtract(x,y):
            return x - y
        for row in range(self.size()[0]):
            for subrow in range(row+1, self.size()[0]):
                fac1 = res[subrow][row]
                fac2 = res[row][row]
                if fac1 != 0:
                    res[subrow] = list(map(subtract, mul(res[row],fac1), mul(res[subrow],fac2)))
                else:
                    continue
        return res
    
    def det(self):
        res = 1
        mat = self.transform_to_triangle()
        for idr in range(len(mat)):
            for idrr in range(len(mat[0])):
                if mat[idr][idrr] != 0:
                    res = res * mat[idr][idrr]
                    break
        return res
    
    def concat(self, vect):
        res = self.lst.copy()
        #row_v = len(vect)
        #assert row_v != len(self.lst), "The vector b should be the same size with A."
        for row in range(len(res)):
            res[row].append(vect[row])
        return res
    
    def solve(self,vec):
        res = [0]*len(vec)
        mat = Matrix(self.concat(vec))
        triangle_mat = mat.transform_to_triangle()
        if triangle_mat[-1].count(0) + 2 != len(triangle_mat[-1]):
            return 'This equation has more than one solutions.'
        else:
            pref_sum = 0
            for row in range(len(triangle_mat)-1,-1,-1):
                i = len(res)-1
                j = 0
                while i - j > row:
                    pref_sum += res[i-j] * triangle_mat[row][-2-j]
                    j += 1
                res[row] = (triangle_mat[row][-1] - pref_sum)/triangle_mat[row][row]
        st = []
        for i in res:
            st.append("{:.2f}".format(i))
        return ' '.join(st)
# m = Matrix([[1,2,3],[2,-1,0],[4,5,-3]])
# print(m.transform_to_triangle())
# print(m.det())
# print(m.solve([1,2,3]))
m = Matrix([[1, 1, 1], [0, 2, 0], [0, 0, 4]])
print(m.solve([1,1,1]))