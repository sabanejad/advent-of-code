import sys

from itertools import combinations

def count_valid_passphrases(l, d=' '):
    cnt = 0
    for passphrase in l:
        if is_pass_phrase_valid(passphrase, d):
            cnt += 1
    return cnt

def is_pass_phrase_valid(passphrase, d):
    for (a, b) in combinations(passphrase.split(d), 2):
        if set(a) == set(b):
            return False & (len(set(passphrase.split(d))) == len(passphrase.split(d)))
    return True & (len(set(passphrase.split(d))) == len(passphrase.split(d)))

def main():
    passphrases = []
    for s in sys.stdin:
        passphrases.append(s.strip())
    print(count_valid_passphrases(passphrases))

if __name__ == "__main__":
    main()