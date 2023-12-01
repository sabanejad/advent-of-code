import sys

def find_digits(s):
    digits = []
    for elem in s:
        if elem.isdigit():
            digits.append(int(elem))
    return digits[0]*10 + digits[-1]

def main():
    sum = 0
    for s in sys.stdin:
        sum += find_digits(s.strip())
    print(sum)

if __name__ == '__main__':
    main()