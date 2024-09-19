
    
        
        

def pgm1():
    choice = ''
    while choice != '0':
        x = int(input("Enter Num: "))
        flag = False
        for i in range(2,x):
                if x % i == 0:
                    flag = True
                    
        if flag:
            print("is composite")
        else:
            print("is prime")
        choice = input("Enter Choice:")


def pgm2():  
    numListStr = input("enter numbers separated by comma: ")

    numList=numListStr.split(',')
    countPrime = 0
    numList = list(map(int,numList))
    primeList= []
    compList = []
    print(numList)

    for i in numList:
        flag = False
        for j in range(2,i):
                if i % j == 0:
                    flag = True
                    
        if not flag:
            countPrime += 1
            primeList.append(i)
        else:
            compList.append(i)

    print(f"there are {countPrime} Prime numbers and {len(numList)-countPrime} composite numbers")
    print(f"list of primes: {primeList}" )
    print(f"list of composites: {compList}")
    
    
    
prgSelector = input()

if prgSelector == 0:
    pgm1()
elif prgSelector == 1:
    pgm2()
else:
    exit(0)
