# использовала оба варианта принт и writelines для наглядности
with open("user_text.txt", "w", encoding="utf-8") as u_txt:
    u_txt.writelines([input('first name: '),'\n', input('last name: '),'\n', input('city: '),'\n'])
    print(input('enter your age: '), file=u_txt)
    print(input('your gender: '), file=u_txt)