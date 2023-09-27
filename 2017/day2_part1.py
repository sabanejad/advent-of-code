import sys

def min_max_dif(l):
    return max(l) - min(l)

def main():
    _sum = 0
    for s in sys.stdin:
        l = [int(i) for i in s.strip().split('	')]
        _sum += min_max_dif(l)
    print(_sum)

if __name__ == "__main__":
    main()