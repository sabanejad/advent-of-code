import 
  

def mix(l):
    element = l.pop(0)
    move_sec = []
    for i in range(element):
        move_sec.append(l.pop(0))
    take_step()

def take_step():
    return

def read_file():
    numbers = []
    for s in sys.stdin:
        numbers.append(int(s.strip()))
    return numbers

def main():
    numbers = read_file()
    mix(numbers)

if __name__ == "__main__":
    main()