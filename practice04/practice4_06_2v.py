# решила усложнить немного задачу


from itertools import cycle

def my_cycle():
    while True:
        a = input('Введите через пробелы последовательность слов или чисел (не менее 5 элементов последовательности): ')
        my_list = a.split()
        if len(my_list) < 5:
            continue
        else:
            my_list2 = my_list[2], my_list[4]
            break
    return my_list2

my_list2 = my_cycle()

stop_count = int(input('Введите число повторений для третьего и пятого элемента последовательности: '))
i = 1
for el in cycle(my_list2):
    if i > stop_count:
        break
    print(el)
    i += 1