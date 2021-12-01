import sys

def check_count(s, n):
    for char in set(s):
        if s.count(char) == n:
            return True
    return False

def main():
    twos = 0
    threes = 0
    for line in sys.stdin:
        twos += check_count(line, 2)
        threes += check_count(line, 3)
    print(twos * threes)

if __name__ == "__main__":
    main()