# def square(n):
#     return n**2

# origList = list(map(int,input().split()))

# evenList = list(filter(lambda x : x%2==0,origList))

# squareList = list(map(square, evenList))
# print(f'Original list:\n{origList}')
# print(f'Even numbers list:\n{evenList}')
# print(f'Squares List:\n{squareList}')


# numbers = list(map(int, input().split()))
# triplets = [(a, b, c) for a in numbers for b in numbers for c in numbers]
# is_pythagorean = lambda triplet: triplet[0]**2 + triplet[1]**2 == triplet[2]**2
# valid_triplets = list(filter(is_pythagorean, triplets))
# print("Valid Pythagorean Triplets:", valid_triplets)

def getStr(prompt):
    while True:
        string = input(prompt)
        if string.isalpha():
            return string
        else:
            print("Name must be a string")

def getInt(prompt):
    while True:
        valI = input(prompt)
        try:
            return int(valI)
        except ValueError:
            print("age must be integer")

def getFloat(prompt,errmsg):
    while True:
        valF = input(prompt)
        try:
            return float(valF)
        except ValueError:
            print(errmsg)


name = getStr("Enter your name:")
sname = getStr("Enter your surname: ")
age = getInt("Enter age: ")
height = getFloat("Enter your height: ","height must be a float")
weight = getFloat("Enter your weight: ", "weight must be float")

print(f'Hello {name} {sname},')
print(f"your age is {age}, your height is {height} and your weight is {weight}")


