def parser(l):
    dummy = l.copy()
    for i in range(0, len(dummy)-3, 4):
        opcode = dummy[i]
        a = dummy[i+1]
        b = dummy[i+2]
        result = dummy[i+3]
        if a < len(dummy) and b < len(dummy) and result < len(dummy):
            if opcode == 1:
                dummy[result] = dummy[a] + dummy[b]
            elif opcode == 2:
                dummy[result] = dummy[a] * dummy[b]
            elif opcode == 99:
                break
    return dummy[0]

def checker(l, output):
    for noun in range(100):
        for verb in range(100):
            l[1] = noun
            l[2] = verb
            if parser(l) == output:
                return 100 * noun + verb

def main():
    l = []
    l = list(map(int, input().split(',')))
    output = 19690720
    print(checker(l, output))

if __name__ == "__main__":
    main()