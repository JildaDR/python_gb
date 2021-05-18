num = int(input("Please enter any number: "))
big_digit = 0
while num > 0:
    digit = num % 10
    if digit > big_digit:
        big_digit = digit
    num = num // 10


print(f'The biggest digit in the number is {big_digit}')
