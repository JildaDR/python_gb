first_day = int(input('how many kilometers does the athlete run on the first day? '))
last_day = int(input('how many kilometers should an athlete run? '))
i = 1

while first_day < last_day:
    print(f'day {i}: athlete runs {first_day:.2f} km')
    first_day = first_day + (first_day * 0.1)
    i += 1


print(f'day {i}: athlete runs {first_day:.2f} km')
print(f'{first_day:.2f} km the athlete will run on {i}th day')
