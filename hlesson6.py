import sys
letter=input("Input a character of your choice")
if len(letter)!=1:
    letter=input("Input only one character")
if len(letter)!=1:
    letter=input("Input only one character")
if len(letter)!=1:
    letter=input("Input only one character")
if len(letter)!=1:
    print("Stop inputting more than one character!:(")
    letter=input("Last try, input only one character")
if len(letter)!=1:
    sys.exit("This is because you didn't input only one character")

if letter.isalpha():
    print("Your character is a letter of the alphabet")
else:
    print("Your character is not a letter of the alphabet")