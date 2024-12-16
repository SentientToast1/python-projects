def prog1(n,m):
    length = len(str(m))

    prod=0
    for i in range(length,-1,-1):
        prod += (length-i)*(n*int(str(m)[i-1]))

    return prod

def prog2(n,m):
    prod = 0
    if n>m:
        for _ in range(m):
            prod+= n
    else:
        for _ in range(n):
            prod+= m
        
    return prod

x = int(input("Enter  first number: "))
y = int(input("Enter  second number: "))
choice = input("Enter choice of program: ")

while True:
    if choice == 'a':
        print(prog1(x,y))
        break
    elif choice == 'b':
        print(prog2(x,y))
        break
    else:
        print("wrong choice")