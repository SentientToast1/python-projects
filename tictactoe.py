import os
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
def printBoard(turn):
    os.system('cls')
    for i in range(9):
        print(board[i]) if (i+1) % 3 == 0 else print(board[i],end="|")
    print(f"\tTurn: {turn}")

def place(turn):
    while True:
        try:
            loc = int(input("Enter position: "))
            if not (1 <= loc <= 9):
                print("out of range!")
                continue
            elif board[loc - 1] != ' ':
                print("spot taken!")
                continue

            break
        except ValueError:
            input("not a number!")
    if turn % 2 == 0:
        board[loc - 1] = 'O'
    else:
        board[loc - 1] = 'X'

def won():
    if board[0] == board[1] == board[2] != ' ' or board[3] == board[4] == board[5] != ' ' or board[6] == board[7] == board[8] != ' ':
        return True
    elif board[0] == board[3] == board[6] != ' ' or board[1] == board[4] == board[7] != ' ' or board[2] == board[5] == board[8] != ' ':
        return True
    elif board[0] == board[4] == board[8] != ' ' or board[2] == board[4] == board[6] != ' ':
        return True
    

# main
turn = 1
while not won() and turn < 10:
    place(turn)
    printBoard(turn)
    turn += 1
os.system('cls')
if turn % 2 == 0 and turn < 10:
    print("Player 1 has won! ")
elif turn % 2 != 0 and turn <10:
    print("Player 2 has won!")
else:
    print("Tie!")