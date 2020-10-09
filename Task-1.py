import sys

# py_name, work_hoours, money_per_hour, prize = sys.argv
# print(f'Your salary - {work_hoours * money_per_hour + prize}')
print(f'Your salary - {int(sys.argv[1]) * int(sys.argv[2]) + int(sys.argv[3])}')