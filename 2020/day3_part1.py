def find_trees(map_, right_step, down_step):
    x = 0
    y = 0
    tree_count = 0
    while y < len(map_):
        if map_[y][x] == '#':
            map_[y][x] = 'X'
            tree_count += 1
        else:
            map_[y][x] = 'O'
        y += down_step
        x = (x + right_step) % len(map_[0])
    return tree_count

def main():
    map_ = []
    while True:
        try:
            map_.append(list(input()))
        except EOFError: 
            break
    print(find_trees(map_, 3, 1))

if __name__ == "__main__":
    main()