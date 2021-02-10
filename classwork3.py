"""
string = "Python be good"
strLeft = string.ljust(20,'*')#ljust - left justified
strRight = string.rjust(20,'-')#rjust - right justified
print(strLeft)
print(strRight)
print(string)

"""
"""
import datetime
string = "First Name"
string2 = "Last Name"
string3 = "Grade"

date1 = datetime.date.today()
strLeft = string.ljust(10)
strLeft = string.casefold()
strCenter = string2.center(20, '*')
strRight = string3.rjust(5)
print("date:", date1)
print(strLeft, strCenter, strRight)

"""
import datetime
date1 = datetime.date.today()
salesPrice = float(input("Please give me the salesPrice:"))
#Find a method that only will let the user input a number
print("price = {:.2f}".format(salesPrice))
