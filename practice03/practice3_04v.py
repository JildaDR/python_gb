def my_func(x, y):
    my_pow = 1 / (x ** abs(y))
    return my_pow


def my_func2(x, y):
    i = abs(y) - 1
    my_pow = x
    while i > 0:
        my_pow = my_pow * x
        i -= 1
    return 1 / my_pow

def my_try():
    while True:
        try:
            a = int(input('введите целое положительное число: '))
        except (ValueError, TypeError):
            continue
        if a <= 0:
            continue
        while True:
            try:
                b = int(input('введите целое отрицательное число: '))
            except (ValueError, TypeError):
                continue
            if b >= 0:
                continue
            break
        break
    return a, b

a, b = my_try()
print(my_func(a, b))
print(my_func2(a, b))