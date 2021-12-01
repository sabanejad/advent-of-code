import sys

def count_increase(s):
    increase = 0
    for i in range(1, len(s)):
        if s[i] > s[i-1]:
            increase += 1
    return increase

def main():
    depth = []
    for s in sys.stdin:
        depth.append(int(s))
    print(count_increase(depth))

if __name__ == "__main__":
    main()