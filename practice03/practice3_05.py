result = [0]
while True:
    a = input('введите числа через пробелы: ')
    a = a.split()
    for i in range(len(a)):
        b = result[0]
        try:
            b = b + int(a[i])
        except (ValueError, TypeError):
            result.clear()
            result.append(b)
            print(f'Вы ввели недопустимый символ, сумма до символа: {result[0]}')
            raise SystemExit

        result.clear()
        result.append(b)
    print(f'Сумма введенных чисел: {result[0]}')
