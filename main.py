from functools import partial
from select import select
from sqlite3 import TimeFromTicks
from time import time
from pip import main


class User():
    interest = 15
    
    # first method for user details
    def __init__(self):   
        self.name = input('Enter yor Name:')
        self.age = input('Enter your Age:')
        self.gender = input('Enter your Gender:')
    
    # show user details
    def show_details(self):
        print("Personal Details :")
        print(" ")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
    
    # select duration for loan amoung the options availaable
    def duration(self):
        print("Please select your duration from the following:")
        print("1. 2 Years")
        print("2. 3 Years")
        print("3. 4 Years")
        print("")

        user_input = int(input())
        if user_input == 1:
            self.time = 2

        elif user_input == 2:
            self.time = 3

        elif user_input == 3:
            self.time = 4
        else:
            print("Invalid")
            quit()
    
    # request the amount
    def amount(self):
        amount = int(input('Enter the amount to be borrowed: '))
        self.borrow = amount

    # method for amount to be repaid
    def repay(self):
        print("The Final amount to be paid after time" ,self.time, "years is Rupees :")
        print (self.borrow + (self.borrow*self.time*self.interest)/100) 

# Main part for calling the methods
# first is general intro in short though
print("")
print("Welcome to our Loan lending service")
print("We offer loans at a reasonable interest, 15% for all")
print("")
print("Kindly tell us your Name,age,Gender")
print("")

# calling diff methods one by one 
user = User()
print("")
user.show_details()
print("")

user.duration()
print("")
user.amount()
print("")
print("Loan procedure comlpeted successfully")
print("")
user.repay()
print("")

# END
