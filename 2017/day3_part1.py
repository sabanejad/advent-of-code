import sys
import math

ACCESS_PORT = 1

def spiral(n):
    """
    this function takes in an 'n' and returns the coords
    (x, y) of 'n' in the spiral below. the assumption
    here is that the center of the spiral, (0, 0) is 
    always 1. 

    17  16  15  14  13 ..
    18   5   4   3  12 29
    19   6   1   2  11 28
    20   7   8   9  10 27
    21  22  23  24  25 26

    numbers on the diagonal in the south-east direction
    are squares: 1, 9, 25, etc. each square is the right-most
    bottom-most element in the kth square where k is 
    sqrt(n) = 2k-1, k = (sqrt(n)+1)/2. values that are not 
    exact squares where, k < sqrt(n) < k+1, are on the kth square. 
    """
    # you're in the kth square, each square has 2k-1 elements on
    # each side. the squares are at (2k-3, -2k+3)
    k = math.ceil((math.sqrt(n)+1)/2)
    l = n - 1 - (2*k-3)**2
    q, r = divmod(l, 2*k-1)
    print(k, l, q, r)

def main():
    for s in sys.stdin:
        requested_square = int(s)
    spiral(requested_square)

if __name__ == "__main__":
    main()