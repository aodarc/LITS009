import os
import glob


def my_func():
    filename = input('Введіть назву файла' + '\n')
    filename_extends = filename.split('.')
    print('Файли з розширенням : ' + repr(filename_extends[-1]))
    my_path = os.getcwd()
    my_file = os.listdir(my_path)
    if filename == '*.py':
        print(glob.glob('./*.py'))
    if filename == '*.txt':
        print(glob.glob('./*.txt'))
    if filename in my_file:
        print(os.path.abspath(filename))
    else:
        print('Файл з таким іменем не знайдений')


if __name__ == '__main__':
    my_func()