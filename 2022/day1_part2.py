import sys

def main():
    top_three = [0, 0, 0]
    total = 0
    for s in sys.stdin:
        if s != '\n':
            total += int(s)
        else:
            if total > min(top_three):
                top_three.remove(min(top_three))
                top_three.append(total)
            total = 0
    if total > min(top_three):
        top_three.remove(min(top_three))
        top_three.append(total)
    print(sum(top_three))

if __name__ == "__main__":
    main()