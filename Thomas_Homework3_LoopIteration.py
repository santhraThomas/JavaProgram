"""
Program: LoopIteration.py
Author: Santhra Thomas
Last date modified: 2/2/21
The purpose is to loop through a list from 147 to 62 by iteration of -3 each time.
Printing out the number of times that program looped through along with ending number.
"""
# Initializing variables
startNum = 147
endNum = 62
counter = 0

# condition statements and while loop
while endNum <= startNum:
    startNum -= 3 #iteration
    #Condition Statement to make sure that startNum is not less than endNum
    if startNum >= endNum:
        # Printing output
        print("Your program has looped through ", counter, " times and your ending number is ", startNum)
        counter += 1 #Counter that keep track of the number of times the program looped
    else:
        break
   
    
