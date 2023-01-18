def sort_tuple(tup):
    def hello(n):
        return (n[1])
    tup.sort(key=hello,reverse=True)
    return tup
tup = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
print(sort_tuple(tup))