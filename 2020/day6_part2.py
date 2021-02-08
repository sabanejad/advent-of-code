def find_overlaps(answers):
    overlap = 0
    for answer in answers:
        intersection = set.intersection(*answer)
        overlap += len(intersection)
    return overlap

def main():
    answers = []
    answer = []
    while True:
        try:
            s = set(input())
            if s == set():
                answers.append(answer)
                answer = []
            else:
                answer.append(s)
        except EOFError: 
            break
    answers.append(answer)
    print(find_overlaps(answers))
    
if __name__ == "__main__":
    main()