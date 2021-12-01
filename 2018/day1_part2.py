from itertools import cycle

def find_duplicate(changes):
    freq = 0
    freqs = set()
    for c in cycle(changes):
        freq += c
        if freq in freqs:
            return freq
        freqs.add(freq)

def get_changes():
    changes = []
    while True:
        try:
            changes.append(int(input()))
        except EOFError:
            break
    return changes

def main():
    print(find_duplicate(get_changes()))

if __name__ == "__main__":
    main()
