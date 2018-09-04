import os
import glob


def my_func():
    filename = input('Введіть назву файла' + '\n')
    filename_extends = filename.split('.')
    my_path = os.getcwd()
    my_file = os.listdir(my_path)
    if filename == '*.py':
        print(glob.glob('./*.py'))
    if filename == '*.txt':
        print(glob.glob('./*.txt'))
    if filename in my_file:
        print('Шлях файлу : ' + os.path.abspath(filename) + ' , файл з розширенням : ' + repr(filename_extends[-1]))
    else:
        print('Файл з таким іменем не знайдений')


if __name__ == '__main__':
    my_func()

# 2 method with endswith
# filename = input('Введіть назву файла' + '\n')
# my_path = os.getcwd()
# for filename in os.listdir(my_path):
#     if filename.endswith('.txt'):
#         print(filename)
#     if filename.endswith('.py'):
#         print(filename)
