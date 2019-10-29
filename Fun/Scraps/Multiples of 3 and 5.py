"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23..
Find the sum of all the multiples of 3 or 5 below 1000."""


def createList5():
    """This is going to be the function that creates all of the lists
    that we will be working with."""
    i = 0
    listOf5 = []
    """This is to cycle through and generates the list of multiples of 5s"""
    for x in range(0, 1000):
        """This is for the lists of 5 and it's mod stuff."""
        if ((x % 5) == 0):
            listOf5.append(x)
        else:
            i = i + 1
    return listOf5

def sumLists(list):
    """This will sum the entire list and print it as an int."""
    i = 0
    x = (len(list))
    for x in range (0, x):
        i = i + list[x]
    print(i)




def createList3():
    """"This creates the list of multiples of 3s"""
    c = 0
    listOf3 = []
    """This is to cycle through and generate the list for the program."""
    for x in range(0, 1000):
        """if x equals 0 when you mod by three add it to the list. """
        if ((x % 3) == 0):
            listOf3.append(x)
    else:
        c = c + 1
    return listOf3

###This is the beginning of main basically.

"""createList5()"""
sumLists(createList5())
print("This is the sum of the list of 5s \n")
sumLists(createList3())
print("This is the sum of the list of 3s")
