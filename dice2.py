from random import choices
ntrials = 15000
player1wins = 0
for i in range(ntrials-1):
    player2dice = choices(range(1, 7), k=2)
    player1dice = choices(range(1, 7), k=3)
    if player2dice[0] == player2dice[1] or player1dice.count(2)>1:
        continue
    player1dice.sort(reverse=True)
    if player2dice[0]+player2dice[1] < player1dice[0]+player1dice[1]:
        player1wins+=1
print("Ratio of player 1 wins =", player1wins/ntrials)
