"""Calibrating the exercises to the audience is going to be a challenging task,
so I ask you to bear with me if the exercises are too easy or too hard.
Every week there will be a poll you can click on to discuss whether the exercise
is too easy or too hard and hopefully in a few weeks, I’ll get the level right.
Let’s get to it! I will start with the exercise and include a discussion later,
in case you want the extra challenge.

Exercise 1 (and Solution)
Create a program that asks the user to enter their name and their age. Print out
a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing
out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines.
(Hint: the string "\n is the same as pressing the ENTER button)"""


def getName():
    name = input("What's your name man?\n")
    return name

def getAge():
    age = input("What's your age man?\n")
    return age

def when100(age):
    till100 = (100 - age)
    print("You'll be 100 in", till100, "years!")

print("Cool name" , getName())
when100(int(getAge()))

















