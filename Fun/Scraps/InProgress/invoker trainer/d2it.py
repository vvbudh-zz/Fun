import math
import random
import re
import keyboard
# import only system from os 
from os import system, name 
  
# import sleep to show output for some time period 
from time import sleep 
  
# define our clear function 
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
# now call function we defined above 
clear() 
usyn = "y"
udkbyn = "n"
quas = "q"
wex = "w"
exort = "e"
invoke = "r"
cast1 = "d"
cast2 = "f"
coldsnap = [quas,quas,quas,"Cold Snap"]
ghostwalk = [quas,quas,wex,"Ghost Walk"]
icewall = [quas,quas,exort,"Ice Wall"]
emp = [wex,wex,wex,"EMP"]
tornado = [wex,wex,quas,"Tornado"]
alacrity = [wex,wex,exort,"Alacrity"]
sunstrike = [exort,exort,exort,"Sun Strike"]
forgespirit = [exort,exort,quas,"Forge Spirit"]
chaosmeteor = [exort,exort,wex,"Chaos Meteor"]
deafeningblast = [quas,wex,exort,"Deafening Blast"]
spells = [coldsnap,ghostwalk,icewall,emp,tornado,alacrity,sunstrike,forgespirit,chaosmeteor,deafeningblast]
last2spells = [coldsnap,icewall]
tempspell = icewall
currentspell = coldsnap
print("Welcome to Invoker Trainer >:)")
usyn = input("Use Save? ( y / n ): ")
#opensave
udkbyn = input("would you like to use the default keybinds? ( y / n ): ")
if udkbyn == "n" or udkbyn == "N":
    quas = input("Quas: ")
    wex = input("Wex: ")
    exort = input("Exort: ")
    invoke = input("Invoke: ")
    cast1 = input("Cast Spell 1: ")
    cast2 = input("Cast Spell 2: ")
    coldsnap = [quas,quas,quas,"Cold Snap"]
    ghostwalk = [quas,quas,wex,"Ghost Walk"]
    icewall = [quas,quas,exort,"Ice Wall"]
    emp = [wex,wex,wex,"EMP"]
    tornado = [wex,wex,quas,"Tornado"]
    alacrity = [wex,wex,exort,"Alacrity"]
    sunstrike = [exort,exort,exort,"Sun Strike"]
    forgespirit = [exort,exort,quas,"Forge Spirit"]
    chaosmeteor = [exort,exort,wex,"Chaos Meteor"]
    deafeningblast = [quas,wex,exort,"Deafening Blast"]
    spells = [coldsnap,ghostwalk,icewall,emp,tornado,alacrity,sunstrike,forgespirit,chaosmeteor,deafeningblast]
    last2spells = [coldsnap,icewall]
    tempspell = icewall
    currentspell = coldsnap
noruwtp = input("How many rounds would you like to play?: ")
while noruwtp != 0:
    temp = 0
    while temp == 0:
        clear()
        x = random.randrange(0,9)
        #print(x)
        if spells[x] == currentspell or spells[x] == last2spells[0] or spells[x] == last2spells[1]:
            continue
        else:
            temp = 1
    currentspell = spells[x]
    last2spells[1] = last2spells[0]
    last2spells[0] = currentspell
    print(currentspell[3])
    # now we need ti get the inpu from the keyboard and limit it to 5 key presses and match the imput to the current spell formula plus invoke key and cast key
    # after that add different game modes(most speels in time limit, mosst speels before fuck up, speel combos, an infinite mode where wrong input losses more health than gain from correct input)
    # then keep track of stats
    # then add save and load stats and key bindings
    # then add *GUI*??
    #noruwtp-=1