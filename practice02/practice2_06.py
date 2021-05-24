my_list = []
list_name = []
list_price = []
list_amount = []
list_unit = []
my_tuple = tuple()
i = 1
while True:
    name = input('Введите название товара: ')
    price = int(input('Введите цену товара: '))
    amount = int(input('Введите количество товаров: '))
    unit = input('Введите единицу измерения товара: ')
    my_dict = {
        'название': name,
        'количество': amount,
        'цена': price,
        'единица измерения': unit}
    my_tuple = (i, my_dict)
    my_list.append(my_tuple)
    i += 1
    print(my_list)
    list_name.append(name)
    list_price.append(price)
    list_amount.append(amount)
    list_unit.append(unit)
    analytics = {
        ([key for key in my_dict.keys()][0]): list_name,
        ([key for key in my_dict.keys()][1]): list_price,
        ([key for key in my_dict.keys()][2]): list_amount,
        ([key for key in my_dict.keys()][3]): list_unit}
    print(analytics)