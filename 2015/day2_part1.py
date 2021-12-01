import sys
import re
import itertools

def parse(s):
    return [int(x) for x in re.findall('[0-9]+', s)]

def main():
    sum_ = 0
    for s in sys.stdin:
        smallest_side = float('inf')
        for dims in list(itertools.combinations(parse(s), 2)):
            x, y = dims
            sum_ += 2 * x * y
            if x * y < smallest_side:
                smallest_side = x * y
        sum_ += smallest_side
    print(sum_)

if __name__ == "__main__":
    main()