"""
Program: DiceRolling.py
Author: Santhra Thomas
Last date modified: 3/23/21
The purpose is to create a program that keep track of dice rolling portion and manipulate its results.

"""
import random #import to generate random numbers
import sys #import statement needed to successfully terminate the program

def RollDice(rolls):
    sumTotal = 0
    list_firstDice = []
    list_secondDice = []
    
    for i in range(0, rolls):
        
        #Generates random numbers from range 1 to 6 for each rolls for both dices.
        firstDice = random.randint(1, 6)
        secondDice = random.randint(1, 6)
        
        #Stores the total sum of each generated random numbers for both the dices to variable sumDice.
        sumDice = firstDice+secondDice

        #Calculate the total sum of the dice
        sumTotal += sumDice

        #Append 2 lists, with one containg the values of first dice and the other with second dice values
        list_firstDice.append(firstDice)
        list_secondDice.append(secondDice)
        print(firstDice,",",secondDice,"=",sumTotal)
    #print statement
    print("-------------------------------------------")
    print("Average number rolled",
          sumTotal, "/", rolls, "=", sumTotal/rolls) #Calculates the avg number rolled
    sys.exit() #Exits the program

choice = True #Initialization of while condition
while(choice):
    #The user is initially asked to choose how many times to roll a pair of dice (10,20 or 50)
    print("Roll Dice Program")
    print("Available number of rolls: 10, 20 & 50 ")
    rolls = int(input("How many rolls?: "))

    if(rolls == 10 or rolls == 20 or rolls == 50): #Condition applied when available number of rolls selected
        RollDice(rolls) #Returns the rolls value to the function RollDice
        
    else:
        #Error message displayed
        print("\nInvalid number of rolls!\n")
        
        

