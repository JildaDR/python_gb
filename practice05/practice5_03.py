with open("practice5_03.txt", "r", encoding="utf-8-sig") as salary:
    content = salary.readlines()
    salary_min = []
    b = 0
    c = 1
    for i in content:
        i = i.strip('\n')
        a = i.split()
        c += 1
        b = b + int(a[1])
        if int(a[1]) < 20000:
            salary_min.append(i)
            salary_min.append('\n')
    salary_mid = b / c


# не поняла, почему перед фамилией Иванов появляется пробел, не смогла с этим разобраться
# напишите, пожалуйста, как правильно реализовать этот вывод
#   print(f'Список всех сотрудников и их зарплаты:\n',''.join(content))
# пришлось на два принта разбить вывод
    print(f'Список всех сотрудников и их зарплаты:')
    print(''.join(content))
    print(f'Список сотрудников, чьи зарплаты меньше 20000:')
    print(''.join(salary_min))
    print(f'Средняя зарплата сотрудников: {int(salary_mid)}')
