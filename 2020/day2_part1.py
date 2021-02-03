import re

def remove_invalid_passwords(passwords):
    valid = 0
    for entry in passwords:
        min_ = int(entry[0])
        max_ = int(entry[1])
        char = entry[2]
        password = entry[3]
        if min_ <= password.count(char) <= max_:
            valid += 1
    return valid

def main():
    passwords = []
    while True:
        try:
            passwords.append(re.split(' |-|: ', input()))
        except EOFError: 
            break
    print(remove_invalid_passwords(passwords))

if __name__ == "__main__":
    main()