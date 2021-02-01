import re

def remove_invalid_passwords(l):
    valid = 0
    for i in l:
        _min = int(i[0])
        _max = int(i[1])
        char = i[2]
        password = i[3]
        if _min <= password.count(char) <= _max:
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