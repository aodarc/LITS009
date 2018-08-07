import math

x = float(input('Please input number for x '))
u = float(input('Please input number for u '))
o = float(input('Please input number for o '))

result = 1/(o*math.sqrt(2*math.pi))*math.exp(-((x-u)**2/2*o**2))

print(result)
