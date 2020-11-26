def parser(l):
    for i in range(0, len(l)-3, 4):
        opcode = l[i]
        a = l[i+1]
        b = l[i+2]
        result = l[i+3]
        if opcode == 1:
            l[result] = l[a] + l[b]
        elif opcode == 2:
            l[result] = l[a] * l[b]
        elif opcode == 99:
            break
    return l[0]

def main():
    l = []
    l = list(map(int, input().split(',')))
    print(parser(l))

if __name__ == "__main__":
    main()