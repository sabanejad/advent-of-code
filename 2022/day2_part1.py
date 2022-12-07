import sys

def calculate_score(a, b):
    score = outcome_of_game(a, b)
    if b == 'rock': score += 1
    if b == 'paper': score += 2
    if b == 'scissors': score += 3
    return score
        

def outcome_of_game(a, b):
    if a == b:
        return 3
    if a == 'rock':
        if b == 'scissors': return 0
        elif b == 'paper': return 6
    if a == 'paper':
        if b == 'rock': return 0
        elif b == 'scissors': return 6
    if a == 'scissors':
        if b == 'paper': return 0
        elif b == 'rock': return 6


def translate(s1, s2):
    if s1 == 'A': opponent = 'rock'
    if s1 == 'B': opponent = 'paper'
    if s1 == 'C': opponent = 'scissors'
    if s2 == 'X': me = 'rock'
    if s2 == 'Y': me = 'paper'
    if s2 == 'Z': me = 'scissors'
    return opponent, me

def main():
    score = 0
    for line in sys.stdin:
        s1, s2 = line.split()
        opponent, me = translate(s1, s2)
        score += calculate_score(opponent, me)
    print(score)


if __name__ == '__main__':
    main()
