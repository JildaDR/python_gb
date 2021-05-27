def my_func(a, b, c):
    my_sum = (a + b + c) - min(a, b, c)
    return print(my_sum)


print(my_func(int(input('Введите число: ')),
              int(input('Введите еще число: ')),
              int(input('И еще одно число: '))))
