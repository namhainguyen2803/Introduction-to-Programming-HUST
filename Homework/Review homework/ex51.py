def max_num_in_list(list):
    max = list[0]
    for a in list:
        if a > max:
            max = a
    return max
def flatten_nested_list(nested_lst):
    return [item for sublist in nested_lst for item in sublist]
a = eval(input())
flat_a = flatten_nested_list(a)
print(*flat_a)
print(max_num_in_list(flat_a))