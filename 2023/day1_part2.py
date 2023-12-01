import sys

text_to_num = {
    'one': 1, 
    'two': 2, 
    'three': 3, 
    'four': 4, 
    'five': 5, 
    'six': 6, 
    'seven': 7, 
    'eight': 8,
    'nine': 9
}

def find_digits(s):
    index_digit = [] # list of (index, digit) tuples
    for d in text_to_num:
        if d in s:
            index_digit.append((s.index(d), text_to_num[d]))
    for elem in s:
        if elem.isdigit():
            index_digit.append((s.index(elem), int(elem)))
    index_digit = sorted(index_digit)
    if len(index_digit) < 2:
        print(s, index_digit)
        return index_digit[0][1]
    else:
        return index_digit[0][1]*10 + index_digit[-1][1]

def main():
    sum = 0
    for s in sys.stdin:
        # print(s.strip(), find_digits(s.strip()))
        sum += find_digits(s.strip())
    print(sum)

if __name__ == '__main__':
    main()