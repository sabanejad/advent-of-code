from math import ceil
import re

def highest_seat_id(seats):
    highest_seat = 0
    for seat in seats:
        m = re.fullmatch('([FB]{7})([RL]{3})', seat)
        if m:
            row_code = m[1]
            column_code = m[2]
        seat_id = which_index(row_code, 'B', 0, 127) * 8 + which_index(column_code, 'R', 0, 7)
        if seat_id > highest_seat:
            highest_seat = seat_id
    return highest_seat

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
    print(highest_seat_id(seats))

if __name__ == "__main__":
    main()
