import os
import random
import socket
import sys
import timeit
import datetime

'''socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(())'''


#Classes, the big dawgs.



class User:
    """this is a class for getting the first name and last name of a user.constructor."""
    def ___init___(self,full_name, birthday):
        """This is the constructor for the user class. Gives us full_name, and birthday.#self.birthday ,
        is the variable you actually use. birthday is the parameter you pass into the function or class."""

        self.name = full_name
        self.birthday = birthday #yyyymmdd

        #Separate the first and last name.
        name_Pieces = full_name.split(" ")
        self.first_name = name_Pieces[0]
        self.last_name = _[-1]

    def age(self):
        """Returns the age of the user in years."""
        today = datetime.date(2001,5,12)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy,mm,dd) #date of birth.
        age_in_days = (today - dob).days
        age_in_years = age_in_days / 365
        return int(age_in_years)

user = User("David Bowie"," 1978,02,12")
print(user.age())

'''
#my testers
def getFirstName:
    #this wil ask the user to tell you a first name

def getLastName:
    #This will as the user to tell us the last name.

def printBoth:
    #prints both names together.
#print(user.self.firstName, " ", user.self.lastname)
'''







"""
user1 = User()
user1.firstName = "David"
user1.lastName = "Bowie"

user2 = User()
user2.firstName = "David"
user2.lastName = "Beckham"


user3 = User()
user3.firstName = "Arthur"
user3.lastName = "Joker"
user3.nickname = "Joker"
"""















'''#strings and how they work.
message = "This is a string"
print (message)'''























#Tuples and how they all work.
'''print(dir(sys))
#This gets the man page of the "getsizeof" function.
print(help(sys.getsizeof))




#The time it command times how long a certain task will take.
#Idk what stmt and the rest of it is, but the last 1 mil number
#here is for how many time to do it over. So we created 1 mil
# #lists and tupeles and saw how long it took.
testList = timeit.timeit(stmt="[1,2,3,4,5]", number = 1000000000)

testTuple = timeit.timeit(stmt="(1,2,3,4,5)", number= 1000000000)

#this prints the two times it took to run the commands.
#The list will take longer.
print ("List time: ", testList)
print ("Tuple time: ", testTuple)

#The difference in time
print("This is the difference in time, testTuple / testList:\n",   testTuple / testList)'''


























'''#Get input from a user and double the int it gets.
def getInput():
    # print("Tell me the numbers you want doubled?")
    userInput = input("Give me a number.")
    userInput = int(userInput) * 2
    print(userInput)
getInput()'''