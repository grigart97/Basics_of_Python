import sys
import itertools as it

# script_1.1. 1-st num - Start, 2-nd num - quantity
count_iterator = it.count(int(sys.argv[1]))
print([next(count_iterator) for _ in range(int(sys.argv[2]))])

# script_1.2. 1-st num - Start, 2-nd num - quantity
for el in it.islice(it.count(int(sys.argv[1])), int(sys.argv[2])):
    print(el, end=' ')

# script_2.1. 1-st num - quantity
cycle_iterator = it.cycle([300, 2, 12, 44, 1])
print([next(cycle_iterator) for _ in range(int(sys.argv[1]))])

# script_2.2. 1-st num - quantity
for el in it.islice(it.cycle([300, 2, 12, 44, 1]), int(sys.argv[1])):
    print(el, end=' ')
