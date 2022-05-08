"""
Date : 26/04/2022
Author: Diego Ordonez
Title: Learning python form scratch
"""

#1. Escribir una función que devuelva el valor más alto de una lista que se le proporcione
import string
import this


def max_list(nums):
    swift = True
    while swift:
        swift = False
        for e in range(len(nums) - 1):
            #Si lo que hay en la primera posición es más grande que lo que hay en la segunda, cambialos de posición
            if nums[e] > nums[e + 1]:
                #lo que habia en la segunda posición mueble a la primera
                # y lo que había en la primera posición ( el numero más grande) envialo a la segúnda posición
                nums[e], nums[e + 1] = nums[e + 1], nums[e]
                swift = True
                
    return nums[-1]

#list = [1,9,8,3,5,6]

#print (list)
#print ("########")
#print(max_list(list))

#2. Escribir una función que determina cual es la palabra más larga que se le ha pasado en un listado de palabras

def longestWord(wordList):
    
    swift = True
    
    while swift:
        swift = False
        #e will be the iterator
        for e in range(len(wordList) - 1):
            #if lenght of first word is greather tan second, then push it them to end
            if len(wordList[e]) > len(wordList[e + 1]):
                #both changes must be at the same time
                wordList[e], wordList[e + 1] = wordList[e + 1], wordList[e]
                swift = True
    
    return wordList[-1]


words = [ "y","ocasion","ahora","que","chuta","Zinchenko"]
#print("longest word is: %s" % longestWord(words))

#3. Escribir una función filtrar_palabras que tome una lista de palabras y un entero n, y devuelva las palabras que tengan mas de n caracteres


def wordsFilter(words, charsNumber):
    
    wordsFound = []
    
    for word in words:
        if len(word) > charsNumber:
            wordsFound.append(word)
    
    return wordsFound

#print(wordsFilter(words, 4))


# 4. Escribir una función que pregunte al usuario para que ingrese una cadena. La respuesta debe evaluar la cadena y decir cuantas letras en mayuscula tiene

def upperCaseDetector(word: string):
    
    uperCaseFound = 0
    
    for chr in word:
        if chr.isupper():
            uperCaseFound += 1
    
    return uperCaseFound


"""
res = upperCaseDetector(input("Enter a word: "))

if res > 0:
    print(f"Given word has {res} capital letters(s)")
else:
    print("No capital letters found")
"""

# 5. Construir un programa que convierta numers binarios a enteros

def convertFromBin(binary):
    return int(binary,2)


#res = convertFromBin(input("enter binary value: "))
#print(f"Integer value is: {res}")

#6. Escribr un programa donde se ingrese el año en curso. Se ingrese el nombre y el año de nacimiento de 3 personas y se calcule cuantos años cumple cada persona durante el año en curso
# IMPORTANTE : la forma de acceder a un diccionario se basa en asignar valores ( nombre que queramos) a los valores key-value del diccionario


def getMyBirthDay(currentYear,peopleBirthYear):
    
    for name,year in peopleBirthYear.items():
        thisYears = currentYear - year
        print(f"{name} will be {thisYears} years old this year")

people = {
    'Diego' : 1991,
    'Alejandro': 1988,
    'Albert' : 1987
}

#getMyBirthDay(2022,people)

#7. Definir una tupla con las edades de 10 personas. Imprimir la cantidad de personas con edades superiores a 20 años

def aboveTwentyYearsOld (tuple):
    totalAboveTwenty = 0
    
    for val in tuple:
        if val > 20:
            totalAboveTwenty += 1
    
    return totalAboveTwenty


thisYears = (4,21,19,16,40,4)

""" 
totalY = aboveTwentyYearsOld(thisYears)
print(f"Values are: {thisYears}")
print(f"There are {totalY} value above 20 in the given list.")
"""

#8. Definir en una lista un conjunto de nombres, e imprimir la cantidad de nombres que comienzan por la letra B

def charInFinder(nameList,char):
    
    for word in nameList:
        if char in word:
            print(f"{word} contains {char}")

""" 
nameList = ['Juan','Susana','Elizabet','Noelia','Federico','Carlos']
charInFinder(nameList,(input("Enter char to find: ")))
"""

#9. Crear una función que cuente vocales, donde el usuario sea el que especifique la palabra

def getVowel(word):
    count = 0
    vowels = "aeiou"
    
    for letter in word:
        if letter.lower() in vowels:
            count += 1
    
    return count
    

""" 
reslt = getVowel(input("Enter a word: "))
print(f"{reslt} vowels found")
"""


#10. calcular si un año es biciesto o no

def isLeapYear(year):
    isleap = False
    
    if ((year % 4) == 0) and ((year % 100) != 0):
        isleap = True
    
    return isleap


thisYear = int(input("Enter a year to test: "))

if isLeapYear(thisYear):
    print(f"{thisYear} IS LEAP")
else:
    print(f"{thisYear} is NOT leap")