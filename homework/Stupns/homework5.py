#Функція сортування бульбашкою

def mysort(li):
    n = len(li)
    for j in range(0, n - 1):
        # вложений цикл порівнює i-ий c i+1 -им елементом і
        # при необхідності міняє їх місцями
        # к-сть порівняннь кожен раз зменшиться на величину j
        for i in range(0, n - j - 1):
            if li[i] > li[i + 1]:
                li[i + 1], li[i] = li[i], li[i + 1]
        print(j + 1, "- ий прохід циклу - ", end=" ")
        print(li)
    return(li)

print(mysort([0, 5, 8, 4, 9, 3]))

#реверснути можна 2 способами :
#перший спосіб це return(li[::-1])
#другий спосіб це переставити місцями li[i],li[i + 1]  = li[i + 1],li[i]