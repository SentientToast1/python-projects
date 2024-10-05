def prg1():
    inpListStr = input("enter data separated by comma: ")
    inpList=inpListStr.split(',')
    inpSet= set(inpList)
    print(inpSet)

def prg2():
    # Write a program that takes a string as input from the user and computes the frequency of each letter. Use a variable of dictionary type to maintain the count.
    inpListStr = input("enter string ")
    inpListStr.replace(" ", "")
    inpList=list(inpListStr.replace(" ", ""))
    inpSet = set(inpList)
    opDict = {}

    for x in inpSet:
        opDict.update({x:0})

    for y in inpList:
        opDict[y] += 1

choice = input("-:")

if choice == '1':
    prg1()
elif choice == '2':
    prg2()
else:
    exit()



