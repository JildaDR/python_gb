def fact(n):
    el = 1
    for i in range(1, n + 1):
        el *= i
        yield el


for el in fact(int(input('Введите число для получения факториала: '))):
    print(el)
