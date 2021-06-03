# There's a lady who's sure
# All that glitters is gold
# And she's buying a stairway to heaven.
# When she gets there she knows, if the stores are all closed
# With a word she can get what she came for.
# Ooh, ooh, and she's buying a stairway to heaven.

with open("practice5_02.txt", "r", encoding="utf-8") as text:
    t_strings = text.readlines()
    str_count = len(t_strings)
    print(f'в тексте {str_count} строк')

    for i in t_strings:
        i = i.strip('\n')
        a = i.split()
        a_count = len(a)
        print(f'в строке "{i}" содержится {a_count} слов')