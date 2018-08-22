import math
import sys

x = int(input('Введіть х :'))
b = int(input('Введіть b :'))
c = float(input('Введіть c :'))
a = (1 / (c * math.sqrt(2 * math.pi))) * math.exp(-(((x - b) ** 2) / 2 * c ** 2))
print(sys.argv)
print(a)
