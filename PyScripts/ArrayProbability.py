print("Array Probability program")
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
