from math import floor

def fuel_per_mass(mass): 
    return floor(mass / 3) - 2

def main():
    total = 0
    while True:
        try: 
            total += fuel_per_mass(int(input()))
        except EOFError:
            break
    print(total)

if __name__ == "__main__":
    main()