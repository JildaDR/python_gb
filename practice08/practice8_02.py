class OwnError(Exception):
    pass


b = float(input('Введите число (делимое): '))
while True:
    c = float(input('Введите число (делитель): '))
    try:
        if c == 0:
            raise OwnError('На 0 делить нельзя!')
    except OwnError as err:
        print('На 0 делить нельзя!')
        continue
    break

a = b / c

print("%.2f" % a)