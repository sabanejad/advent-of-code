def find_trees(l, right_step, down_step):
    x = 0
    y = 0
    tree_count = 0
    while y < len(l):
        if l[y][x] == '#':
            l[y][x] = 'X'
            tree_count += 1
        else:
            l[y][x] = 'O'
        y += down_step
        if y < len(l):
            x = (x + right_step) % len(l[y])
    return tree_count

def main():
    l = []
    while True:
        try:
            l.append(list(input()))
        except EOFError: 
            break
    print(find_trees(l, 3, 1))

if __name__ == "__main__":
    main()