"""Задачка1
Розробити функцію *convert_n_to_m(x, n, m)*,
яка приймає 3 аргументи -- ціле число (в системі числення з основою n) 
або рядок x, що представляє таке число, та цілі числа n та m (1 <= n, m <= 36),
та *повертає рядок* -- `представлення числа х у системі числення m.`_У випадку, 
якщо аргумент х не є числом або рядком, або не може бути представленням 
цілого невід’ємного числа в системі числення з основою n, повернути логічну константу False"""
import string


def convert_n_to_m(x, n, m):
    lists = string.hexdigits
    if not isinstance(x, (str, int)):  # якщо в х не входить число або строка- повертаєм False
        return False
    if m > 36 and n < 1:  # якщо m > 36 , повертаєм False
        return False
    try:
        num = int(str(x), n)
    except ValueError:
        return False
    try:
        if m == 1:
            return '0' * num
        else:
            result = ''
            while num != 0:
                digit = num % m
                result += lists[digit]
                num = num // m
            return result[::-1]
    except ValueError:
        return False
    else:
        return result


print(convert_n_to_m([123], 4, 3))
print(convert_n_to_m("0123", 5, 6))
print(convert_n_to_m("123", 3, 5))
print(convert_n_to_m(123, 4, 1))
print(convert_n_to_m(-123.0, 11, 16))
print(convert_n_to_m("A1Z", 36, 16))
