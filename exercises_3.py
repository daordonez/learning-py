#2. Juego de Master Mind
# - Debe solicitar primero la longitud de la cadena
# - se debe ir solicitando números para que se compruebe que si ha acertado con la cadena

import random

def masterMind(long):
    
    startN = 10**(long - 1)
    endN = (10**long) - 1
    
    masterNumber = random.randint(startN,endN)
    
    return masterNumber

print("##################################")
print("MASTER MIND")
print("##################################")

attempts = 5
isGuessed = False
userDefsLong = int(input("Enter long number: ")) 
base = str(masterMind( userDefsLong ))
userInput = input("Try to guess the number: ")

#La cadena introducida es más grand que la longitud máxima
if userInput == base:
    print(f"You're a true MASTER MIND, you're right in the first attempt!, number was: {base}")
else:
    
    while (attempts > 1) and (isGuessed == False):
        
        if len(str(userInput)) > userDefsLong:
            attempts -= 1
            print(f"Given number has a greather lenght that you defined. Attempts remaining:{attempts}")
            userInput = input("Try to guess the number: ")
            
        else:
            if userInput == base:
                print(f"You guessed the number!. Number was: {base}")
                isGuessed = True
            else:
                #Si el número base contiene números de los que el usuario a introducido contamos cuantos son
                countHits = 0
                
                #De los numeros introducidos cuantos son correctos
                for num in base:
                    if num in userInput:
                        countHits +=1
                attempts -= 1
                print(f"With {userInput} you have guessed {countHits} numbers. Attempts remaining:{attempts} ")
                userInput = input("Try to guess the number: ")
        
    if isGuessed == False:
        print(f"You lose :( Number was: {base}")
            
