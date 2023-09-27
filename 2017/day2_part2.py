import sys

def mod_result(l):
    i = 0
    while i < len(l):
        j = i+1
        while j < len(l):
            if l[i] % l[j] == 0:
                return l[i] // l[j]
            elif l[j] % l[i] == 0:
                return l[j] // l[i]
            j += 1
        i += 1

def main():
    _sum = 0
    for s in sys.stdin:
        l = [int(i) for i in s.strip().split('	')]
        _sum += mod_result(l)
    print(_sum)

if __name__ == "__main__":
    main()