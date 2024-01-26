PrgChoice = int(input("Enter Program Number: "))
choice = ""
match PrgChoice:
    case 1:
        choice = "ArrayProbability.py"
    case 2:
         choice = "MarkList.py"
    case 3:   
         choice = "Gacha.py"

1
with open(f"Pyscripts/{choice}") as prg:
    exec(prg.read())