# *Завдання* - вам потрібно вивести в консольку це проміжок чисел у форматі `[-99; 43)`
# тобто сам проміжок це числа від -99……42


def func_range(text):
    first = text.replace(text, text[1:4])
    second = text.replace(text, text[5:7])
    new_str = "[{};{})".format(first, second)
    print('you input data :', new_str)
    return print('you range list :', list(range(int(first), int(second))))

func_range('[-99,43)')