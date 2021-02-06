"""
Program: TripCost.py
Author: Santhra Thomas
Last date modified: 1/26/21
The purpose is to calculate how much a trip would cost when the gas price per gallon is $2.21
The user enters both mpg of their car and miles they are planning to travel. 
"""

# Setup Constants
GALLONS_PRICE = 2.21
#Get input from User
mileage = float(input("Please state the gas milage of your car (mpg): "))
miles = float(input("Please state how far are you plan on traveling in miles: "))

#Calculation of the expenses on the trip
expense = (miles / mileage) * GALLONS_PRICE

#Output of the result of how much the trip will cost to the user
print("Your trip would cost $" + str(round(expense, 2)))
