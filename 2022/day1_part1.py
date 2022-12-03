import sys

def main():
    max = 0
    total = 0
    for s in sys.stdin:
        if s != '\n':
            total += int(s)
        else:
            if total > max:
                max = total
            total = 0
    if total > max:
        max = total
    print(max)

if __name__ == "__main__":
    main()