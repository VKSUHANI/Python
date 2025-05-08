from datetime import *
currentDate=(datetime.now()).date()
print(currentDate)
birthDate=input("Enter your birth date in YYYY-MM-DD format: ")
birthDate=datetime.strptime(birthDate, "%Y-%m-%d").date()
print(birthDate)
age=currentDate-birthDate
print("Your age is: ",age.days//365)