import re

def remove_invalid_passwords(l):
    valid = 0
    for i in l:
        first_p = int(i[0]) - 1
        second_p = int(i[1]) - 1
        char = i[2]
        password = i[3]
        if (password[first_p] == char) ^ (password[second_p] == char):
            valid += 1
    return valid

def main():
    l = []
    while True:
        try:
            l.append(re.split(' |-|: ', input()))
        except EOFError: 
            break
    print(remove_invalid_passwords(l))

if __name__ == "__main__":
    main()