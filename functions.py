
# Date : 25/04/2022
# Title : Learning python from scratch
# Author: Diego Ordonez

def numberComparation(number1,number2):
    if number1 > number2:
        print(f"Number: {number1} is greather than {number2}")
    elif number1 < number2:
        print(f"Number: {number2} is greather than {number1}")
    else:
        print(f"Numbers {number1} and {number2} are equals")

n1 = int(input("Introduzca el primer numero: "))
n2 = int(input("Introduza el sugundo numero: "))
print(f"Los numero son {n1} y {n2}")
numberComparation(n1,n2)