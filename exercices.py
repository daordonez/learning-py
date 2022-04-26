# Date : 25/04/2022
# From : https://pythondiario.com/2013/05/ejercicios-en-python-parte-1.html
# Student : Diego Ordonez

"""
# Definir una fauncion que obtenga el numero mas grande de 2
def maxNumber(number1, number2):
    if number1 > number2:
        return number1
    elif number1 < number2:
        return number2
    else:
        return number1 #equals
    
#n1 = int(input("Enter first number: "))
#n2 = int(input("Enter second number: "))
#result = maxNumber(n1,n2)
#print(f"The greathest number is: {result}")


#Definir una funcion que obtenga el numero mas grande de 3
def max_of_three(number1,number2,number3):
    #compare if there are some equal
    if number1 != number2 != number3:
        temp_number = maxNumber(number1,number2)
        return maxNumber(temp_number,number3)
    else:
        if number1 == number2:
            return maxNumber(number2,number3)
        elif number1 == number3:
            return maxNumber(number1,number2)
        elif number2 == number3:
            return maxNumber(number1,number3)


#n1 = int(input("enter first number: "))
#n2 = int(input("enter second number: "))
#n3 = int(input("enter third number: "))

#result = max_of_three(n1,n2,n3)
#print(f"The greathest of the three is: {result}")

#Definir una funcion que calcule la longitud de una lista o cadena dada

def stringLenght(str):
    count = 0
    for i in str:
        count += 1
    return count


#result = stringLenght(input("Enter an string: "))
#print ({result})

#Escribir una funcion que devuelva si una letra dada es una vocal

def isVocal(letter):
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        return True
    elif letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
        return True
    else:
        return False

#letter = input("enter a letter: ")
#if isVocal(letter):
#   print("isVocal")
#else:
#   print("NO is vocal")

#ejercicio 5
def sumCollection(list):
    store = 0
    for element in list:
        store += element
    
    return store

def multip(list):
    store = 1
    
    for element in list:
        store *= element
    return store

sumate = [1,2,3,4,5]
multiplicate = [1,2,3,4]

#result = sumCollection(sumate)
#result_m = multip(multiplicate)

#print(result)
#print(result_m)

# 6. Escribir una función que calcule la cadena inversa

def reverseStrings(toReverse):
    long = stringLenght(toReverse)
    reverse = ""
    negative = -1
    index = 1
    
    while index <= long:
        zIndex = index * negative
        reverse += toReverse[zIndex]
        index += 1
                
    return reverse

#__reverse = reverseStrings(input("Enter an String: "))
#print(__reverse)
"""
# 7. Definir una función que determine si una palabra es Palindromo
def reverseStrings(toReverse):
    long = len(toReverse)
    reverse = ""
    negative = -1
    index = 1
    
    while index <= long:
        zIndex = index * negative
        reverse += toReverse[zIndex]
        index += 1
                
    return reverse


def palindrome(string):
    
    reversingWord = reverseStrings(string)
    
    for index in range(0,len(string)):
        if string[index] == reversingWord[index]:
            isPalindrome = True
        else:
            isPalindrome = False
            break
    
    

str = input("Enter a word: ")
palindrome(str)