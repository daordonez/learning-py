"""
Date : 26/04/2022
Author: Diego Ordonez
Title: Learning python form scratch
"""

#1. Escribir una función que devuelva el valor más alto de una lista que se le proporcione
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


words = [ "y","ocasion","ahora,","que","chuta","Zinchenko"]
print("longest word is: %s" % longestWord(words))