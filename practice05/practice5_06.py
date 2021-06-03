with open("practice5_06.txt", "r", encoding="utf-8-sig") as task_out:
    content = task_out.readlines()
    my_dict = {}
    for i in content:
        a = i.split()
        a_list = 0
        for i in a[1::]:
            f = filter(str.isdigit, i)
            f1 = "".join(f)
            try:
                a_list += int(f1)
            except ValueError:
                pass
        my_dict[a[0]] = a_list
    print(my_dict)
