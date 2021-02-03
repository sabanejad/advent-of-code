def adds_to_sum(s, n):
    while True:
        try:
            elem = s.pop()
        except IndexError:
            raise ValueError('invalid input')
        delta = n - elem
        if delta in s:
            return delta * elem

def main():
    s = set()
    while True:
        try:
            s.add(int(input()))
        except EOFError: 
            break
    print(adds_to_sum(s, 2020))

if __name__ == "__main__":
    main()