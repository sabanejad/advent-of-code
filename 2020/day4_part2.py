import re

def find_valid_passports(passports):
    valid_passport_count = 0
    for passport in passports:
        valid_num = 0
        for item in passport:
            code_id, code = item.split(':', 1)
            valid_num += valid.get(code_id, lambda code: False)(code)
        if valid_num == len(valid):
            valid_passport_count += 1
    return valid_passport_count

def min_max_pred(min_, max_, len_, code):
    return len(code) == len_ and code.isdigit() and min_ <= int(code) <= max_

def height_pred(code):
    unit = code[-2:]
    height = code[:-2]
    if unit == 'in':
        return min_max_pred(59, 76, 2, height)
    elif unit == 'cm':
        return min_max_pred(150, 193, 3, height)
    return False

valid = {
    'byr': lambda code: min_max_pred(1920, 2002, 4, code), 
    'iyr': lambda code: min_max_pred(2010, 2020, 4, code), 
    'eyr': lambda code: min_max_pred(2020, 2030, 4, code), 
    'hgt': height_pred,
    'hcl': lambda code: re.match('#[a-f0-9]{6}', code) is not None, 
    'ecl': lambda code: code in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}, 
    'pid': lambda code: min_max_pred(float('-inf'), float('+inf'), 9, code), 
}

def main():
    passports = []
    passport_data = []
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
    print(find_valid_passports(passports))

if __name__ == "__main__":
    main()