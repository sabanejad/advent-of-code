import sys
import re
import numpy

def parse(s):
    return sorted([int(x) for x in re.findall('[0-9]+', s)])

def main():
    sum_ = 0
    for s in sys.stdin:
        dims = parse(s)
        sum_ += dims[0] * 2 + dims[1] * 2 + numpy.prod(dims)
    print(sum_)

if __name__ == "__main__":
    main()