from math import ceil
import re

def find_seat_ids(seats):
    seat_ids = []
    for seat in seats:
        m = re.fullmatch('([FB]{7})([RL]{3})', seat)
        if m:
            row_code = m[1]
            column_code = m[2]
        seat_ids.append(which_index(row_code, 'B', 0, 127) * 8 + which_index(column_code, 'R', 0, 7))
    seat_ids.sort()
    return seat_ids

def which_seat_id(seat_ids):
    for i in range(len(seat_ids) - 1):
        if seat_ids[i + 1] - seat_ids[i] != 1:
            return seat_ids[i + 1] - 1

def which_index(code, upper_half, min_, max_):
    if min_ == max_:
        return min_
    char = code[0]
    if char == upper_half:
        min_ += ceil((max_ - min_) / 2)
    else:
        max_ -= ceil((max_ - min_) / 2)
    return which_index(code[1:], upper_half, min_, max_)

def main():
    seats = []
    while True:
        try:
            seats.append(input())
        except EOFError:
            break
    print(which_seat_id(find_seat_ids(seats)))

if __name__ == "__main__":
    main()
