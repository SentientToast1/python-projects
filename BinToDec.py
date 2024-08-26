while True:
    binIn = input("Enter binary: ")
    if all(x in '01' for x in binIn):
        break
    else:
        print("Incorrect")



def BinToDec(binFunc):
    binList = [int(x) for x in binFunc]
    compList = []
    for x in range(len(binList)):
        compList.append(int(pow(2,x)))
    compList.reverse()
    sumBin = 0
    for x in range(len(binList)):
        sumBin += compList[x] * binList[x]
    return sumBin



print(f"Decimal is: {BinToDec(binIn)}")
