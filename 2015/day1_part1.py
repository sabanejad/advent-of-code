import sys

def parse(s):
    return list(s)

def main():
    score = 0
    for s in sys.stdin:
        for char in parse(s):
            if char == '(':
                score += 1
            elif char == ')':
                score -= 1
    print(score)

if __name__ == "__main__":
    main()