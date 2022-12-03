import sys
import numpy
import string

from itertools import zip_longest

def find_priority(ch):
    keys = list(string.ascii_letters)
    values = list(numpy.arange(1, 53))
    d = dict(zip_longest(keys, values))
    return d[ch]

def find_common(front, back):
    return set(front).intersection(set(back)).pop()

def main():
    sum = 0
    for s in sys.stdin:
        sack = list(s)
        front = sack[:int(len(sack)/2)]
        back = sack[int(len(sack)/2):]
        common = find_common(front, back)
        sum += find_priority(common)
    print(sum)

if __name__ == "__main__":
    main()