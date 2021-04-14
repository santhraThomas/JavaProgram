"""
Program: TaxGUI.py
Author: Santhra Thomas
Last date modified: 4/14/21
The tax program's purpose is to ask the user for yearly salary, number of dependents, and married or single?
The program will then calculate the amount owed by the user.
"""

from breezypythongui import EasyFrame
from tkinter import HORIZONTAL


class TaxCalculator(EasyFrame):

    def __init__(self):
        # Set up window and widgets
        EasyFrame.__init__(self,width="400", height = "200", title = "Tax Calculator") 
         
        # Set up the input labels, fields, Panels, and radio buttons
        dataPanel = self.addPanel(row = 0, column = 1, background = "#ff8700")
        inputLabel_1 = self.addLabel(text = "Enter your yearly salary: ", row = 0, column = 1, background = "#ff8700")
        inputLabel_1["foreground"] = "#040032" 
        dataPanel = self.addPanel(row = 0, column = 2, background = "#ff8700")
        self.inputField = self.addFloatField(value = 0.0, row = 0,
                                            column = 2, width = 30)
        dataPanel = self.addPanel(row = 2, column = 1, background = "#ff8700")
        inputLabel_2 = self.addLabel(text = "Enter the number of dependents: ", row = 2, column = 1, background = "#ff8700")
        inputLabel_2["foreground"] = "#040032"
        dataPanel = self.addPanel(row = 2, column = 2, background = "#ff8700")
        self.inputField1 = self.addIntegerField(value = 0, row = 2,
                                            column = 2, width = 30)
        #Add radio button group
        self.group = self.addRadiobuttonGroup(row = 3, column = 1,
                                              columnspan = 4, orient = HORIZONTAL)
        radiobutton1 = self.group.addRadiobutton(text = "Married")
        radiobutton2 = self.group.addRadiobutton(text = "Single")
        self.group.setSelectedButton(radiobutton1)

        #font color for the radio buttons
        self.group["background"] = "#ff8700"
        radiobutton1["foreground"] = "#040032"
        radiobutton1["background"] = "#ff8700"
        radiobutton2["foreground"] = "#040032"
        radiobutton2["background"] = "#ff8700"

        #Command button to calculate the tax
        dataPanel = self.addPanel(row = 4, column = 1, background = "#002a5f")
        dataPanel = self.addPanel(row = 4, column = 2, background = "#002a5f")
        calculateButton = self.addButton(text = "Calculate",row = 4, column = 1, columnspan= 2, command = self.convert)
        calculateButton["foreground"] = "#002a53"
        calculateButton["background"] = "white"
        

        # Set up the output labels, fields, and panels
        dataPanel = self.addPanel(row = 5, column = 1, background = "#002a5f")
        dataPanel = self.addPanel(row = 5, column = 2, background = "#002a5f")
        outputLabel = self.addLabel(text = "Tax payer owes : $", row = 5, column = 1, background = "#002a5f")
        outputLabel["foreground"] = "white"
        self.outputField = self.addFloatField(value = "", row = 5,
                                            column = 2, width = 30, state = "readonly")
        
    def convert(self):
        
        #Exception Handler if any Value Error(not a valid input type)
        try:
            salary = self.inputField.getNumber() #gets the variable stored for salary field
            dependent = self.inputField1.getNumber() #gets the variable stored for dependent
            radiobutton = (self.group.getSelectedButton()["value"]) #gets the selected button's label
            
            #variable initialization
            single = 6200 
            married = 9200
            # Condition will proceed if the user is married
            if (radiobutton == 'married'):
                totalDeductions = (dependent * 4500)+ married  #deduction calculation

                #Range of salaries to calculate gross income
                if salary > 180001:
                    gross_income = round((salary - totalDeductions)*.35,2)
                    self.outputField.setValue(gross_income)
                elif salary > 120000 :
                    gross_income = round((salary - totalDeductions)*.30,2)
                    self.outputField.setValue(gross_income)
                elif salary > 80001:
                    gross_income = round((salary - totalDeductions)*.25,2)
                    self.outputField.setValue(gross_income)
                elif salary > 50001:
                    gross_income = round((salary - totalDeductions)*.20,2)
                    self.outputField.setValue(gross_income)
                elif salary > 20001:
                    gross_income = round((salary - totalDeductions)*.15,2)
                    self.outputField.setValue(gross_income)
                elif salary > 0:
                    gross_income = round((salary - totalDeductions)*.10,2)
                    self.outputField.setValue(gross_income)
                else:#Error message if value is negative
                    self.messageBox(title = "ERROR", message = "Please enter a positive input for salary!!")
                
            #Condition will proceed if user is single
            else:
                totalDeductions = (dependent * 4500)+ single #deduction calculation

                #Range of salaries to calculate gross income
                if salary > 180001:
                    gross_income = round((salary - totalDeductions)*.35,2)
                    self.outputField.setValue(gross_income)
                elif salary > 120000 :
                    gross_income = round((salary - totalDeductions)*.30,2)
                    self.outputField.setValue(gross_income)
                elif salary > 80001:
                    gross_income = round((salary - totalDeductions)*.25,2)
                    self.outputField.setValue(gross_income)
                elif salary > 50001:
                    gross_income = round((salary - totalDeductions)*.20,2)
                    self.outputField.setValue(gross_income)
                elif salary > 20001:
                    gross_income = round((salary - totalDeductions)*.15,2)
                    self.outputField.setValue(gross_income)
                elif salary > 0:
                    gross_income = round((salary - totalDeductions)*.10,2)
                    self.outputField.setValue(gross_income)
                else: #Error message if value is negative
                    self.messageBox(title = "ERROR", message = "Please enter a value greater than zero for salary!!")
        except: #Error message dispayed if user inputs enters invalid variable type to the text fields
            errorBox_1 = self.messageBox(title = "ERROR", message = "Invalid input in the text fields above!!")
            errorBox_2 = self.messageBox(title = "ERROR", message = "Make sure no symbols used for text fields")     

         
def main():
    TaxCalculator().mainloop()#The program will loop 

if __name__ == "__main__":
    main()
