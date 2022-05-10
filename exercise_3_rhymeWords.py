"""
    Escribir un programa que pida dos palabras y diga si riman o no. Si coinciden las tres ultimas letras tiene que decir que riman
    Si coinciden solo las dos ultimas, tiene que decir que riman un poco , y si no, no riman
    Source : https://pythondiario.com/2013/06/ejercicios-en-python-parte-3.html
    Student : Diego Ordonez
"""

def compareWords(word1,word2):
    
    reverse_word1 = word1[::-1]
    reverse_word2 = word2[::-1]
    rhym = 0
    res = ""
    for iter in range(3):
        
        if reverse_word1[iter] == reverse_word2[iter]:
            #print(f"{reverse_word1[iter]} := {reverse_word2[iter]} ")
            rhym += 1
            #print(f" count rhym :{rhym}")
    
    if rhym == 3:
        res = "riman"
    elif rhym == 2:
        res = "riman un poco"
    else:
        res = "no riman"
    return res
    
    

word1 = input("Introduce la primera palabra: ")
word2 = input("Introduce la segunda palabra: ")

comp = compareWords(word1,word2)

print(f"Las palabras: {word1} & {word2} : {comp}")