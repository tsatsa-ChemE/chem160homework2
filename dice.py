from random import choices
ntrials = 15000
player1wins = 0
for i in range(ntrials):
    player2dice = choices(range(1, 7), k=2)
    if player2dice[0] == player2dice[1]:
        continue
    player1dice = choices(range(1, 7), k=3)
    player1dice.sort(reverse=True)
    if player2dice[0]+player2dice[1] < player1dice[0]+player1dice[1]:
        player1wins+=1
print("Ratio of player 1 wins =", player1wins/ntrials)