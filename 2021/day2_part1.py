import sys

def move(directions):
    horizontal = 0
    depth = 0
    for d in directions:
        delta = int(d[1])
        if d[0] == 'forward':
            horizontal += delta
        elif d[0] == 'down':
            depth += delta
        elif d[0] == 'up':
            depth -= delta
    return horizontal * depth

def main():
    directions = []
    for s in sys.stdin:
        directions.append(s.split())
    print(move(directions))

if __name__ == "__main__":
    main()