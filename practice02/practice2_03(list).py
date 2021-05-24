#вариант со списком
winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]

month = int(input('Введите числовое значение месяца: '))

if month in winter:
    print('winter')
elif month in spring:
    print('spring')
elif month in summer:
    print('summer')
elif month in autumn:
    print('autumn')
else:
    print('Вы ввели недопустимое значение')


