import sys
import getpass

print("Welcome to Hangman \n Rules: \n 1)only Two players are allowed at the same time \n 2)The guesser only have 10 chances")

print("press quit to exit")

giveword = getpass.getpass("give a word to the guesser : ")

turns = 10

userchar = ''

while turns > 0:
    failchance = 0
    for char in giveword:
        if char in userchar:
            print(char)            
        else:
            print("__")
            failchance += 1
    if failchance == 0:
        print("you won")
        break
    usechr = input("guees the word :")
    userchar += usechr
    
    if usechr == 'quit':
        sys.exit("Mission failed!")
    
    if usechr not in giveword:  
        turns -= 1
        print("now you got only", turns, "turns left")
    
        if turns == 0:
            print("you loose")

    
    
  
