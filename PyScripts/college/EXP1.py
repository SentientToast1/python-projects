import os

def Q1():
    
    
    basicPay = int(input("Enter Basic Salary: "))
    HRA = 0.1*basicPay
    TA= 0.05*basicPay

    print(f'Salary for the month\n------------------\nBasic Pay: {basicPay}\nHRA: {HRA}\nTA: {TA}\n------------------\nTotal: {basicPay+HRA+TA}')
    
def Q2():
    
    
    string = "Python Programming" #a
    print(string[15]) #b
    print(f'length of string is: {len(string)}') #c
    print(string[0:6]) #d
    print(string[2:4]+string[15:18]) #e
    print(string.upper()) #f
    string2 = "is interesting"
    print(string+" "+string2) #g
    
    #methods
    print(string2.replace("interesting", "pineapple"))
    print('-'.join(string2))
    string3 = "   BLABLABLALBLA"
    string3 = string3.lstrip()
    print(string3.ljust(25,'.'))
    print(string3.lower())
    dicti = {
        "y":"z",
        "m":""
        
    }
    table = string.maketrans(dicti)
    print(string.translate(table))
    string4= "the ballad of buckravers"
    print(string4.capitalize())
    print(string4.title())
    print(string3.casefold())
    print(string2.zfill(24))
    print(string.swapcase())
    print('00000helloworlds000000'.strip('0'))
    print('hello'.center(7,'#'))
    
    
    
    
    
    
    
    
    
choice = int(input("enter: " ))
os.system('cls')
if not choice:
    Q1()
    
else:
    Q2()
    
    
    
    
    
    
    
