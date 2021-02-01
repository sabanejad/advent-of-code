def adds_to_sum(s, n):
    while True:
        elem = s.pop()
        for i in s: 
            if elem + i == n:
                return i * elem

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