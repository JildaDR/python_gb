my_list = [7, 5, 5, 3, 2]
while True:
    number = int(input('Введите натуральное число: '))
    for i in (my_list):
        if number > max(my_list):
            my_list.insert(0, number)
            break
        elif number < min(my_list):
            my_list.append(number)
            break
        elif number == i:
            continue
        elif number > i:
            ind = my_list.index(i)
            my_list.insert(ind, number)
            break
    print(my_list)
