

#A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

import random as r
import math




def palindromeLoop():
    '''This is the palindrome loop. I like making the entire function in, well
    a fucking function. Mornin' I haven't had my tea.
    It's going to generate the first numbers.'''

    largestPalindrome = 0
    p1 = 0
    p2 = 0
    incriment = 0
    
    while incriment != -1:
        '''While we are looking for a number that's a palindrome, 
        keep looking, if we find it, stop.'''
        incriment = incriment + 1  # to keep track of how many iterations.

        #make the random number.
        first = r.randint(100,999)
        second = r.randint(100,999)

        #This is a test to see if it worked.
        #print (first, second)
        #It does.

        #print("Here's the multiplied = first....")
        #Multiply them into the one big number.
        multiplied = first * second

        #print(multiplied)
        #Convert it to a string
        strMultiplied = str(multiplied)
        
        # add to list of palindromes

        # search list for highest value

        #idk why but [::-1] makes it go backwards. This will start at the end and
        # count backwards until you get to position 0
        #make the inverse/reverse.
        inverse = (strMultiplied[::-1])
        #print(inverse)
        #print("Here's the if statement.")
        if (inverse) == strMultiplied:
            print("We found one. ", multiplied)
            incriment = -1


palindromeLoop()







