import random as rand

player = [500,500,500]


while input("continue ") == "":
    pool=0
    bet = []
    guesses = []
    house = rand.randint(min(player),max(player))
    for x in range(len(player)):
        bet.append(int(input(f"enter bet {x}: ")))
        player[x] -= bet[x]
        
        pool+=bet[x]
    guess=rand.randint(1,6)
    for x in range(len(player)):

        guesses.append(int(input("enter guess: ")))

    for y in guesses:
        if y == guess:
           player[ guesses.index(y)] += pool+house
    print(f'the number was {guess} \nhouse buy in: {house}')
    for x in player:
        print(f'player {player.index(x)}: {x}')