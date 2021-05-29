import random

my_list = [random.randint(1, 20) for i in range(12)]
print(my_list)
my_list2 = [i for i in my_list if my_list.count(i) == 1]
print(my_list2)
