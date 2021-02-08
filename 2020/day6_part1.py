def main():
    answers = []
    answer = set()
    unique_answers = 0
    while True:
        try:
            s = set(input())
            if s == set():
                answers.append(answer)
                unique_answers += len(answer)
                answer = set()
            else:
                answer = answer.union(s)
        except EOFError: 
            break
    answers.append(answer)
    unique_answers += len(answer)
    print(unique_answers)
    
if __name__ == "__main__":
    main()