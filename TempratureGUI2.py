"""
Program: TempratureGUI2.py
Author: Santhra Thomas
Last date modified: 4/14/21
The purpose is to ask the user for either to enter a choice between faherenheits or celcius to a text box.
Then the program converts the temprature to the other based on the option using the breezypythongui.
"""
from breezypythongui import EasyFrame
 
class Temprature(EasyFrame):
 
    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self,width="400", height = 200, title = "Temprature Converter") # Set up windo and widgets
       
        # Add the button group
        self.group = self.addRadiobuttonGroup(row = 0, column = 0)
 
        # Add the radio buttons to the group
        radioButton = self.group.addRadiobutton("Celsius")
        defaultRB = self.group.addRadiobutton("Fahrenheit")
        self.group["background"] = "#f8d002"
        radioButton["background"] = "#f8d002"
        defaultRB["background"] = "#f8d002"
        # Select one of the buttons in the group
        self.group.setSelectedButton(defaultRB)
 
        # Output field and display command button for the results
        dataPanel = self.addPanel(row = 3, column = 1,background = "#005a5e")
        self.output = self.addTextField("", row = 3, column = 1, width = 30, state = "readonly")
        dataPanel = self.addPanel(row = 0, column = 1,background = "#f8d002")
        displayButton = self.addButton("Display", row = 0, column = 1,
                       command = self.display)
        displayButton["foreground"] = "white"
        displayButton["background"] = "#003c6d"
        dataPanel = self.addPanel(row = 3, column = 0,background = "#005a5e")
        textLabel_1 = self.addLabel(text = "Selected Unit of Temparture : ", row = 3, column = 0, background = "#005a5e")
        textLabel_1["foreground"] = "white"

        # Label and field for the input temprature
        dataPanel = self.addPanel(row = 4, column = 0,background = "#005a5e")
        textLabel_2 = self.addLabel(text = "Enter the Temparture: ",row = 4, column = 0,background = "#005a5e")
        textLabel_2["foreground"] = "white"
        
        dataPanel = self.addPanel(row = 4, column = 1,background = "#005a5e")
        self.getinput = self.addFloatField(value = 0.0,row = 4,column = 1, width = 30)

        # Label and field for the output temprature and convert comand button for results
        dataPanel = self.addPanel(row = 5, column = 0,background = "#005a5e")
        dataPanel = self.addPanel(row = 5, column = 1,background = "#005a5e")
        convertButton = self.addButton("Convert", row = 5, column = 0, columnspan = 2, 
                       command = self.convert)
        convertButton["foreground"] = "#007e8a"
        convertButton["background"] = "white"
        dataPanel = self.addPanel(row = 6, column = 0,background = "#005a5e")
        textLabel_3 = self.addLabel(text = "Converted Temprature: ",row = 6, column = 0, background = "#005a5e")
        textLabel_3["foreground"] = "white"
        dataPanel = self.addPanel(row = 6, column = 1,background = "#005a5e")
        self.outputField = self.addFloatField(value = "",row = 6,column = 1, width = 30, state = "readonly")
 
    # Event handling method
 
    def display(self):
        """Displays the selected button's label in the text field."""
        self.output.setText(self.group.getSelectedButton()["value"])
    def convert(self):
        #Converts the current temprature to the temprature equivalent of the other temprature unit
        try:
            textTemp = self.output.getText()#Gets the input from the textfield
            str(textTemp)
            unitTemp = textTemp.lower()#Covert to lower case so it is easier to use the conditional operation
            temprature = self.getinput.getNumber()#Gets the value set for the temprature
            if(unitTemp == 'fahrenheit'):
                celcius = round(((temprature-32)*5/9),2)
                self.outputField.setValue(celcius)
            elif(unitTemp == 'celsius'):
                fahrenheit = round(((temprature*1.8)+32),2)
                self.outputField.setValue(fahrenheit)
            else:
                self.messageBox(title = "ERROR", message = "Please press the display button for the temprature unit")
            
        except:
            self.messageBox(title = "ERROR", message = "Please enter a valid temprature")
    
def main():
    Temprature().mainloop() #The program will loop 

if __name__ == "__main__":
    main()

