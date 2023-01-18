def process(filepath) :
    with open(filepath, 'r') as f:
        data = f.readlines()
    lis_data = list(map(lambda x: x.strip().split(' '),data))
    dic1 = {}
    for line in lis_data:
        if line[0] not in dic1:
            dic1[line[0]] = {line[1]:int(line[2])}
        else:
            if line[1] not in dic1[line[0]].keys():
                dic1[line[0]].update({line[1]:int(line[2])})
            else:
                dic1[line[0]][line[1]] += int(line[2])
    lis = list(dic1)
    lis.sort()
    for name in lis:
        print(f'{name}:', end='\n')
        di = list(dic1[name])
        di.sort()
        for thing in di:
            print(thing, dic1[name][thing], end='\n')
process('data1.inp')