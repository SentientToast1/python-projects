PrgChoice = int(input("Enter Program Number: "))

match PrgChoice:
    case 1:
        with open("PyScripts\MarkList.py") as prg:
            exec(prg.read())
    case 2:
        with open("PyScripts\ArrayProbability.py") as prg:
            exec(prg.read())
    case 3:
        with open("PyScripts\Gacha.py") as prg:
            exec(prg.read())    