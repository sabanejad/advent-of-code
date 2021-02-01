def find_trees(l, right_step, down_step):
    x = 0
    y = 0
    tree_count = 0
    while y < len(l):
        if l[y][x] == '#':
            tree_count += 1
        y += down_step
        if y < len(l):
            x = (x + right_step) % len(l[y])
    return tree_count

def main():
    l = []
    overall_count = 1
    r = [1, 3, 5, 7, 1]
    d = [1, 1, 1, 1, 2]
    while True:
        try:
            l.append(list(input()))
        except EOFError: 
            break
    for r, d in zip(r, d):
        overall_count *= find_trees(l, r, d)
    print(overall_count)

if __name__ == "__main__":
    main()