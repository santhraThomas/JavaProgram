"""
Program: SubscriptionBill.py
Author: Santhra Thomas
Last date modified: 2/10/21
The purpose is to ask the user to enter the information on their subscription plan and output the bill.
The bill will be according to the type of service (basic or premium), if premium pay per view channels.
Both the service would have service tax and service pay along with a 10% increase if any past due balance.

"""
#Initializing variables
service = 'A'
bService = 6.50
pService = 9.25
validInput = 'False'

#Input statements
fName = input("Please enter your first name: ")
lName = input("Please enter your last name: ")

#while loop to ask user for the service type
while service != 'B' and service != 'b' and service != 'P' and service != 'p' : 
    service = input("What type of service do you have? (Basic $50 or Premium $90) \nEnter B for Basic or P for Premium Service:" )

if service == 'P' or service == 'p':
    
    #Loop will continue until the user input the correct input for the number of channels
    while validInput == 'False':
        
    #Dealing with literal errors using try and except method
        try:
            channels = int(input("How many pay per view channels do you have?($9.99 charged for a channel):"))
            validInput = 'True'
        except:
            print("That is not an Integer! Please enter an Integer")
            
    #Extra charge for channels calculations
    extra = channels * 9.99
    charge = 90.00 + extra + pService

    #Loop will continue until the user input the correct input for the past balance
    while validInput == 'True':

        #Dealing with literal errors using try and except method
        try:
            existingBalance = float(input("Any past balance? If so how much? If no balance then enter 0:"))
            validInput = 'False'
        except:
            print("That is not a number!! Please enter a number")
            
    #Premium service total calculations
    balance = existingBalance+(.10*existingBalance)
    total = charge + balance

    #Output of premium service charge
    print("\nHello,",fName, lName, "\nFollowing is your Subscription Bill:")
    print("\nPremium + ", channels, "extra channel(s) :\n$90 +", extra, pService, "(taxes) + ",
          existingBalance, "(existing balance)+(.10*existingBalance) = $", balance, ") = $"+ str(round(total,2)), "total balance due")
else:
    
    #Calculations for basic service
    charge = 50.00 + bService
    
    #Loop will continue until the user input the correct input for the past balance
    while validInput == 'False':

        #Dealing with literal errors using try and except method
        try:
            existingBalance = float(input("Any past balance? If so how much? If no balance then enter 0:"))
            validInput = 'True'
        except:
            print("That is not a number!! Please enter a number")

    #Basic service total calculations
    balance = existingBalance+(.10*existingBalance)
    total = charge + balance

    #Output of basic service charge
    print("\nHello,",fName, lName, "\nFollowing is your Subscription Bill:")
    print("\nBasic :\n$50.00 + $",bService, "(taxes) + ",
          existingBalance, "(existing balance)+(.10*existingBalance) = $", balance, ") = $"+ str(round(total,2)), "total balance due")


