def find_trees(map_, right_step, down_step):
    x = 0
    y = 0
    tree_count = 0
    while y < len(map_):
        if map_[y][x] == '#':
            tree_count += 1
        y += down_step
        x = (x + right_step) % len(map_[0])
    return tree_count

def main():
    map_ = []
    overall_count = 1
    right = [1, 3, 5, 7, 1]
    down = [1, 1, 1, 1, 2]
    while True:
        try:
            map_.append(list(input()))
        except EOFError: 
            break
    for r, d in zip(right, down):
        overall_count *= find_trees(map_, r, d)
    print(overall_count)

if __name__ == "__main__":
    main()