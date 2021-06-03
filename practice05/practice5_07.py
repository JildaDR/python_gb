import json
with open("practice5_07.txt", "r", encoding="utf-8-sig") as task_in:
    c = 0
    my_list = []
    dict_profit = {}
    dict_average = {}
    dict_loss = None
    sum = 0
    while True:
        line = task_in.readline()
        if not line:
            break
        a = line.split()
        f = filter(str.isdigit, a.pop())
        a.append("".join(f))
        a_profit = int(a[2]) - int(a[3])
        if a_profit < 0:
            dict_loss = {}
            dict_loss[a[0]] = (f'loss: {abs(a_profit)}')
        else:
            dict_profit[a[0]] = a_profit
            sum += a_profit
            c += 1
    avg = sum / c
    dict_average['average profit'] = avg
    my_list.append(dict_profit)
    my_list.append(dict_average)
    if dict_loss != None:
        my_list.append(dict_loss)

with open("practice5_07.json", "w") as write_f:
        json.dump(my_list, write_f)



