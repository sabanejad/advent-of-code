import re

def remove_invalid_passwords(passwords):
    valid = 0
    for entry in passwords:
        first_p = int(entry[0]) - 1
        second_p = int(entry[1]) - 1
        char = entry[2]
        password = entry[3]
        if (password[first_p] == char) ^ (password[second_p] == char):
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