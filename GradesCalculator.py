"""
Program: GradesCalculator.py
Author: Santhra Thomas
Last date modified: 2/2/21
The purpose is to ask the instructor to input grades from recent test.
Display the average score, how many grades entered, and determine how many got A,B,C,D,or F.
When entered -1 the program is ended.
"""
#Initializing variables
score = 0
scoresEntered = 0
totScore = 0
scoreA = 0
scoreB = 0
scoreC = 0
scoreD = 0
scoreF = 0
avg = 0
#While loop condition
while score != -1:
    #Prompt asking user to input data
    score = float(input("Please enter a score between 0-100 or enter -1 to quit the program: "))
    if score != -1 and score >= 0 and score <= 100: #Condition to check if score is not sentinal value and in between 0 to 100
        totScore += score #Calculating total scores
        scoresEntered += 1 #Iteration to keep track of number of scores entered
        #Condition to check if which grade the entered score belong
        if score > 91:
            scoreA += 1
        elif score > 81:
            scoreB += 1
        elif score > 71:
            scoreC += 1
        elif score >= 60:
            scoreD += 1
        else:
            scoreF += 1
if scoresEntered !=0:
    # Calculation of average score
    avg = totScore/scoresEntered
    #Outputs to be printed
    print("Average score of the class is:" +str(round(avg,2)))
    print("Total number of grades enetered:", scoresEntered)
    print(scoreA, " recieved an A")
    print(scoreB, " recieved an B")
    print(scoreC, " recieved an C")
    print(scoreD, " recieved an D")
    print(scoreF, " recieved an F")
    
