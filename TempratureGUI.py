"""
Program: TempratureGUI.py
Author: Santhra Thomas
Last date modified: 3/31/21
The purpose is to ask the user for the temprature in Fahrenheits and display the result in Celcius using the breezypythongui.
"""
from breezypythongui import EasyFrame
from tkinter.font import Font
from tkinter import messagebox# Used this import for font and message box only


class TempratureCalculator(EasyFrame):

    def __init__(self):
        EasyFrame.__init__(self,width="550", height = 200, title = "Temprature Converter") # Set up windo and widgets

        # Label and field for the input
        dataPanel = self.addPanel(row = 0, column = 0,background = "#f8ffe3")
        textLabel = self.addLabel(text = "Enter the current temprature in Fahrenheit: ",row = 0, column = 0,background = "#f8ffe3")
        font = Font(family ="Verdana", size = 10,weight = "bold", slant = "italic")
        textLabel["font"] = font
        dataPanel = self.addPanel(row = 0, column = 1,background = "#f8ffe3")
        self.getinput = self.addFloatField(value = 0.0,row = 0,column = 1, width = 30)

        # Label and field for the output
        dataPanel = self.addPanel(row = 1, column = 0,background = "#f8ffe3")
        textLabel = self.addLabel(text = "Converted current temprature in Celcius: ",row = 1, column = 0, background = "#f8ffe3")
        font = Font(family ="Verdana", size = 10,slant = "italic", weight = "bold")
        textLabel["font"] = font
        dataPanel = self.addPanel(row = 1, column = 1,background = "#f8ffe3")
        self.output = self.addFloatField(value = 0.0,row = 1,column = 1, width = 30, state = "readonly")

        
        dataPanel = self.addPanel(row = 2, column = 0,background = "#007d76")
        dataPanel = self.addPanel(row = 2, column = 1,background = "#007d76")
        dataPanel = self.addPanel(row = 3, column = 0,background = "#007d76")
        dataPanel = self.addPanel(row = 3, column = 1,background = "#007d76")
        #The command button (Calculate)
        textLabel = self.addButton(text = "Calculate",row = 3, column = 0, columnspan= 2, command = self.convert)
        font = Font(family ="Verdana", size = 10,weight = "bold", slant = "italic")
        textLabel["font"] = font
        textLabel["foreground"] = "#007e8a"
        textLabel["background"] = "white"

    def convert(self):
        # Error Handling
        # Inputs the Fahrenheits value, and computes the Celcius, and outputs the result.
        try:
            fahrenheits = self.getinput.getNumber() #Gets the value set for the Fahrenheits
            if (fahrenheits == 0.0):
                #Prompt if the user failed to input a value or have the same value as the set value for the textfield
                response = messagebox.askyesno('Yes|No', "No change was made in Fahrenheits! \n\nDo you wish to proceed with already set value?")
                if (response == True):
                    celcius = round(((fahrenheits-32)*5/9),2) 
                    self.output.setValue(celcius) 
                else: #Error message if the user choose not to proceed with the set value
                    messagebox.showerror("Error", "Please enter a input you want to calculate")
            else:
                celcius = round(((fahrenheits-32)*5/9),2) #Calculations to convert from Fahrenheits to Celcius
                self.output.setValue(celcius) #set the output field with the value calculated
        except ValueError:
            # Display an error message when user input invalid value
            messagebox.showerror("Error", "Please enter a valid input!!")
            #self.messageBox(title = "ERROR", message = "Please enter a valid input!!") [This is to create a message box without using tkinter]
            

def main():
    TempratureCalculator().mainloop() #The program will loop 

if __name__ == "__main__":
    main()
