from random import shuffle
def shuffler(MyList):
    shuffle(MyList)
    return MyList

Ball = ['','O','']

ShuffList = shuffler(Ball)


def PlayerGuess():

    guess = ''

    while guess not in ['0','1','2']:
        guess = input("Pick a number between 0-2: ")
    
    return int(guess)
pos=0
for x in range(len(ShuffList)):
    if ShuffList[x] == 'O':
        pos=x
    

if ShuffList[PlayerGuess()] == 'O':
    print("Correct")
else:
    print("Wrong")
    print(f'Ball was at position {pos}')

print(ShuffList)