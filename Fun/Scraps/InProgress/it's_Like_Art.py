
'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''
import math

flag = False
son = 0
n = 1
p = 0
progress = list()
numberarray = list()
goal = 5
#while will run until goal is satisfied
while flag == False:
    #print(n,"!")
    progress.append(n)
    j=0
    p=1
    while j < len(progress):            
        p=p*progress[j-1]
        j+=1
    numberarray = [int(x) for x in str(p)]
    #add numbers from factorial product
    i=0
    son=0
    while i<len(numberarray):
        son = son + numberarray[i]
        i+=1
        #print(son)
        #print(n,"!")
    #if sum == goal yay!
    if son == goal:
        print("the factorial thats sum eqauls 100 is", n)
        flag = True
    print(n,"! = ",p," ",son)
    n+=1
