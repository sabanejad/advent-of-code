import sys

def ingest_map():
    map = {}
    ns = 0
    for s in sys.stdin:
        ew = 0
        for e in s.strip():
            map[(ew, ns)] = int(e)
            ew += 1
        ns += 1
    box = ew, ns
    return box, map

def count_map(box, map):
    x, y = box
    sum = 0
    for (a, b), v in map.items():
        if a == 0 or a == x-1 or b == 0 or b == y-1:
            continue
        elif check_map(a, b, x, y, map):
            sum += 1
    return sum + x * 2 + y * 2 - 4
        
def check_map(a, b, height, width, map):
    right = True
    left = True
    up = True
    down = True
    x, y = a-1, b
    while x >= 0:
        if map[x, y] >= map[a, b]:
            left = False
        x -= 1
    x, y = a+1, b
    while x <= width-1:
        if map[x, y] >= map[a, b]:
            right = False
        x += 1
    x, y = a, b-1
    while y >= 0:
        if map[x, y] >= map[a, b]:
            up = False
        y -= 1
    x, y = a, b+1
    while y <= height-1:
        if map[x, y] >= map[a, b]:
            down = False
        y += 1
    return right or left or up or down

def main():
    box, map = ingest_map()
    print(count_map(box, map))

if __name__ == "__main__":
    main()