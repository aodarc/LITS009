import timeit


def numberGenerator(n):
    number = 0
    while number < n:
        yield number
        number += 1


def simple_func():
    a = []
    b = a.append(0)
    c = a.append(1)
    d = a.append(2)
    f = a.append(3)
    g = a.append(4)
    h = a.append(5)
    j = a.append(6)
    k = a.append(8)
    l = a.append(9)
    return a


if __name__ == '__main__':
    print('Work Number generator func ~ms :')
    print(timeit.timeit("numberGenerator(10)", setup="from __main__ import numberGenerator"))
    print('Work Simple func ~ms :')
    print(timeit.timeit("simple_func()", setup="from __main__ import simple_func"))
