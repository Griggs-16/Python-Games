from random import randint
import sys

print("Welcome to rock, paper and scissors game \n")

print("Rules: \n 1)Only two players are allowed at the same time \n 2)Rock can defeat scissors, paper can defeat rock and scissors can defeat paper \n So, its all about luck \n")

player = True

selectf = ['rock', 'paper', 'scissors']

comp = selectf[randint(0, 2)]

turns = 3

while player == True:
    player = input("Enter your Chance :")
    
    if player == comp:
        print("tie")
    elif player == 'rock':
        if comp == 'scissors':
            print("comp selects", comp, "you win")
        else:
            print("computer selects", comp, "you loose")
            turns -= 1
    elif player == 'paper':
        if comp == 'rock':
            print("comp selects", comp, "you win")
        else:
            print("comp selects", comp, "you loose")
            turns -= 1
    elif player == 'scissors':
        if comp == 'paper':
            print("comp selects", comp, "you win")
        else:
            print("comp selects", comp, "you loose")
            turns -= 1
    else:
        
        print("invalid input")
        
    player = True
   
    if turns == 0:
        sys.exit("Good game try again later")
    
            
            
            
    