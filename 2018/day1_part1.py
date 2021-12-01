def main():
    total = 0
    while True:
        try: 
            total += int(input())
        except EOFError:
            break
    print(total)

if __name__ == "__main__":
    main()