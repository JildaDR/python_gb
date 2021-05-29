from random import sample

my_list = [el for el in sample(range(1, 300), 20)]
print(my_list)
my_list2 = []
for i in range(1, len(my_list)):
    if my_list[i] > my_list[i - 1]:
        my_list2.append(my_list[i])

print(my_list2)

