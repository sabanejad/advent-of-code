import sys
from typing import Tuple
from itertools import chain


def check_id(id: str):
    # the len of range we care to check
    for i in range(1, len(id)//2+1):
        validity = []
        # the start of the range to check
        for j in range(len(id)):
            if j + 2 * i > len(id):
                break
            if id[j:j+i] == id[j+i:j+2*i]:
                validity.append(True)
            else:
                validity.append(False)
        if all(validity):
            return id
    return None

def check_for_invalid_ids(_range: Tuple[int, int]):
    start, end = _range
    invalid_ids = []
    for i in range(int(start), int(end)+1):
        invalid_ids.append(check_id(str(i)))
    return invalid_ids

def main():
    for s in sys.stdin:
        ranges = [_range.split('-') for _range in s.split(',')]
    invalid_ids = []
    for _range in ranges:
        invalid_ids.append(check_for_invalid_ids(_range))
    return sum([int(x) for x in chain.from_iterable(invalid_ids) if x is not None])


if __name__ == '__main__':
    print(main())