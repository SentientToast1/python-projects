
while True:
    bin = input("Enter binary: ")
    for x in bin:
        y = True
        if x == '0' or x == '1':
            pass
        else:
            y = False
    if y:
        break
    else:
        print("incorrect")



binList = [int(x) for x in bin]
compList = []
for x in range(len(binList)):
    compList.append(int(pow(2,x)))
compList.reverse()
sum = 0
for x in range(len(binList)):
    sum += compList[x] * binList[x]


print(f"Decimal is: {sum}")
