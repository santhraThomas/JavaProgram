"""
Program: CurrencyGUI.py
Author: Santhra Thomas
Last date modified: 4/7/21
The purpose is to ask the user for choose an international currency.
The user will enter an amount in that international currency and convert it to U.S. Dollars using tkinter.
"""

from breezypythongui import EasyFrame


class CurrencyCalculator(EasyFrame):

    def __init__(self):
        # Set up window and widgets
        EasyFrame.__init__(self,width="530", height = "200", title = "Currency Converter") 

        # Set up the list box
        self.listBox = self.addListbox(row = 0, column = 0, rowspan = 5)
         
        # Add some items to the list box
        self.listBox.insert(0, "Egyptian - Pound")
        self.listBox.insert(1, "Europe - Euro")
        self.listBox.insert(2, "South Korean - Won")
        self.listBox.insert(3,"Russian - Ruble")
        self.listBox.insert(4, "Indian - Rupee")
        
         
        # Set up the labels, fields, Panels, and buttons
        dataPanel = self.addPanel(row = 0, column = 1, background = "#f8ffe3")
        self.addLabel(text = "Enter the amount to convert", row = 0, column = 1, background = "#f8ffe3")
        dataPanel = self.addPanel(row = 0, column = 2, background = "#f8ffe3")
        self.getinput = self.addFloatField(value = "", row = 0,
                                            column = 2, width = 20)
        dataPanel = self.addPanel(row = 2, column = 1, background = "#f8ffe3")
        self.addLabel(text = "Amount in dollars: $", row = 2, column = 1, background = "#f8ffe3")
        dataPanel = self.addPanel(row = 2, column = 2, background = "#f8ffe3")
        self.output = self.addFloatField(value = "", row = 2,
                                            column = 2, width = 20, state = "readonly")
        dataPanel = self.addPanel(row = 3, column = 1, background = "#00a7a3")
        dataPanel = self.addPanel(row = 3, column = 2, background = "#00a7a3")
        self.addButton(text = "Convert", row = 3, column = 1, columnspan = 2, command = self.convert)
        
    def convert(self):
        # Error Handling
        try:
            amount = self.getinput.getNumber() #amount variable stores the amount to be converted
            if (amount >= 0): #Condition to chech if the user input positive value for money
                #index variable stores the index number of option the user chose
                index = self.listBox.getSelectedIndex() 
                """Condition to convert the international currency to dollars
                   (rounding by 2 decimals) using their assigned index number
                   Sets the converted value to the output field"""
                if index == 0:
                    dollars = round((amount * 1.374388),2)
                    self.output.setValue(dollars)
                elif index == 1:
                    dollars = round((amount * 1.187621),2)
                    self.output.setValue(dollars)
                elif index == 2:
                    dollars = round((amount * 0.000894),2)
                    self.output.setValue(dollars)
                elif index == 3:
                    dollars = round((amount * 0.012966),2)
                    self.output.setValue(dollars)
                elif index == 4:
                    dollars = round((amount * 0.013448),2)
                    self.output.setValue(dollars)
                else:
                    #Error message if user failed to choose an international currency from ListBox
                    self.messageBox(title = "ERROR", message = "Please choose a currency!!") 
            else:
                #Error message if user failed to enter a positive number for the amount to be converted field
                self.messageBox(title = "ERROR", message = "Please enter a positive input!!") 
        except ValueError:
            # Display an error message when user input invalid value
            self.messageBox(title = "ERROR", message = "Please enter a valid input!!") 
        
         
def main():
    CurrencyCalculator().mainloop()#The program will loop 

if __name__ == "__main__":
    main()
