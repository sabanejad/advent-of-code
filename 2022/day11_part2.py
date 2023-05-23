import sys

num_rounds = 10000
worry_levels = {}
rules = {}
division_test = {}
all_dividers = 1
conditions = {} # True, False
inspections = {}
max_inspection = 0
second_max_inspection = 0


def read_inputs():
    global all_dividers
    for s in sys.stdin:
        if s.startswith('Monkey '):
            monkey = s.strip().removeprefix('Monkey ').removesuffix(':')
        if s.startswith('  Starting items: '):
            worry_levels[monkey] = [int(e) for e in s.strip().removeprefix('Starting items: ').split(',')]
        if s.startswith('  Operation: new = '):
            rules[monkey] = s.strip().removeprefix('Operation: new = ').split()
        if s.startswith('  Test: divisible by '):
            division_test[monkey] = int(s.strip().removeprefix('Test: divisible by '))
        if s.startswith('    If true: throw to monkey '):
            true = s.strip().removeprefix('If true: throw to monkey ')
        if s.startswith('    If false: throw to monkey '):
            false = s.strip().removeprefix('If false: throw to monkey ')
            conditions[monkey] = (true, false)
    for val in division_test.values():
        all_dividers *= val


def execute_round():
    for monkey, list_of_items in worry_levels.items():
        for item in list_of_items:
            inspect(monkey)
            new_worry_level = execute_rule(item, rules[monkey]) % all_dividers
            true, false = conditions[monkey]
            if new_worry_level % division_test[monkey] == 0:
                worry_levels[true].append(new_worry_level)
            else:
                worry_levels[false].append(new_worry_level)
        worry_levels[monkey] = []
    return


def inspect(m):
    global max_inspection
    global second_max_inspection
    if m not in inspections: inspections[m] = 1
    else: 
        inspections[m] += 1
        if inspections[m] > max_inspection:
            max_inspection = inspections[m]
        elif inspections[m] > second_max_inspection:
            second_max_inspection = inspections[m]
    return


def execute_rule(worry_level, rules_for_monkey):
    if rules_for_monkey[1] == '*' and rules_for_monkey[2] == 'old':
        new_worry_level = worry_level * worry_level
    elif rules_for_monkey[1] == '+' and rules_for_monkey[2] == 'old':
        new_worry_level = worry_level + worry_level
    elif rules_for_monkey[1] == '*':
        new_worry_level = worry_level * int(rules_for_monkey[2])
    elif rules_for_monkey[1] == '+':
        new_worry_level = worry_level + int(rules_for_monkey[2])
    return new_worry_level


def main():
    read_inputs()
    for i in range(num_rounds):
        execute_round()
    print(max_inspection, second_max_inspection, max_inspection * second_max_inspection)
    

if __name__ == '__main__':
    main()