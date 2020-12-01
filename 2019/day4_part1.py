
def valid_password(password):
    password_split = [int(item) for item in list(str(password))]
    if len(password_split) != 6:
        return False
    if not(password in range(100000, 1000000)):
        return False
    for a, b in zip(password_split, password_split[1::]):
        if a > b:
            return False
    if len(password_split) == len(set(password_split)):
        return False
    return True

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