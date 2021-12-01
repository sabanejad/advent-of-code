import sys
import re

def parse_claim(s):
    return tuple(int(x) for x in re.findall('[0-9]+', s))

def fill_grid(claims):
    grid = {}
    for claim in claims:
        i, a, b, c, d = claim
        for x in range(a, a+c):
            for y in range(b, b+d):
                grid[x, y] = grid.get((x, y), 0) + 1
    return grid

def find_collisions(claims, grid):
    for claim in claims:
        i, a, b, c, d = claim
        sum_ = 0
        for x in range(a, a+c):
            for y in range(b, b+d):
                sum_ += grid[x, y]
        if sum_ == c * d: 
            print(i)

def main():
    claims = []
    for s in sys.stdin:
        claims.append(parse_claim(s))
    grid = fill_grid(claims)
    find_collisions(claims, grid)

if __name__ == "__main__":
    main()