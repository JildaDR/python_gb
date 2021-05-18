number = int(input("Please enter any digit, I will convert it in time format hh:mm:ss: "))


ss = int(number % 60)
mm = int((number / 60) % 60)
hh = int((number // 60) / 60)
dd = int(hh / 24)
hd = int(hh % 24)

if hh >= 24:
    print(f'{dd} days, {hd:02d}:{mm:02d}:{ss:02d}')
else:
    print(f'{hh:02d}:{mm:02d}:{ss:02d}')
