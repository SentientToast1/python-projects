from color import colors
Programs = {
    1 : "ArrayProbability.py",
    2 : "MarkList.py",
    3 : "Gacha.py"
    
}
print(colors.cyan,"| Sr.no | Name")
for i in Programs:
    print(colors.cyan,f"|   {i}   | {Programs[i]}")
print()

choice = len(Programs) + 1
while choice > len(Programs): 
    choice = int(input("Enter Program Number: "))
    print("Wrong number")
with open(f"Pyscripts/{Programs[choice]}") as prg:
    exec(prg.read())

