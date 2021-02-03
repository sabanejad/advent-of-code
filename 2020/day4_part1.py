def find_valid_passports(passports, valid):
    valid_passport_count = 0
    for passport in passports:
        valid_num = 0
        for item in passport:
            code, _ = item.split(':', 1)
            if code in valid:
                valid_num += 1
        if valid_num == len(valid):
            valid_passport_count += 1
    return valid_passport_count

def main():
    passports = []
    passport_data = []
    valid = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    while True:
        try:
            s = input().split(' ')
            if s == ['']:
                passports.append(passport_data)
                passport_data = []
            else:
                passport_data.extend(s)
        except EOFError: 
            break
    passports.append(passport_data)
    print(find_valid_passports(passports, valid))

if __name__ == "__main__":
    main()