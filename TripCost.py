"""
Program: TripCost.py
Author: Santhra Thomas
Last date modified: 3/24/21
The purpose is to create a program that calculates a trip cost with information such as miles, and miles per gallon assuming $2.79 per gallon of gas.

"""
import sys #import statement needed to successfully terminate the program

#Function that calculates the trip cost
def FuelCost(miles,mpg):
    cost_per_gallon = 2.79 #Given value
    #Calculations
    distance = miles * 2
    totGallon = distance/ mpg
    roundTripCost = totGallon*2.79
    #Final print out statements
    print("Round trip total distance: ",distance, "miles")
    print("Round trip total gallons of gas needed: ", round(totGallon,2), "gallons")
    print("Cost per gallon is: $",cost_per_gallon)
    print("-------------------------------------------------")
    print("Your Round trip cost: $", round(roundTripCost,2))
    sys.exit() #Exits the program
    
choice = True
while(choice):
    print("Select a city to travel to:")
    print("i. Grand Rapids (156 miles)\nii. Petoskey, MI (269 miles)\niii. Marquette, MI (454 miles)\niv. Enter a city of your choosing")
    numChoice = True
    while(numChoice):
        try:#Try except will help to catch any values that are not numbers and give error message
            city = int(input("\nPlease choose 1,2,3,or 4 option from above: "))
            numChoice = False
        except:
            print("Please enter a number!")
    if(city == 1 or city == 2 or city == 3 or city == 4):#Condition to check if the options are chosen correctly
        if(city == 4):#Option that lets user inputs his/her city and miles information
            option = True
            while(option):
                city_of_choice = input("Please enter a city you choose to travel to: ")
                if city_of_choice.replace(' ', '').isalpha(): #Allows string with alphabets and white spaces in it
                    pick = True
                    while(pick):
                        try:#Try except will help to catch any values that are not numbers and give error message
                            miles = float(input("Please enter the miles from your place to this city: "))
                            pick = False
                        except:
                            print("Error please enter a number for miles!")
                    option = False
                    
                else:
                    print("Please enter a valid city name!")
                    
        elif(city == 1):
            miles = 156
            
        elif(city == 2):
            miles = 269
            
        else:
            miles = 454
        
        selection = True
        while(selection):
            print("Select a vehicle that you used to travel:")
            print("i. Chevy Volt (106 MPG)\nii. Chrysler Pacifica (28 MPG)\niii. Ford F150 (22 MPG)\niv. Enter the car of your choosing and include its MPG")
            numChoice2 = True
            while(numChoice2):
                try:
                    vehicle = int(input("\nPlease choose 1,2,3,or 4 option from above: "))
                    numChoice2 = False
                except:
                    print("Please enter a number!")
            if(vehicle == 1 or vehicle == 2 or vehicle == 3 or vehicle == 4):#Condition to check if the options are chosen correctly
                if(vehicle == 4):#Option that lets user inputs his/her vehicle info and its mpg
                    option = True
                    while(option):
                        vehicle_of_choice = input("Please enter a vehicle you choose to travel to: ")
                        if not all(x.isdigit() for x in vehicle_of_choice):#Checks if the string does not contain all numbers
                            if vehicle_of_choice.replace(' ', '').isalnum():#Allows string with alphabets and white spaces in it
                            
                                pick = True
                                while(pick):
                                    try:#Try except will help to catch any values that are not numbers and give error message
                                        mpg = float(input("Please enter the miles per gallon (MPG) of your vehicle: "))
                                        pick = False
                                    except:
                                        print("Error please enter a valid number for mpg!")
                            option = False
                        else:
                            print("Error!! Please enter the vehicle name with alphabets")
                        
                            
                elif(vehicle == 1):
                    mpg = 106

                elif(vehicle == 2):
                    mpg = 28

                else:
                    mpg = 22
                
                    
            
            FuelCost(miles, mpg) #returns the miles value and mpg value to the function called FuelCost
    else:
        print("Please enter a valid option")
        



        
                    
                    
        
