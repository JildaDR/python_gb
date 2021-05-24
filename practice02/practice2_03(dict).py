#вариант со словарем
season = {'winter': [12, 1, 2], 'spring': [3, 4, 5], 'summer': [6, 7, 8], 'autumn': [9, 10, 11]}
month = int(input('Введите числовое значение месяца: '))
for key, value in season.items():
    if month in value:
        print(f'{key}')
