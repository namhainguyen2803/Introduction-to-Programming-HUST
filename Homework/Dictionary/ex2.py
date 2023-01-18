'''
You are given a text. Write a program to print all the words in the text, one for each line. Words should be sorted in descending order of their number of occurrences in the text. Those words with the same number of occurrences should be sorted in lexicographic order.
hi
hi
what is your name
my name is bond
james bond
my name is damme
van damme
claude van damme
jean claude van damme
'''
text = []
while True:
    try:
        text.append(input().split(' '))
    except:
        break

def flatten(arr):
  def check_num(arr):
    for i in arr:
      if type(i)==list:
        return False
    return True
  neww=[]
  for j in arr:
    if type(j)==list:
      neww.extend(j)
    else:
      neww.append(j)
  if check_num(neww)==False:
    return flatten(neww)
  else:
    return neww


def check_duplicate(lis):
  new_lis = []
  for element in lis:
    if element not in new_lis:
      new_lis.append(element)
  return new_lis
lis_str = flatten(text)
not_duplicate = check_duplicate(lis_str)
occurence = []
for str in not_duplicate:
  occurence.append(lis_str.count(str))
str_ocr = list(zip(not_duplicate,occurence))
str_ocr.sort(key= lambda x: (-x[1],x[0]))
for str in str_ocr:
  print(str[0])