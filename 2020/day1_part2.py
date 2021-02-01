from itertools import combinations

def adds_to_sum(s, n):
    while True:
        elem = s.pop()
        for a, b in combinations(s, 2):
            if a + b + elem == n:
                return elem * a * b

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