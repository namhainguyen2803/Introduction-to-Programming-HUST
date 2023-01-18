class string_utilities():
    def is_valid_parenthese(self,word):
        lis = list(word)
        new1 = 0
        new2 = 0
        new3 = 0
        for i in lis:
            if i == '[':
                new1 = new1 + 1
            elif i == ']':
                new1 = new1 - 1
            if i == '{':
                new2 = new2 + 1
            elif i == '}':
                new2 = new2 - 1
            if i == '(':
                new3 = new3 + 1
            elif i == ')':
                new3 = new3 - 1
            
            if new1 < 0 or new2 < 0 or new3 < 0:
                return False
        if new1 == new2 == new3 == 0:
            return True
        return False
    def reverse_words(self,word):
        lis = word.split(' ')
        lis = lis[::-1]
        return ' '.join(lis)

print(string_utilities().is_valid_parenthese('{[(])]}'))
print(string_utilities().is_valid_parenthese('{[()(({}))]}'))
print(string_utilities().reverse_words('Bach khoa Ha Noi'))