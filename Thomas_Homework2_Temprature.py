"""
Program: Temprature.py
Author: Santhra Thomas
Last date modified: 1/26/21
The purpose is to ask the user for the temprature in Fahrenheits and display the result in Celcius.
"""
#Get input from the user
fahrenheits = float(input("Please enter the temprature in Fahrenheits: "))

#Calculation to convert fahrenheints to celcius
celcius = ((fahrenheits-32)*5/9)

#Display the message that tells the user the temprature in Celcius
print("The temprature in Celcius is: "+str(round(celcius,2)))
