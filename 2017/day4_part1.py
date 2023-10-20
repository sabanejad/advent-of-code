import sys

def count_valid_passphrases(l, d=' '):
    cnt = 0
    for passphrase in l:
        if len(set(passphrase.split(d))) == len(passphrase.split(d)):
            cnt += 1
    return cnt

def main():
    passphrases = []
    for s in sys.stdin:
        passphrases.append(s.strip())
    print(count_valid_passphrases(passphrases))

if __name__ == "__main__":
    main()