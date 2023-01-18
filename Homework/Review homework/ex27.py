def is_palindrome(st):
    li = [i for i in st if i !=' ']
    if li == li[::-1]:
        return 'YES'
    return 'NO'
print(is_palindrome(input()))