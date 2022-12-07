import sys

def calculate_score(outcome, my_move):
    if outcome == 'win': score = 6
    if outcome == 'draw': score = 3
    if outcome == 'lose': score = 0
    if my_move == 'rock': score += 1
    if my_move == 'paper': score += 2
    if my_move == 'scissors': score += 3
    return score

def pick_move(opponent, outcome):
    if outcome == 'draw': return opponent
    if opponent == 'rock':
        if outcome == 'lose': return 'scissors'
        elif outcome == 'win': return 'paper'
    if opponent == 'paper':
        if outcome == 'lose': return 'rock'
        elif outcome == 'win': return 'scissors'
    if opponent == 'scissors':
        if outcome == 'lose': return 'paper'
        elif outcome == 'win': return 'rock'

def translate(s1, s2):
    if s1 == 'A': opponent = 'rock'
    if s1 == 'B': opponent = 'paper'
    if s1 == 'C': opponent = 'scissors'
    if s2 == 'X': outcome = 'lose'
    if s2 == 'Y': outcome = 'draw'
    if s2 == 'Z': outcome = 'win'
    return opponent, outcome

def main():
    score = 0
    for line in sys.stdin:
        s1, s2 = line.split()
        opponent, outcome = translate(s1, s2)
        my_move = pick_move(opponent, outcome)
        score += calculate_score(outcome, my_move)
    print(score)

if __name__ == '__main__':
    main()