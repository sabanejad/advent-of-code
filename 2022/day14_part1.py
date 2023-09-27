import sys

coors = []
board = {}
entry_point = (500, 0)
x_entry, y_entry = entry_point
min_x = 493 # assuming from looking at input, make this programmatic
max_x = 506
min_y = 0
max_y = 10
num_sand_drops = 45


def read_input():
    for line in sys.stdin:
        l = []
        for c in line.strip().split(' -> '):
            l.append(tuple(int(coor) for coor in c.split(',')))
        coors.append(l)


def fill_board():
    for line in coors:
        for (x1, y1), (x2, y2) in zip(line[:-1], line[1:]):
            if x1 == x2 and y1 > y2:
                # going up
                for y in range(y2, y1+1):
                    board[x1, y] = '#'
            elif x1 == x2 and y1 < y2:
                # going down
                for y in range(y1, y2+1):
                    board[x1, y] = '#'
            elif y1 == y2 and x1 > x2:
                # going left
                for x in range(x2, x1+1):
                    board[x, y1] = '#'
            else:
                # going right
                for x in range(x1, x2+1):
                    board[x, y1] = '#'
    board[entry_point] = '+'


def print_board():
    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            if (x, y) in board: print(board[x, y], end='')
            else: print('.', end='')
        print()


def drop_sand(x=x_entry, y=y_entry):
    # (x, y) is where the grain is, (~x, y+1) is where it's going
    if x == min_x or x == max_x or y == max_y: return 'overflow'
        # board[x, y] = '~'
    # if x < min_x or x > max_x or y > max_y
    elif (x, y+1) not in board: drop_sand(x, y+1)
    elif (x-1, y+1) not in board: drop_sand(x-1, y+1)
    elif (x+1, y+1) not in board: drop_sand(x+1, y+1)
    else: board[x, y] = 'o'


def main():
    read_input()
    fill_board()
    num_sands = 1
    # s = drop_sand(x=492, y=2)
    # print(s)
    # while True:
    #     s = drop_sand()
    #     if s == 'overflow':
    #         print(num_sands)
    #         break
    #     num_sands += 1
    for i in range(num_sand_drops):
        print(num_sands)
        print(drop_sand())
        num_sands += 1
        print_board()


if __name__ == '__main__':
    main()
