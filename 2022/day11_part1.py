import sys

num_rounds = 20
const_divider = 3
worry_levels = {}
rules = {}
division_test = {}
conditions = {} # True, False
inspections = {}
detail_print = False


def read_inputs():
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


def execute_round():
    for monkey, list_of_items in worry_levels.items():
        if detail_print: print(f'Monkey {monkey}:')
        for item in list_of_items:
            if detail_print: print(f'  Monkey inspects an item with a worry level of {item}.')
            inspect(monkey)
            new_worry_level = execute_rule(item, rules[monkey]) // const_divider
            if detail_print: print(f'    Monkey gets bored with item. Worry level is divided by {const_divider} to {new_worry_level}.')
            true, false = conditions[monkey]
            if new_worry_level % division_test[monkey] == 0:
                if detail_print:
                    print(f'    Current worry level is divisible by {division_test[monkey]}.')
                    print(f'    Item with worry level {new_worry_level} is thrown to monkey {true}.')
                worry_levels[true].append(new_worry_level)
            else:
                if detail_print:
                    print(f'    Current worry level is not divisible by {division_test[monkey]}.')
                    print(f'    Item with worry level {new_worry_level} is thrown to monkey {false}.')
                worry_levels[false].append(new_worry_level)
        worry_levels[monkey] = []
    return


def inspect(m):
    if m not in inspections: inspections[m] = 1
    else: inspections[m] += 1
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
    if detail_print: print(f'    Worry level is {rules_for_monkey[1]} by {rules_for_monkey[2]} to {new_worry_level}.')
    return new_worry_level


def get_two_biggest_inspections():
    num_inspections = list(inspections.values())
    biggest = max(num_inspections)
    num_inspections.remove(biggest)
    second_biggest = max(num_inspections)
    return biggest * second_biggest


def main():
    read_inputs()
    for i in range(num_rounds):
        execute_round()
    print(get_two_biggest_inspections())
    

if __name__ == '__main__':
    main()