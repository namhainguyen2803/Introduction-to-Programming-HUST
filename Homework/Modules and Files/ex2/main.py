import list_utilities 

x = eval(input())
new = list_utilities.flatten_nested_list(nested_lst=x)
for i in new[:-1]:
    print(i, end=' ')
print(new[-1],end='\n')
#print(new)
print(list_utilities.max_num_in_list(new))