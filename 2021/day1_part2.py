import sys

def sum_slide(s, n):
    sum_ = []
    for i in range(n-1, len(s)):
        sum_.append(s[i-n+1] + s[i-n+2] + s[i])
    return sum_

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
    print(count_increase(sum_slide(depth, 3)))

if __name__ == "__main__":
    main()