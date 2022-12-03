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

def find(numbers, boards):
    for n in numbers:
        for k in boards.keys():
            for l in boards[k]:
                for element in l:
                    if element == n:
                        l.remove(element)
                        if len(l) == 0:
                            return int((find_sum(boards, k) - element)/2 * n)

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
        if s == '\n':
            rows = []
            id += 1
        elif id == 0:
            numbers = [int(n) for n in s.strip().split(',')]
        else:
            rows.append([int(n) for n in s.strip().split()])
            boards = add_rows_columns(boards, id, rows)
    print(find(numbers, boards))

if __name__ == "__main__":
    main()