import math


def my_func(*args):
    x = float(input('Введіть х :'))
    b = float(input('Введіть b :'))
    c = float(input('Введіть c :'))
    a = 1 / (c * math.sqrt(2 * math.pi)) * math.exp((-(x - b) ** 2) / 2 * c ** 2)
    return print(a)
