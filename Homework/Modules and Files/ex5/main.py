def process(filepath):
    with open(filepath,'r') as f:
       data = f.readlines()
    lis = []
    for i in data:
        new = i.strip().split(' ')
        new[2] = int(new[2])
        lis.append(new)
    # [['Ivanov', 'paper', 10], ['Petrov', 'pens', 5], ['Ivanov', 'marker', 3], ['Ivanov', 'paper', 7], 
    # ['Petrov', 'envelope', 20], ['Ivanov', 'envelope', 5]]
    dic = {}
    for i in lis:
        if i[0] not in dic:
            dic[i[0]] = {i[1]:i[2]}
        else:
            if i[1] not in dic[i[0]]:
                dic[i[0]].update({i[1]:i[2]})
            else:
                dic[i[0]][i[1]] =  i[2] + dic[i[0]][i[1]]
    new_dic = dict(sorted(dic.items(), key = lambda x: x[0]))
    for ke,di in new_dic.items():
        print(f'{ke}:',end='\n')
        di = dict(sorted(di.items(), key = lambda x: x[0]))
        for k,d in di.items():
            print(k,d,end='\n')
    
            
file = 'data1.inp'
process(filepath=file)
# {'Ivanov': {'paper': 17, 'envelope': 5}, 'Petrov': {'pens': 5, 'envelope': 20}}
