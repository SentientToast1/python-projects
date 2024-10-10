n = int(input())

monList = []
timeList = []

while n != 0:
    tempList = list(map(int, input().split()))
    monList.append(tempList[0])
    timeList.append(tempList[1])
    
    n -= 1

optList = list(zip(monList, timeList))
optList.sort(key=lambda x : x[1])



m = int(input())
while m != 0:
    count = 0
    param = list(map(int , input().split()))
    for x in range(len(optList)):
        if param[1] >= optList[x][1] and param[0] >= optList[x][0]:
            print(f"{optList[x][0]} {optList[x][1]}")
            optList.pop(x)
            found = True
            break
        else:
            found = False
    if not found: print("None")
    m -= 1