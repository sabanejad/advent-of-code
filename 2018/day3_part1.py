import sys
import re

def parse_claim(s):
    return tuple(int(x) for x in re.findall('[0-9]+', s)[1:])

def fill_grid(claims):
    grid = {}
    for claim in claims:
        a, b, c, d = claim
        for x in range(a, a+c):
            for y in range(b, b+d):
                grid[x, y] = grid.get((x, y), 0) + 1
    return grid

def main():
    claims = []
    for s in sys.stdin:
        claims.append(parse_claim(s))
    grid = fill_grid(claims)
    print(sum(1 for v in grid.values() if v > 1))

if __name__ == "__main__":
    main()