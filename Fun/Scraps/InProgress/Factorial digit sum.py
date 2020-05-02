
'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!


###Sudo code. -vv
Make a function for finding the factorial
        n = userInput()
        b = n #backup variable for start.
        
        ProgressVar = b * (n - 1) #save the progress for the next turn.
        n = n-1 #decriment the variable in prep for the next multiplication.
        ProgressVar =  b *(n - 1) #Next incriment, use a while loop

        Upon completion of the loop, when n = 0, print the final number.
        

Make a function to find the sum of the factorial we just created is not None:
    FindFactorial(int n):'''
rollingTotal = 0#This is the rolling total that we'll add to each time we
# iterate.

#This Didn't do what I wanted yet becaues I don't want to type in the # each
# time while debugging. Comment for now.
'''n = input("What's the number you want to provide to us today?")
print("You've selected3", n, "as your variable.")'''
n = 10
b = n
progressVar = 0
while (n > 0):
    progressVar = (b * (n - 1) + progressVar)
    print(progressVar)
    rollingTotal = progressVar + rollingTotal
    n = n - 1
    #progressVar = b * (n - 1)

print(rollingTotal)
