import time as t

# start first generator numb

start = t.time()

for num in range(1, 101):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=' ')

print('\n')

end = t.time()
func_time_one = (end - start)

# start second simple numb

start = t.time()

spisok = (1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
new_spisok = []
index = 0

while index < len(spisok):
    new_spisok.append(spisok)
    print(new_spisok, '\n')
    break

end = t.time()

func_time_two = (end - start)

print('Time work generators :', func_time_one, '\n')
print('Time work cycle while :', func_time_two, '\n')
print('Time difference :', func_time_two - func_time_one)
