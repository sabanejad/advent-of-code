import sys

def eliminate(remove_digit, binaries, d):
    # removes elements with value
    # remove_digit in position d
    remove = set()
    for b in binaries:
        if int(b[d]) == remove_digit:
            remove.add(b)
    return binaries - remove

def count_digit(binaries, d):
    # counts digits at position d
    # and returns the most common
    ones = 0
    for b in binaries:
        if int(b[d]) == 1:
            ones += 1
    return ones >= len(binaries)/2

def main():
    binaries = set()
    for s in sys.stdin:
        binary = s.strip()
        binaries.add(binary)
    length = len(next(iter(binaries)))
    O2 = binaries.copy()
    CO2 = binaries.copy()
    for d in range(length):
        if(len(O2) != 1):
            remove_digit_o2 = count_digit(O2, d)
            O2 = eliminate(not remove_digit_o2, O2, d)
        if(len(CO2) != 1):
            remove_digit_co2 = count_digit(CO2, d)
            CO2 = eliminate(remove_digit_co2, CO2, d)
    print(int(CO2.pop(), 2) * int(O2.pop(), 2))

if __name__ == "__main__":
    main()