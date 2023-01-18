def count_words(file_path):
    with open(file_path,'r') as f:
        data = f.readlines()
        lis = list(map(lambda x: x.strip(' \n'),data))
    di2={}
    for line in lis:
        line = line.split(' ')
        for i in line:
            i = i.strip(' "')
            if i != '':
                if i not in di2:
                    di2[i] = 1
                else:
                    di2[i] = di2[i] + 1
                    
    print(sum(di2.values()))