import sys

def process_input(q):
    index = 1
    s1 = q.pop(0).split(',')
    s2 = q.pop(0).split(',')
    print(s1)
    print(s2)
    print('last one', q.pop(0))

def main():
    q = []
    for s in sys.stdin:
        s = s.strip()
        q.append(s)
    process_input(q)

if __name__ == "__main__":
    main()