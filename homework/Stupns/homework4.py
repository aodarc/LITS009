def find_most_frequent(text, symbol='.,:;!?- '):  #
    a = {}  # пустий словник
    s = ''  # пуста строка
    for i in text.lower():  # перебір тексту в нижньому регістрі
        if i not in symbol:  # якщо не символ, то
            s += i  # записую в тимчасову строку цей символ
        elif s:  # інакше якщо не пуста
            a[s] = a.setdefault(s, 0) + 1  # якщо це слово є в словнику змінюємо значення,
            #  якщо нема, створюємо значення 1
            s = ''  # обнуляю строку
    if not a:  # якщо словник пустий
        return False  # повертаємо False
    m = max(a.values())  # в змінну m записуємо максимальне значення значень словника
    return sorted([i for i in a if a[i] == m])  # сортую щоб показувало за зростанням


print(find_most_frequent('to understand recursion you need first to understand recursion...'))
