def fill_grid(grid, l):
    x = 0
    y = 0
    path = 0
    for item in l:
        direction = item[0]
        steps = item[1]
        if direction == 'U':
            for i in range(y, y + steps):
                grid[x, i] = path
                path += 1
            y = y + steps
        elif direction == 'R':
            for i in range(x, x + steps):
                grid[i, y] = path
                path += 1
            x = x + steps
        elif direction == 'D':
            for i in range(y, y - steps, -1):
                grid[x, i] = path
                path += 1
            y = y - steps
        elif direction == 'L':
            for i in range(x, x - steps, -1):
                grid[i, y] = path
                path += 1
            x = x - steps
    grid[x, y] = path

def find_best_path_x(grid_1, grid_2):
    min_path = float('inf')
    intersections = grid_1.keys() & grid_2.keys()
    for value in intersections:
        path = grid_1[value] + grid_2[value]
        if path < min_path and path > 0:
            min_path = path
    return min_path

def parse_step(s):
    return (s[0], int(s[1::]))

def main():
    wire_1 = list(map(parse_step, input().split(',')))
    wire_2 = list(map(parse_step, input().split(',')))
    grid_1 = {}
    grid_2 = {}
    fill_grid(grid_1, wire_1)
    fill_grid(grid_2, wire_2)
    print(find_best_path_x(grid_1, grid_2))

if __name__ == "__main__":
    main()