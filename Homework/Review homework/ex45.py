text = {}
while True:
    try:
        vote = input().split(' ')
        if vote[0] not in text:
            text[vote[0]] = int(vote[1])
        else:
            text[vote[0]] += int(vote[1])
    except:
        break
lis = []
for k,v in text.items():
    lis.append([k,v])
lis.sort(key=lambda x: x[0])
for i in lis:
    print(i[0], i[1])