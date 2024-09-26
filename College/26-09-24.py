def prg1():
    In = input("-:")
    power = len(In)
    sum = 0
    for i in range(power):
        sum += int(In[i])**power

    if sum == int(In):
        print(f'{sum} is an armstrong number')
    else:
        print(f'{In} is not an armstrong number')

def prg2():
    string = input("enter string:")
    digits = []
    letters= []
    for i in string:
        if i.isdigit():
            digits.append(i)
        elif i.isalpha():
            letters.append(i)

    print(f"there are {len(digits)} digits in the string")
    print(f"there are {len(letters)} letters in the string")
    
print('Date: 26-09-24')
prgchoice = input("enter program numer: ")

if prgchoice == '1':
    prg1()
elif prgchoice == '2':
    prg2()
else:
    exit()









