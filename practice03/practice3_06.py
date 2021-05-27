def int_func(text):
    while True:
        text_list = list(text)
        err = None
        text_upd = None
        for i in range(len(text_list)):
            try:
                ord(text_list[i]) < 97 and ord(i) > 122
            except TypeError:
                print('Вы ввели недопустимый символ')
                err = 0
                break
        if err == 0:
            text = input('Напишите слово строчными буквами: ')
            continue
        else:
            text_upd = str.capitalize(text)
            break

    return text_upd


print(int_func(input('Напишите слово строчными буквами: ')))