import sys

def execute_offsets(l):
    i = 0
    step_cnt = 0
    while i < len(l):
        print(i, l[i], l)
        i += l[i]
        print(l)
        step_cnt += 1
        if i >= len(l):
            return step_cnt
        l[i] += 1
    return step_cnt

def main():
    offsets = []
    for s in sys.stdin:
        offsets.append(int(s.strip()))
    print(execute_offsets(offsets))

if __name__ == "__main__":
    main()