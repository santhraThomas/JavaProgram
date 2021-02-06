"""
Program: GrossWeeklyPay.py
Author: Santhra Thomas
Last date modified: 1/26/21
The purpose is to calculate the take home pay for an individual.
The program asks user information such as first name, hours worked during week, hourly rate, and overtime hours.
The program calculates the gross weekly pay and deduct the pay from the total of tax to display the take-home pay.
"""

#Setup the Constants
FICA = 0.062
MEDICARE_TAX = 0.0145
STATE_TAX = 0.0425
FEDERAL_TAX = 0.24
CITY_TAX = 0.009
PARK_TAX = 0.006

#Get input from User
fname = input("Please enter your first name: ")
hours = float(input("Please enter the number of hours you worked during the week: "))
rate = float(input("Please enter your hourly rate of pay $:"))
overTime = float(input("Please state your overtime working hours if any:"))

#Calculations of total tax
totalTax = FICA+MEDICARE_TAX+STATE_TAX+FEDERAL_TAX+CITY_TAX+PARK_TAX
grossIncome = (hours * rate) + (overTime * (rate * 1.5))
incomeTax = grossIncome * (totalTax)
takeHomePay = grossIncome - incomeTax

#Final display of the income tax
print("The gross weekly income is $" +str(round(grossIncome,2)))
print("Your take-home pay is $" +str(round(takeHomePay,2)))
