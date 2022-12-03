import sys
import collections

def get_gamma_epsilon(d, count):
    gamma = ''
    epsilon = ''
    od = collections.OrderedDict(sorted(d.items()))
    for v in od.values():
        if v > count-v:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    return int(gamma, 2) * int(epsilon, 2)

def main():
    count_ones = {}
    count = 0
    for s in sys.stdin:
        count += 1
        binary = [int(d) for d in list(s.strip())]
        for i, d in enumerate(binary):
            if d == 1:
                count_ones[i] = count_ones.get(i, 0) + 1
    print(get_gamma_epsilon(count_ones, count))

if __name__ == "__main__":
    main()