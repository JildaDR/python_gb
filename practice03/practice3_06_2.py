def int_func(text):
    while True:
        text_list = list(text)
        err = None
        text_upd = None
        for i in range(len(text_list)):
            if ord(text_list[i]) < 97 or ord(text_list[i]) > 122:
                print('Вы ввели недопустимый символ')
                err = 0
                break
            else:
                continue
        if err == 0:
            raise SystemExit
        else:
            text_upd = str.capitalize(text)
            break

    return text_upd


def str_func(string):
    string_list = string.split()
    list_upd = []
    for i in range(len(string_list)):
        list_upd.append(int_func(string_list[i]))
    return ' '.join(list_upd)


print(str_func(input('Напишите строку из нескольких слов латинскими буквами в нижнем регистре: ')))
