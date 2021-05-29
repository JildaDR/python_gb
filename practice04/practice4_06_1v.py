from itertools import count

start_count = int(input('Введите число, с которого начнется генерация последовательности: '))
stop_count = int(input('Введите число, на котором закончится генерация последовательности: '))

for i in count(int(start_count)):
    if i > int(stop_count):
        break
    else:
        print(i)
