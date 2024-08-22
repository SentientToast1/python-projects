while True:
    binIn = input("Enter binary: ")
    if all(x in '01' for x in binIn):
        break
    else:
        print("Incorrect")



def BinToDec(bin):
    binList = [int(x) for x in bin]
    compList = []
    for x in range(len(binList)):
        compList.append(int(pow(2,x)))
    compList.reverse()
    sum = 0
    for x in range(len(binList)):
        sum += compList[x] * binList[x]
    return sum



print(f"Decimal is: {BinToDec(binIn)}")
