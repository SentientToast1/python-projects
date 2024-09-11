import os

def Q1():
    
    
    basicPay = int(input("Enter Basic Salary: "))
    HRA = 0.1*basicPay
    TA= 0.05*basicPay

    print(f'Salary for the month\n------------------\nBasic Pay: {basicPay}\nHRA: {HRA}\nTA: {TA}\n------------------\nTotal: {basicPay+HRA+TA}')
    
def Q2():
    
    s4 = 'hello world1'
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
    print('Strawberry'.count('r'))
    print('hello'.encode("unicodebigunmarked"))
    print('h\te\tl\tl\to'.expandtabs(10))
    print('newer'.find('e'))
    a = {'x':'5','y':'6'}
    print("{x} is lesser than {y}".format_map(a))
    print('{0} {1}'.format(string,string2))
    print(s4.index('l'))
    print(s4.partition(' '))
    print(s4.rfind('l'))
    print(s4.rindex('o'))
    print('hello'.rjust(9,'@'))
    print(s4.rpartition('world'))
    print(s4.rsplit('l'))
    print('hello******'.rstrip('*'))
    print(s4.splitlines())
    #conditional methods
    print(s4.isalnum())
    print(s4.isalpha())
    print(s4.endswith('1'))
    print(s4.startswith('h'))
    print('1234'.isdecimal())
    print('1.24'.isdigit())
    print('1234hello'.isidentifier())
    print('President'.islower())
    print('president'.isupper())
    print('1.245'.isnumeric())
    print(''.isprintable())
    print('  '.isspace())
    print('Super Adventures'.istitle())


    
    
    
    
    
    
    
choice = int(input("enter: " ))
os.system('cls')
if not choice:
    Q1()
    
else:
    Q2()
