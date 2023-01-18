'''
In the family tree, each person, except for the ancestor, has exactly one parent. Each element of the tree is associated with a non-negative integer called the height. The ancestor has a height of 0, any other element has a height that is greater more 1 than its parent. Given a family tree, your task is to determine the height of all its elements.
Input: 
The first line contains the number of elements in the family tree N. 
N-1 next lines specify the parent for each element of the tree, except for the ancestor. Each line has the form descendant_name parent_name.

Output:
The program should list all the elements of the tree in lexicographic order. After printing the name of each element, it should print its height, respectively.
input:
9
Alexei Peter_I
Anna Peter_I
Elizabeth Peter_I
Peter_II Alexei
Peter_III Anna
Paul_I Peter_III
Alexander_I Paul_I
Nicholaus_I Paul_I
output:
Alexander_I 4
Alexei 1
Anna 1
Elizabeth 1
Nicholaus_I 4
Paul_I 3
Peter_I 0
Peter_II 2
Peter_III 2

'''
N = int(input())
text = []
n=0
while n<N:
  try:
    text.append(input().split(' '))
    n = n + 1
  except:
    break
      
#ancestor_lis = list(map(lambda x: x[1],text))
#descendant_lis = list(map(lambda x: x[0],text))

def check_dup(lis):
  new_lis = []
  for dup in lis:
    if dup not in new_lis:
      new_lis.append(dup)
  return new_lis
  
#ancestor_dup = check_dup(ancestor_lis)
#descendant_dup = check_dup(descendant_lis)

def check_ancestor(ancestor, descendant):
  tree_lis = []
  for a in ancestor:
    if a not in descendant:
      tree_lis.append(a)
  return tree_lis

def remove_value(dic,value):
  new_di=[]
  for di in dic:
    if di[1] != value:
      new_di.append(di)
  return new_di
def remove_dup(lis):
  new_lis = []
  for li in lis:
    if li not in new_lis:
      new_lis.append(li)
  return new_lis

#ancestor = check_dup(ancestor_lis)
#descendant = check_dup(descendant_lis)
new_dic = []
stt = 0
while len(text)>0:
  ancestor_lis = list(map(lambda x: x[1],text))
  descendant_lis = list(map(lambda x: x[0],text))
  ancestor = check_dup(ancestor_lis)
  descendant = check_dup(descendant_lis)
  for ances in check_ancestor(ancestor, descendant):
    new_dic.append([ances,stt])
    for i in range(len(text)):
      if text[i][1]==ances:
        new_dic.append([text[i][0],stt+1])
    text = remove_value(text,ances)
  stt = stt + 1

fin = remove_dup(new_dic)
fin.sort(key=lambda x: x[0])
for fi in fin:
  print(fi[0] + ' '+ str(fi[1]))

  


'''
def tree_lis(text,treelis=[]):
  if len(text)>1:
    ancestor_lis = list(map(lambda x: x[1],text))
    descendant_lis = list(map(lambda x: x[0],text))
    ancestor = check_dup(ancestor_lis)
    descendant = check_dup(descendant_lis)
    lis = check_ancestor(ancestor, descendant)
    treelis.append(lis)
    for ances in check_ancestor(ancestor, descendant):
      text = remove_value(text,ances)
    return tree_lis(text,treelis)
  else:
    return treelis
    
'''