def my_func():
    while True:
        try:
            x = int(input('введите целое положительное число: '))
        except (ValueError, TypeError):
            continue
        if x <= 0:
            continue
        while True:
            try:
                y = int(input('введите целое отрицательное число: '))
            except (ValueError, TypeError):
                continue
            if y >= 0:
                continue
            break
        break
    my_pow = 1 / (x ** abs(y))
    return my_pow


def my_func2():
    while True:
        try:
            x = int(input('введите целое положительное число: '))
        except (ValueError, TypeError):
            continue
        if x <= 0:
            continue
        while True:
            try:
                y = int(input('введите целое отрицательное число: '))
            except (ValueError, TypeError):
                continue
            if y >= 0:
                continue
            break
        break
    i = abs(y) - 1
    my_pow = x
    while i > 0:
        my_pow = my_pow * x
        i -= 1
    return 1 / my_pow



print(my_func())
print(my_func2())