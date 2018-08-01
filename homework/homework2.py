#1 homework__________________________

str = '((((((((((((((2, 3)))))))))))))'
str.count('(')
str.count(')')
print(str.count('('))
print(str.count(')'))
if str.count('(') == str.count(')'):
    print('parenthesis are balanced')
else:
    print('parenthesis are not balanced')

#2 homework__________________________


lst = [1, [2, 3], 4, [[6, 7]]]

lst = [lst[0], lst[1][0], lst[1][1], lst[2], lst[3][0][0], lst[3][0][1]]
print(lst)
