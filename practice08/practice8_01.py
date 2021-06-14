class MyException(Exception):
    pass


class Data:
    def __init__(self, data):
        self.data = str(data)

    @classmethod
    def get_data(cls, data):
        my_list = data.split('-')
        day = int(my_list[0])
        month = int(my_list[1])
        year = int(my_list[2])
        try:
            if Data.validator(day, month, year):
                return f'день: {day}, месяц: {month}, год: {year}'
            raise MyException
        except MyException:
            print('Вы ввели недопустимое значение!')
        return f'end program'




    @staticmethod
    def validator(day, month, year):
        if month in (1, 3, 5, 7, 8, 10, 12) and 1 <= day <= 31 and year <= 2021:
            return True
        elif month in (4, 6, 9, 11) and 1 <= day <= 30 and year <= 2021:
            return True
        elif month == 2 and 1 <= day <= 28 and year <= 2021:
            return True
        elif month == 2 and 1 <= day <= 29 and year in range(0, 2021, 4):
            return True
        return False


print(Data.get_data('21-12-1978'))
print(Data.get_data('31-05-2000'))
print(Data.get_data('29-02-1972'))
print(Data.get_data('29-02-1985'))

