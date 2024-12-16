
n = int(input("Enter first number: "))
m = int(input("Enter second number: "))
length = len(str(m))

prod=0
for i in range(length,-1,-1):
    prod += (length-i)*(n*int(str(m)[i-1]))

print(prod)