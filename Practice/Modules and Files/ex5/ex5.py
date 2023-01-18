with open('test.inp') as f:
    re = f.readlines()
    dic = {}
    for i in range(len(re)):
        line = re[i]
        lis = line.split(' ')
        for word in lis:
            dic[word] = dic.get(word,0) + 1
res = ''
with open('test.out', 'w') as f:
    f.write(str(dic))
with open('test.out', 'r') as f:
	all = f.read()
	print(all)
f.close()