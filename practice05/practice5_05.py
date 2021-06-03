from random import randint

with open("practice5_05in.txt", "w+", encoding="utf-8") as task_out:
    nums = []
    i = 0
    while i <= 21:
        nums.append(str(randint(1, 100)))
        i += 1
    print(' '.join(nums), end='', file=task_out)
with open("practice5_05in.txt", "r", encoding="utf-8") as task_in:
    in_nums = task_in.read()
    a = in_nums.split()
    sum_nums = 0
    for i in a:
        sum_nums += int(i)

    print(sum_nums)