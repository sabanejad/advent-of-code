import sys

def get_dir_size(k, files):
    size = 0
    for a, b in files[k]:
        if a == 'dir':
            if k != '/':
                size += get_dir_size(k + '/' + b, files)
            else:
                size += get_dir_size(k + b, files)
        else:
            size += int(a)
    return size

def read_input():
    files = {}
    loc = ''
    for s in sys.stdin:
        s = s.strip().split()
        if 'cd' in s:
            if s[-1] == '..':
                    l = loc.split('/')
                    loc = '/'.join(l[:-1])
                    if loc == '':
                        loc = '/'
            else: 
                if loc != '' and loc[-1] != '/':
                    loc = loc + '/' + s[-1]
                else: 
                    loc = loc + s[-1]
        if '$' not in s:
            if loc not in files.keys():
                files[loc] = [tuple(s)]
            else:
                files[loc].append(tuple(s))
    return files

def main():
    files = read_input()
    sizes = {k: get_dir_size(k, files) for k in files.keys()}
    delete = 30000000 - (70000000 - sizes['/'])
    min_delete = float('inf')
    for v in sizes.values():
        if v > delete and v < min_delete:
            min_delete = v
    print(min_delete)

if __name__ == "__main__":
    main()