import random as rand
cash = []
player = []

def enterPlayer():
    name = input("Enter player name: ")
    player.append(name)
    cash.append(500)

while input("Add player? y/n ") != "n":
    enterPlayer()

def playGame():
    pool = 0
    bet = []
    guesses = []
    for x in range(len(player)):
        bet.append(int(input(f"enter bet {player[x]}: ")))
        cash[x] -= bet[x]
        pool+=bet[x]
    ans = rand.randint(1,50)
    for x in range(len(player)):
        guesses.append(int(input(f"{player[x]} enter guess: ")))
    

    for y in guesses:
        guesses[guesses.index(y)] = abs(y-ans)
    print(guesses)
    cash[guesses.index(min(guesses))] += pool
    
playGame()