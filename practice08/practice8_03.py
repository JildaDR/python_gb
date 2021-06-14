class MyException(Exception):
    pass


class Validate:

    @staticmethod
    def validate(i):
        if not i.isdigit():
            return False
        return True


my_list = []
while True:
    a = input('enter some digit (or enter STOP for stop iteration): ')
    try:
        if Validate.validate(a):
            my_list.append(a)
            continue
        elif a.lower() == 'stop':
            break
        raise MyException
    except MyException as err:
        print('Only digit please!')
        continue

print(my_list)
