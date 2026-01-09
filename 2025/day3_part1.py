import sys
from itertools import combinations
import time

# time: 0.033
# def find_max_joltage(battery):
#     _combinations = combinations(battery, 2)
#     max_joltage = max(_combinations)
#     return int(str(max_joltage[0])+str(max_joltage[1]))

# time: 0.004
def find_max_joltage(battery, how_many: int = 2):
    # find max digit not including the last digit
    if len(battery) < how_many:
        raise Exception('battery too small')
    if how_many < 1:
        return ''
    if how_many > 1:
        digit = max(battery[:-how_many+1])
    else:
        digit = max(battery)
    digit_index = battery.index(digit)
    return int(''.join([str(digit)] + [str(find_max_joltage(battery[digit_index + 1:], how_many=how_many-1))]))

def main():
    _sum = 0
    for s in sys.stdin:
        _sum += find_max_joltage([int(x) for x in s.strip()])
    return _sum

if __name__ == '__main__':
    start = time.time()
    print(main())
    print('time:', time.time()-start)