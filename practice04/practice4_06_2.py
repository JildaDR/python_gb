from itertools import cycle

a = input('Введите через пробелы последовательность слов или чисел: ')
stop_count = int(input('Введите число повторений для элементов последовательности: '))

my_list = a.split()

i = 1
for el in cycle(my_list):
    if i > stop_count:
        break
    print(el)
    i += 1