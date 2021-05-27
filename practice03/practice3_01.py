def division(a, b):
    return a / b

while True:
    try:
        print(division(int(input('Введите число (делимое): ')), int(input('Введите число (делитель): '))))
    except (ValueError, TypeError):
        print('Вы ввели неправильное значение')
        continue
    except ZeroDivisionError:
        print('Деление на 0 невозможно')
        continue


