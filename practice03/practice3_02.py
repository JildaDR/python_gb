def user_data(name, l_name, b_date, city, email, tel):
    return print(f'Имя: {name}, '
                 f'фамилия: {l_name}, '
                 f'год рождения: {b_date}, '
                 f'город рождения: {city}, '
                 f'эл.адрес: {email}, '
                 f'телефон: {tel}')


user_data(
    name=input('Введите имя: '),
    l_name=input('Введите фамилию: '),
    b_date=input('Введите год рождения: '),
    city=input('Введите город проживания: '),
    email=input('Введите электронный адрес: '),
    tel=input('Введите номер телефона: ')
)
