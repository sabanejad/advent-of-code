import sys
import numpy
import string

from itertools import zip_longest

def find_priority(ch):
    keys = list(string.ascii_letters)
    values = list(numpy.arange(1, 53))
    d = dict(zip_longest(keys, values))
    return d[ch]

def find_common(l):
    return (set(l[0]).intersection(set(l[1]))).intersection(l[2]).pop()

def main():
    sum = 0
    groups = []
    for s in sys.stdin:
        if len(groups) >= 3:
            common = find_common(groups)
            sum += find_priority(common)
            groups = []
            groups.append(s.strip())
        else:
            groups.append(s.strip())
    if len(groups) >= 3:
        common = find_common(groups)
        sum += find_priority(common)
    print(sum)

if __name__ == "__main__":
    main()