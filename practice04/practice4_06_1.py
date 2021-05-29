# на всякий случай реализовала скрипт с использованием argv

from itertools import count
from sys import argv

script_name, start_count, stop_count = argv

for i in count(int(start_count)):
    if i > int(stop_count):
        break
    else:
        print(i)

