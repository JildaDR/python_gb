def my_func():
    n = int(input('num: '))
    n_list = list(range(1, n + 1))
    my_multiplier = range(2, n + 1)
    for i in my_multiplier:
        a = i
        my_func2(a, n, n_list)
    return n_list

def my_func2(x, y, z):
    for i in range(2, y + 1):
        exclude = x * i
        if exclude <= y:
            try:
                z.remove(exclude)
            except ValueError:
                pass
        else:
            return z



print(my_func())