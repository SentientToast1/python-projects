import random as rng

print("-----Mark List Program-----")
print("")
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
