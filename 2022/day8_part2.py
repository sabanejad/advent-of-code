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
    max_score = 0
    for (a, b), v in map.items():
        if a == 0 or a == x-1 or b == 0 or b == y-1:
            continue
        elif get_scenic_score(a, b, x, y, map) > max_score:
            max_score = get_scenic_score(a, b, x, y, map)
    return max_score
        
def get_scenic_score(a, b, width, height, map):
    right = 0
    left = 0
    up = 0
    down = 0
    x, y = a-1, b
    while x >= 0:
        if map[x, y] >= map[a, b] or x == 0:
            # up = a - x
            break
        x -= 1
    left = a - x
    x, y = a+1, b
    while x <= width-1:
        if map[x, y] >= map[a, b] or x == width-1:
            break
        x += 1
    right = x - a
    x, y = a, b-1
    while y >= 0:
        if map[x, y] >= map[a, b] or y == 0:
            break
        y -= 1
    up = b - y
    x, y = a, b+1
    while y <= height-1:
        if map[x, y] >= map[a, b] or y == height-1:
            break
        y += 1
    down = y - b
    return up * left * down * right

def main():
    box, map = ingest_map()
    print(count_map(box, map))

if __name__ == "__main__":
    main()