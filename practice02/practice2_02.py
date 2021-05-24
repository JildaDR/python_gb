l = input('Введите элементы списка через пробел: ')
l_list = l.split()
if len(l_list) % 2 > 0:
    l_list.extend(' ')
    l_list[::2], l_list[1::2] = l_list[1::2], l_list[::2]
    l_list.remove(' ')
else:
    l_list[::2], l_list[1::2] = l_list[1::2], l_list[::2]

print(l_list)
