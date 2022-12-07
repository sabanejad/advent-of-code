import re
import sys
import string

def parse_input():
    piles = {}
    moves = []
    switch = False
    for s in sys.stdin:
        if switch:
            moves.append(parse_moves(s))
        elif s == '\n': switch = True
        else:
            l = list(s)[1::4]
            for i in range(len(l)):
                if l[i] in string.ascii_uppercase:
                    if i+1 in piles.keys(): piles[i+1].append(l[i])
                    else: piles[i+1] = [l[i]]
    for k, v in piles.items():
        piles[k].reverse()
    return piles, moves

def parse_moves(s):
    return tuple([int(x) for x in re.findall(r'\d+', s)])

def make_moves(piles, moves):
    for m in moves:
        how_many, from_pile, to_pile = m
        for n in range(how_many):
            element = piles[from_pile].pop()
            piles[to_pile].append(element)
    return piles

def get_final_string(piles):
    s = ''
    for i in range(1, len(piles)+1):
        s += piles[i].pop()
    return s

def main():
    piles, moves = parse_input()
    piles = make_moves(piles, moves)
    print(get_final_string(piles))

if __name__ == "__main__":
    main()