import sys
from itertools import product

def intersect(s1, s2):
    intersection = ''
    for char1, char2 in zip(s1, s2):
        if char1 == char2:
            intersection += char1
    return intersection

def main():
    IDs = list(sys.stdin)
    for s1, s2 in product(IDs, repeat=2):
        intersection = intersect(s1, s2)
        if len(intersection) == len(s1) - 1:
            print(intersection)
            break

if __name__ == "__main__":
    main()