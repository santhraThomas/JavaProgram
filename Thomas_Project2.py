'''
Program: Project2.py
Author: Santhra Thomas
Last date modified: 2/26/21

This project is based on games crap. 
'''
import random      
import sys

choice = True
dollar = 100
betMoney = 0
valid = True
betChoice = True
bet = True
wager_input = True
while(choice):
    status = input("Press any key if you wish to play game or press 'N' if you wish to leave")
    if status.lower() != 'n':
        dollar -= 5
        while(betChoice):
            print("Which value you want to bet on:\nEnter 1 to bet on 4 \nEnter 2 to bet on 5 \nEnter 3 to bet on 6 \nEnter 4 to bet on 8 \nEnter 5 to bet on 9 \nEnter 6 to bet on 10")
            print("Enter 7 to bet on double 2 \nEnter 8 to bet on double 3 \nEnter 9 to bet on double 4 \nEnter 10 to bet on double 5")
            try:
                betValue = int(input("Enter your chosen bet from above: "))
                if (betValue < 1 or betValue > 10):
                    print("Enter a valid value between 1-10: ")
                else:
                    while (valid):
                        betMoney = int(input("How much you want to bet from 1-5? "))
                        try:
                            if (betMoney >= 1 and betMoney <= 5):
                                dollar -= betMoney
                                bet_choice = input("Press 'P' to bet on PASS line or press 'D' to bet on DON'T PASS line: ")
                                if bet_choice.lower() == 'p' or bet_choice.lower() == 'd':
                                    choice = input("Press any key to roll the dice: ")
                                    die1 = random.randrange(1,7)
                                    die2 = random.randrange(1,7)
                                    totSumDice = die1 + die2
                                    print("Result of dices: ", dices, "=",  totSumDice)
                                    if bet_choice.lower() == 'p':
                                        if (betValue == 1 and totSumDice == 4)or(betValue == 2 and totSumDice == 5)or(betValue == 3 and totSumDice == 6)or(betValue == 4 and totSumDice == 8)or(betValue == 5 and totSumDice == 9) or(betValue == 6 and totSumDice == 10):
                                            print("You won the PASS Line Side Bet!!")
                                            dollar = dollar + (2*betMoney)
                                        elif (betValue == 7 and totSumDice == 4 and die1 == die2):
                                            print("You won the PASS Line Side Bet for doubles!!")
                                            dollar = dollar + (7*betMoney)
                                        elif (betValue == 8 and totSumDice == 6 and die1 == die2):
                                            print("You won the PASS Line Side Bet for doubles!!")
                                            dollar = dollar + (7*betMoney)
                                        elif (betValue == 9 and totSumDice == 8 and die1 == die2):
                                            print("You won the PASS Line Side Bet for doubles!!")
                                            dollar = dollar + (9*betMoney)
                                        elif (betValue == 10 and totSumDice == 10 and die1 == die2):
                                            print("You won the PASS Line Side Bet for doubles!!")
                                            dollar = dollar + (9*betMoney)
                                        else:
                                            print("You lose the bet and lost your money")
                                            dollar -= betMoney
                                            print("Your remaining money: ", dollar)
                                    else:
                                        if (betValue == 1 and totSumDice != 4)or(betValue == 2 and totSumDice != 5)or(betValue == 3 and totSumDice != 6)or(betValue == 4 and totSumDice != 8)or(betValue == 5 and totSumDice != 9) or(betValue == 6 and totSumDice != 10):
                                            print("You won the Don't PASS Line Side Bet!!")
                                            dollar = dollar + (2*betMoney)
                                        elif (betValue == 7 and totSumDice == 4 and die1 != die2):
                                            print("You won the Don't PASS Line Side Bet for doubles!!")
                                            dollar = dollar + (7*betMoney)
                                        elif (betValue == 8 and totSumDice == 6 and die1 != die2):
                                            print("You won the Don't PASS Line Side Bet for doubles!!")
                                            dollar = dollar + (7*betMoney)
                                        elif (betValue == 9 and totSumDice == 8 and die1 != die2):
                                            print("You won the Don't PASS Line Side Bet for doubles!!")
                                            dollar = dollar + (9*betMoney)
                                        elif (betValue == 10 and totSumDice == 10 and die1 != die2):
                                            print("You won the Don't PASS Line Side Bet for doubles!!")
                                            dollar = dollar + (9*betMoney)
                                        else:
                                            print("You lose the bet and lost your money")
                                            dollar -= betMoney
                                            print("Your remaining money: ", dollar)
                                    if (totSumDice == 7 or totSumDice == 11):
                                        print("You won!!")
                                        dollar = dollar + betMoney

                                    elif(totSumDice == 2 or totSumDice == 3 or totSumDice == 12):
                                        print("You lost!!")
                                        print("Game Over!!")
                                        print("Remaining coins: ", dollar)
                                        cont = input("Do you wish to continue? Press any key for Yes or 'N' for no")
                                        if cont.lower() == 'n':
                                            sys.exit()
                                        else:
                                            valid = False
                                    else:
                                        point = totSumDice
                                        print("Your point is", point)
                                        die1 = random.randrange(1,7)
                                        die2 = random.randrange(1,7)
                                        totSumDice = die1 + die2
                                        while(wager_input):
                                            wager_input = input("Would you like to place a wager? Press any key to place a wager or Press 'N' to not: ")
                                            if wager_input.lower() != 'n':
                                                if dollar > 0:
                                                    wager = True
                                                    betChoice = True
                                                    while(betChoice):
                                                        print("Which value you want to bet on:\nEnter 1 to bet on 4 \nEnter 2 to bet on 5 \nEnter 3 to bet on 6 \nEnter 4 to bet on 8 \nEnter 5 to bet on 9 \nEnter 6 to bet on 10")
                                                        print("Enter 7 to bet on double 2 \nEnter 8 to bet on double 3 \nEnter 9 to bet on double 4 \nEnter 10 to bet on double 5")
                                                        betValue = int(input("Enter your chosen bet from above: "))
                                                        try:
                                                            if (betValue < 1 or betValue > 10):
                                                                print("Enter a valid value between 1-10: ")
                                                            else:
                                                                sideBetChoice = True
                                                                while(sideBetChoice):
                                                                    sideBet = int(input("How much you want to bet from 1-5? "))
                                                                    if (sideBet < 1 or sideBet > 5):
                                                                        print("Enter a side bet value between 1-5: ")
                                                                    elif (sideBet >=1 and sideBet<= 5):
                                                                        dollar = dollar - sideBet
                                                                        if(dollar < 0):
                                                                            print("Insufficient amount for betting! Remaining money: ", dollars)
                                                                            sys.exit()
                                                                        else:
                                                                            if totSumDice == 7:
                                                                                print("You lost all your side bets")
                                                                                dollar - sideBet
                                                                                sideBet = 0
                                                                                print("Remaining dollars : ", dollar)
                                                                            elif totSumDice == 4 or totSumDice == 5 or totSumDice == 6 or totSumDice == 8 or totSumDice == 9 or totSumDice == 10:
                                                                                if (betValue == 1 and totSumDice == 4)or(betValue == 2 and totSumDice == 5)or(betValue == 3 and totSumDice == 6)or(betValue == 4 and totSumDice == 8)or(betValue == 5 and totSumDice == 9) or(betValue == 6 and totSumDice == 10):
                                                                                    print("You won the PASS Line Side Bet!!")
                                                                                    dollar = dollar + (2*betMoney)
                                                                                    sideBetChoice = False
                                                                                    betChoice = False
                                                                                elif (betValue == 7 and totSumDice == 4 and die1 == die2):
                                                                                    print("You won the PASS Line Side Bet for doubles!!")
                                                                                    dollar = dollar + (7*betMoney)
                                                                                    sideBetChoice = False
                                                                                    betChoice = False
                                                                                elif (betValue == 8 and totSumDice == 6 and die1 == die2):
                                                                                    print("You won the PASS Line Side Bet for doubles!!")
                                                                                    dollar = dollar + (7*betMoney)
                                                                                    sideBetChoice = False
                                                                                    betChoice = False
                                                                                elif (betValue == 9 and totSumDice == 8 and die1 == die2):
                                                                                    print("You won the PASS Line Side Bet for doubles!!")
                                                                                    dollar = dollar + (9*betMoney)
                                                                                    sideBetChoice = False
                                                                                    betChoice = False
                                                                                elif (betValue == 10 and totSumDice == 10 and die1 == die2):
                                                                                    print("You won the PASS Line Side Bet for doubles!!")
                                                                                    dollar = dollar + (9*betMoney)
                                                                                    sideBetChoice = False
                                                                                    betChoice = False
                                                                                else:
                                                                                    print("You lose the bet and lost your money")
                                                                                    dollar -= betMoney
                                                                                    print("Your remaining money: ", dollar)
                                                                                    remain = input("Do you wish to continue? Press any key for Yes or 'N' for no")
                                                                                    if remain.lower() == 'n':
                                                                                        sys.exit()
                                                                                    else:
                                                                                        sideBetChoice = False
                                                                            else:
                                                                                print("Enter a valid side bet!")
                                                        except:
                                                            print("Enter a valid bet choice!") 
                                                else:
                                                    print("Not enough money to side bet")
                                                    sys.exit()
                                            else:
                                                if totSumDice == point:
                                                    print("You won!!")
                                                elif totSumDice == 7:
                                                        print("You lost!!")
                                                        print("Remaining dollars : ", dollar)
                                                        sys.exit()
                                                else:
                                                    die1 = random.randrange(1,7)
                                                    die2 = random.randrange(1,7)
                                                    totSumDice = die1 + die2
                                else:
                                    print("Enter a valid bet choice")
                            else:
                                print("Error not a valid value between 1-5!")
                        except:
                            print("Enter a valid bet money")
                        
                    valid = False
            except:
                print("Enter a valid bet value!")
    else:
        choice = False
        sys.exit()
                
