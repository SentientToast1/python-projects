
while True:
    bin = input("Enter binary: ")
    count = 0
    for x in bin:
        if x == '0' or x == '1':
            count = 0
        else:
            count += 1
    if count != 0:
        print("incorrect")
    else:
        break



binList = [int(x) for x in bin]
compList = []
for x in range(len(binList)):
    compList.append(int(pow(2,x)))
compList.reverse()
sum = 0
for x in range(len(binList)):
    sum += compList[x] * binList[x]


print(f"Decimal is: {sum}")