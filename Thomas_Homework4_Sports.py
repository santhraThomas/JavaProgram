"""
Program: Sports.py
Author: Santhra Thomas
Last date modified: 2/10/21
The purpose is to aread text file hw4 and create the following output:
Win - Loss record for the season to date
Average Score of Wayne State and opponents
Average winning margin
Average losing margin
Biggest win
Worst defeat.
"""
with open("hw4.txt", 'r') as fields:
    #Initialize variables
    counter = 0
    numLines = 0
    homeWin = 0
    homeLoss = 0
    sumHome = 0
    sumAway = 0
    sumHomeWin = 0
    sumHomeLoss = 0
    prevScore = 0
    previousScore = 0

    #Split the lines into different variables
    for line in fields:
        numLines += 1
        fields = line.split(":")
        date = fields[0]
        homeTeam = fields[1]
        homeScore= fields[2]
        awayTeam = fields[3]
        awayScore= fields[4]
        #print("Date : ", date, "Home Team : ", homeTeam, "Home Score: ", homeScore, "Away Team : ", awayTeam, "Away Score: ", awayScore)

        #While loop to count the number of win and loss of Home Team , record the total score of winning and loosing, and calculate big win and worst deafeat
        while counter < numLines:
            if homeScore > awayScore:
                counter += 1
                homeWin += 1
                sumHomeWin += int(homeScore) #Total winning score
                diffScore = int(homeScore) - int(awayScore) #Find the difference between the winning scores

                #Condition to compare the difference between current and previous score difference
                if (diffScore > prevScore): 
                    prevScore = diffScore #replace previous score difference with higher score difference value
                    bigWin = int(homeScore) #replace the bigWin with the score with highest difference
                    prev = int(homeScore) #records the score with highest difference to use later in else statement
                else:
                    bigWin = prev #saves the previous score with highest difference to bigWin
                    
            else:
                counter += 1
                homeLoss += 1
                sumHomeLoss += int(homeScore) #Total loosing score
                diffScore = int(awayScore) - int(homeScore) #Find the difference between the losing scores
                if (diffScore > previousScore):
                    previousScore = diffScore #replace previous score difference with higher score difference value
                    defeat = int(homeScore) #replace the defeat with the score with highest difference
                    previous = int(homeScore) #records the score with highest difference to use later in else statement
                else:
                    defeat = previous #saves the previous score with highest difference to defeat

        #Converting string to integer
        sumHome += int(homeScore)
        sumAway += int(awayScore)
        
        #Calculations
        avgHome = sumHome/numLines
        avgAway = sumAway/numLines
        avgWin = sumHomeWin/numLines
        avgLoss= sumHomeLoss/numLines     
        
    
    #Output statements
    print("Wayne state's win record: ", homeWin, "\nWayne State's loss record: ", homeLoss)
    print("Average score for WSU: "+ str(round(avgHome)), "\nAverage score for Others: "+ str(round(avgAway)))
    print("Average winning margin: "+ str(round(avgWin)), ", Average losing margin: "+ str(round(avgLoss)))
    print("Biggest Win : ", bigWin)
    print("Worst Defeat : ", defeat)
    
        
    
