import sys

def find_marker(l, marker):
    for count in range(marker, len(l)):
        rolling_four = l[count-marker:count]
        rest = l[count:]
        if len(set(rolling_four)) == marker:
            return count
    

def main():
    files = []
    for s in sys.stdin:
        s = s.strip()
        if 'cd' in s:
            files[s[-1]] = 
        print(list(s.strip()))

if __name__ == "__main__":
    main()