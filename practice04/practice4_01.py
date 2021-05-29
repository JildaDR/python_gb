from sys import argv

script_name, hours, rate, bonus = argv


def payments(a, b, c):
    return int(a) * int(b) + int(c)


print(payments(hours, rate, bonus))
