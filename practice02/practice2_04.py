my_text = input('Составьте строку из нескольких слов: ')
text_list = my_text.split()
for ind, el in enumerate(text_list):
    print(ind, el[:10])
