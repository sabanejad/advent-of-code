import sys

def parse(s):
    return list(s)

def main():
    score = 0
    pos = 0
    for s in sys.stdin:
        for char in parse(s):
            if score == -1:
                print(pos)
                break
            if char == '(':
                score += 1
                pos += 1
            elif char == ')':
                score -= 1
                pos += 1

if __name__ == "__main__":
    main()