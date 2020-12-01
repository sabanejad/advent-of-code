# two adjacent matching digits are not part 
# of a larger group of matching digits
def two_repeats(password_split):
    for a, b in zip(password_split, password_split[1::]):
        if a == b and password_split.count(a) == 2:
            return True
    return False

def valid_password(password):
    password_split = [int(item) for item in list(str(password))]
    # six-digit number
    if len(password_split) != 6:
        return False
    # never decreasing
    for a, b in zip(password_split, password_split[1::]):
        if a > b:
            return False
    return True and two_repeats(password_split)

def num_valid_passwords(password_range):
    start = int(password_range[0])
    end = int(password_range[1])
    num = 0
    for i in range(start, end+1):
        if valid_password(i):
            num += 1
    return num

def main():
    password_range = input().split('-')
    print(num_valid_passwords(password_range))

if __name__ == "__main__":
    main()