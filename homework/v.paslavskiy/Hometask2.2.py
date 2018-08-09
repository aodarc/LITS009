str = '((((((((((((((2, 3)))))))))))))'

def brackets(brec):
    count = 0
    for c in brec:
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1
    if count > 0:
        print('brackets are not equal')
    elif count == 0:
        print('brackets are equal')
   
brackets(str)



    # if count < 0:
    #     return False
    # elif count == 0:
    #     return True
