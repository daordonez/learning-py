"""
    Date : 26/04/2022
    Author: Diego Ordonez
    Title: Learning python from scratch
"""

def palindrome(string):
    
    reversingWord = string[::-1]
    
    for index in range(len(string)):
        if string[index] == reversingWord[index]:
            isPalindrome = True
        else:
            isPalindrome = False
            break
    
    return isPalindrome


with open('palindromes.txt') as file:
    txtContent = file.read().splitlines()

for line in txtContent:
    print(line)
    r = palindrome(line)
    if r == True :
        print(f"## {line} is a palindrome")
    else:
        print(f"{line} is NOT a palindrome")