import sys

def int_split(s):
    a, b = s.split('-')
    return int(a), int(b)

def is_contained(p1, p2):
    s1, e1 = int_split(p1)
    s2, e2 = int_split(p2)
    if s1 <= s2 and e1 >= e2: return True
    if s2 <= s1 and e2 >= e1: return True
    return False

def main():
    count = 0
    for s in sys.stdin:
        p1, p2 = s.split(',')
        if is_contained(p1, p2):
            count += 1
    print(count)

if __name__ == "__main__":
    main()