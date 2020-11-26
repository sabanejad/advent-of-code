def inc_value(grid, key):
    if key in grid:
        grid[key] += 1
    else:
        grid[key] = 1


def fill_grid(grid, l):
    x = 0
    y = 0
    for item in l:
        direction = item[0]
        steps = item[1]
        if direction == 'U':
            for i in range(y, y + steps):
                inc_value(grid, (x, i))
            y = y + steps
        elif direction == 'R':
            for i in range(x, x + steps):
                inc_value(grid, (i, y))
            x = x + steps
        elif direction == 'D':
            for i in range(y, y - steps, -1):
                inc_value(grid, (x, i))
            y = y - steps
        elif direction == 'L':
            for i in range(x, x - steps, -1):
                inc_value(grid, (i, y))
            x = x - steps

def find_closest_x(grid):
    min_distance = float('inf')
    for (x, y), v in grid.items():
        if v == 2:
            if abs(x) + abs(y) < min_distance and abs(x) + abs(y) > 0:
                min_distance = abs(x) + abs(y)
    return min_distance

def parse_step(s):
    return (s[0], int(s[1::]))

def main():
    wire_1 = list(map(parse_step, input().split(',')))
    wire_2 = list(map(parse_step, input().split(',')))
    grid = {}
    fill_grid(grid, wire_1)
    fill_grid(grid, wire_2)
    print(find_closest_x(grid))

if __name__ == "__main__":
    main()