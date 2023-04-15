import sys
import string

char_to_height = dict(zip(string.ascii_lowercase, range(1, 27)))
char_to_height['S'] = 0
char_to_height['E'] = 27

def ingest_map():
    map = {}
    ns = 0
    for s in sys.stdin:
        ew = 0
        # width = len(list(s.strip()))
        for e in s.strip():
            # if e in string.ascii_lowercase:
            #     map[(ew, ns)] = char_to_height[e]
            if e == 'S':
                starting_loc = ew, ns
            #     map[(ew, ns)] = e
            elif e == 'E':
                destination_loc = ew, ns
            #     map[(ew, ns)] = e
            map[(ew, ns)] = e
            ew += 1
        ns += 1
    box = ew, ns
    return starting_loc, destination_loc, box, map

# def translate_map(map):
#     for k, v in map.items():


def navigate(starting_loc, destination_loc, box, map):
    possible_moves = {}
    width, height = box
    x1, y1 = starting_loc
    xt, yt = destination_loc
    # while 0 < i < depth and 0 < j < width:
    # if map(i, j): return

# def check_surrounding(coords, map):
#     """
#     checks all possible moves from coords and returns all viable 
#     next moves."""
#     i, j = coords
#     if i-1, j in map.keys():
#     if map[coords] == 'S':
#         return

def main():
    starting_loc, destination_loc, box, map = ingest_map()
    # print(map)
    # print(ingest_map())


if __name__ == "__main__":
    main()