import sys

def find_marker(l, marker):
    for count in range(marker, len(l)):
        rolling_four = l[count-marker:count]
        rest = l[count:]
        if len(set(rolling_four)) == marker:
            return count
    

def main():
    for s in sys.stdin:
        print(find_marker(list(s), 14))

if __name__ == "__main__":
    main()