def count_words(filepath):
    with open(filepath,'r') as f:
        data = f.read()
    new = data.split()
    return len(new)
file = 'data1.inp'
print(count_words(filepath=file))