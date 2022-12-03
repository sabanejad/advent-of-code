import sys

def add_rows_columns(d, id, rows):
    columns = []
    for i in range(len(rows[0])):
        column = []
        for r in rows:
            column.append(r[i])
        columns.append(column)
    d[id] = rows + columns
    return d

def remove_number(number, boards, remaining_boards):
    remaining_boards_copy = remaining_boards.copy()
    for k in remaining_boards_copy:
        for l in boards[k]:
            l_copy = l.copy()
            for element in l_copy:
                if element == number:
                    l.remove(element)
                    if len(l) == 0 and remaining_boards != [] and k in remaining_boards:
                        remaining_boards.remove(k)
    return remaining_boards

def bingo(boards, last_board, number):
    return int(find_sum(boards, last_board)/2 * number)

def find_numbers(numbers, boards):
    remaining_boards = [k for k in boards.keys()]
    for number in numbers:
        remaining_boards = remove_number(number, boards, remaining_boards)
        if len(remaining_boards) == 1:
            last_board = remaining_boards[0]
        if remaining_boards == []:
            return bingo(boards, last_board, number)

def find_sum(boards, k):
    sum = 0
    for l in boards[k]:
        for element in l:
            sum += element
    return sum

def main():
    boards = {}
    id = 0
    rows = []
    for s in sys.stdin:
        # onto the next board
        if s == '\n':
            rows = []
            id += 1
        # add the bingo numbers
        elif id == 0:
            numbers = [int(n) for n in s.strip().split(',')]
        # add the rows
        else:
            rows.append([int(n) for n in s.strip().split()])
            boards = add_rows_columns(boards, id, rows)
    print(find_numbers(numbers, boards))

if __name__ == "__main__":
    main()