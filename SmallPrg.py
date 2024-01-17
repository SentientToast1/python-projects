import random as rng
#__Program 1__
def ArrayProbability():
    array=[]
    arrayLen = int(input("Enter array length: "))
    if arrayLen != 0:
        for i in range(0 , arrayLen):
            inp = int(input(f"enter array element {i+1}: "))
            if(inp != 0):
                array.append(inp)
    else:
        print("OVERRIDE!")
        array = [14,3,5,2,5,6,12,67,12]
        arrayLen = len(array)

    print(f"your final array is: {array}")
    counter = 0
    numInput = int(input("Enter whose number probability to find: "))

    for i in array:
        if i == numInput:
            counter = counter  + 1
            
    if counter == 0:
        print("number not found")
    else:
        print(f"the probability of '{numInput}' is: {counter}/{arrayLen}")

#__Program 2__
def MarkList():   
    lis = []
    p = 0
    f = 0
    students = rng.randint(20,30)

    for i in range(0,students):
        a = rng.randint(1 , 100)
        lis.append((i,a))

    for j,k in lis:
        if k >= 50: 
            p+=1
        else:
            f+=1

    print(f"Passed: {p}\nFailed: {f}\nClass Of: {students}")
    cond = input("input 'Y' to see scores\n")

    if cond == "y" or cond == "Y":
        for m,n in lis:
            print(f"R.No: {m+1}, Marks: {n}/100\n--")
        else:
            exit()

#End of programs
























ProgramSelector  = int(input("Which program: "))

match ProgramSelector:
    case 1:
        ArrayProbability()
    case 2:
        MarkList()
    case _:
        print("invalid program")






