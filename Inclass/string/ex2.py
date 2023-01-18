def transform_string(str):
    lis = list(str)
    if len(lis)%4==0:
        return str[::-1]
    else:
        new = ''
        for i in range(len(lis)):
            if i%2==1:
                new = new + lis[i]
        return new
print(transform_string('Dai hoc bach khoa ha noi'))
print(transform_string('DHBKHN'))