
def Q1():
    #Write a Python program that takes a string from the user, removes all vowels from the string, extracts the remaining letters, and sorts them in alphabetical order. The program should then print the sorted letters as a list.
    string = input('Enter your string: ').lower()
    vowels = {
        'a' : '',
        'e' : '',
        'i' : '',
        'o' : '',
        'u' : '',
        ' ': ''
    }
    transtable = string.maketrans(vowels)
    string2 = list(string.translate(transtable))
    string2.sort()
    print(string2)

def Q2():
    #Write a Python program that takes a list of words from the user, identifies and removes any words that are palindromes (words that read the same backward as forward), and then sorts the remaining words in reverse alphabetical order. The program should finally print the updated list as a tuple.
    pass
    string = input('Enter words with commas: ')
    stringList = string.rsplit(',')
    filteredList=[]
    print(stringList)
    for i in stringList:
        if i != i[::-1]:
            filteredList.append(i)





Q2()