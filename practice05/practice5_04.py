# Не поняла, как импортировать модуль для перевода, предложенные в интернете варианты
# не работают, пожалуйста, напишите, какой именно модуль надо импотировать и способ
# его применения. Сделала 2 варианта с readlines и readline
with open("practice5_04in.txt", "r", encoding="utf-8-sig") as task_in, \
        open("practice5_04out.txt", "w", encoding="utf-8-sig") as task_out:
    content = task_in.readlines()
    outtab = ['один', 'два', 'три', 'четыре']
    c = 0
    for i in content:
        a = i.split()
        a[0] = outtab[c]
        c += 1
        print(' '.join(a), file=task_out)

with open("practice5_04in.txt", "r", encoding="utf-8-sig") as task_in, \
        open("practice5_04out.txt", "w", encoding="utf-8-sig") as task_out:
    outtab = ['один', 'два', 'три', 'четыре']
    c = 0
    while True:
        line = task_in.readline()
        if not line:
            break
        a = line.split()
        a[0] = outtab[c]
        c += 1
        print(' '.join(a), file=task_out)

