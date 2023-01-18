'''
You are given a text. A word is a sequence of non-blank consecutive characters. Words are separated by one or more spaces or end-of-line characters. For each word from this text, you have to count how many times it has occurred earlier in this text.
input:
one two one tho three
aba aba; aba @?"
three two three
output:
0 0 1 0 0 0 0 1 0 1 1 2
'''
d = {}
lis = []
while True:
    try:
        tmp = input().split(' ')
        for x in tmp:
            if x not in d:
                d[x] = 0
            else:
                d[x] +=1
            lis.append(d[x])
    except:
        break
for i in lis:
  print(i, end=' ')