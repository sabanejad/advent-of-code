import sys

def same_halfway_around_check(l):
    """
    this function finds the sum of all digits that match 
    the next digit in the list. The list is circular, so 
    the digit after the last digit is the first digit in 
    the list.
    """
    _sum = 0
    for i in range(len(l)):
        if l[i]==l[(i+len(l)//2)%len(l)]: _sum+=l[i]
    return _sum

def main():
    for s in sys.stdin:
        l = [int(i) for i in list(s.strip())]
        print(same_halfway_around_check(l))

if __name__ == "__main__":
    main()