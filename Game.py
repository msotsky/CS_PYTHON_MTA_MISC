#COMP SCI 1631
#ASSIGMENT 1 PART 1 (IF STATEMENTS)
#Date: 2018-09-24 _ 2018-09-25
#DUE: SEPTEMBER 28, 2018 AT 11:55PM
#MAXIME SOTSKY
#World of Warcraft influenced
# using '★' to divide each type of if statements (easier for me to read it)

import time
import os
#these vars are to keep track of choices / inventory
playerClass = " "
gold = 0
moral = 0
gnomeSays = "Gnome: Greetings traveler! My name is Liliput the gnome!!! and you are? (^̮^)" #using (^̮^) for extra annoying effect
#using a var to display so i can use the speaking affect
traveler1Name = "Liliput"
badName = 0
letter = 0
#Going to be using this while loop for a nicer reading affect, hope im allowed to do this
#i'm not sure how to make this into a function or if i even can
while letter <= len(gnomeSays): #hope im allowed to do this
    os.system('cls') #delete lines really fast for reading affect
    print (gnomeSays[:letter]) #printing letters
    time.sleep(0.05)#printing letter delay / speed
    letter += 1 #adding one to letter count, going to next letter

playerName = input("...") #waiting for a user input
letter = 0 #reseting letter count
#a if elif and else (with exactly one elif)★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
if playerName == traveler1Name:
    gnomeSays = "Gnome: GREAAT NAAME! but that's not gonna stop me from calling you by your real name. My little bootlicker~ (^̮^)"
    while letter <= len(gnomeSays): 
        os.system('cls') 
        print (gnomeSays[:letter])
        time.sleep(0.05)
        letter += 1
    print("*The gnome gives you 10 gold for attempting to cheat the system")
elif len(playerName) <= 2:
    gnomeSays = "Gnome: Come on atleast try to think of a name a real name, but thats okay your name is Bootlicker now (^̮^)"
    while letter <= len(gnomeSays): 
        os.system('cls') 
        print (gnomeSays[:letter])
        time.sleep(0.05)
        letter += 1
else:
    gnomeSays = "Gnome: Thats a terrible name! ima call you bootlicker instead (^̮^)" #most likely outcome
    while letter <= len(gnomeSays): 
        os.system('cls') 
        print (gnomeSays[:letter]) 
        time.sleep(0.05)
        letter += 1
    print ("*laughs obnoxiously*")
time.sleep(4)
letter = 0
gnomeSays = "Gnome: HEY BOOTLICKER!! Wanna do something wild?!??"
while letter <= len(gnomeSays): 
    os.system('cls') 
    print (gnomeSays[:letter]) 
    time.sleep(0.05)
    letter += 1
print("Options: choose a number (':")
print("1)*Nod* and follow gnome for the wild experience")
print("2)*spit on gnome*")
print("3)Tell gnome you don't have time for his !@#$ and to leave you alone.")

choice = input("what you gonna do?!? [1,2,3]")

letter = 0
#d. if elif elif ★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
if choice == "1":
    gnomeSays = "GREAT!! I knew i'd convince you. Follow me! We gonna be so rich you and me!! I'm talking big money [̲̅$̲̅(̲̅5̲̅)̲̅$̲̅]"
    while letter <= len(gnomeSays): 
        os.system('cls') 
        print (gnomeSays[:letter]) 
        time.sleep(0.05)
        letter += 1
elif choice == "2":
    print("*Gnome spits back*")
elif choice == "3":
    print("*Gnome follows you as you walk away*(^̮^)")
#e. if no trailing elif or else ★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
if choice != "1": #To keep my story going by not giving the player any real choices
    print("Options: [Sorry you're stuck with the annoying gnome for now..]")
    print("4)*Nod and follow gnome for the wild experience*")
    newChoice = input("choice selection: [4](PRESS 4 KEY TO CONTINUE AMAZING ADVENTURE)")
    letter = 0
    if newChoice == "4":
        gnomeSays = "GREAT!! I knew i'd convince you. Follow me! We gonna be so rich you and me!! I'm talking BIG MONEY [̲̅$̲̅(̲̅5̲̅)̲̅$̲̅]"
        while letter <= len(gnomeSays): 
            os.system('cls') 
            print (gnomeSays[:letter]) 
            time.sleep(0.05)
            letter += 1
time.sleep(5)
print("[*Liliput has brought you deep into The Goblin Forest*]")
time.sleep(5)
print("**LOADING amazing aventure game**") #This is to give a little context on what goblins are 
print("INFO: Goblins are rude creatures and could be dangerous in large numbers and are known for their greed and great riches")
time.sleep(10)

letter = 0
gnomeSays = "Gnome: GEEZzZ LOUISE! That was some looong~ loading screen!!"
while letter <= len(gnomeSays): 
    os.system('cls') 
    print (gnomeSays[:letter]) 
    time.sleep(0.05)
    letter += 1
time.sleep(4)
print("*Hiding in a bush* You and you Liliput are examining a nearby goblin camp")
time.sleep(4)
print("*You notice bags of gold being loaded into a caravan*")
letter = 0
gnomeSays = "Gnome: Okay so here's the plan. . ."
while letter <= len(gnomeSays): 
    os.system('cls') 
    print (gnomeSays[:letter]) 
    time.sleep(0.05)
    letter += 1
letter = 0
gnomeSays = "Gnome: We gonna rob these leper gnomes by stealing that caravan. Here's a dagger"
while letter <= len(gnomeSays): 
    os.system('cls') 
    print (gnomeSays[:letter]) 
    time.sleep(0.05)
    letter += 1
print("*Gnome hands you a rusty dagger*")
time.sleep(5)
letter = 0
gnomeSays = "Gnome: Now, one of us needs to be the destraction. I vote you <3"
while letter <= len(gnomeSays): 
    os.system('cls') 
    print (gnomeSays[:letter]) 
    time.sleep(0.05)
    letter += 1
print("Options")
print("1)Be the destraction while gnome hijacks the caravan")
print("2)*Throw little gnome into goblins* and hijack the caravan")
choice = input("Choose [1,2]")

if choice == "2":
    moral = -1
    letter = 0
    gnomeSays = "Gnome: AAAAHHHHHHHHH!!!!!"
    while letter <= len(gnomeSays): 
        os.system('cls') 
        print (gnomeSays[:letter]) 
        time.sleep(0.05)
        letter += 1
    time.sleep(4)
    print("*You throw the gnome*")
    print("Goblins are killing your only friend, leaving the caravan vulnerable")
if choice == "1":
    print("Options") #This is kinda like class selection
    print("1)*Charge into the goblins like a true warrior!")
    print("2)*stealth and sap* the goblins like a sneeky rogue assassin!")
    print("3)*Freeze* the goblins like the powerful mage you are!")
    print("Press any other key if you're just a normal human with no powers :(")
    classChoice = input("Choose [1,2,3,#]")
#b.if elif elif else (least 1 else)★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
if classChoice == "1": #Warrior selection
    playerClass = "Warrior" #setting players class
    print("*You charge into the goblins knocking them all out")
    time.sleep(5)
    letter = 0
    gnomeSays = "Gnome: Hey bootlicker. Why is are warriors the worst salesman?!"
    while letter <= len(gnomeSays): 
        os.system('cls') 
        print (gnomeSays[:letter]) 
        time.sleep(0.05)
        letter += 1
    time.sleep(5)
    letter = 0
    gnomeSays = "Gnome: BECAUSE THEY CHAAAARRRGEEEE TOO MUCH *gnome chuckles*"
    time.sleep(1)
    print("The gnome is tries to hold in his laughter while following you to the caravan")
elif classChoice == "2": #Rogue selection
    playerClass = "Rogue"
    print("*You turn invisible and knock all goblins cold that were surrounding the caravan*")
    time.sleep(5)
    letter = 0
    gnomeSays = "Gnome: Heyy~ bootlicker. How many butts does an assassin have?"
    while letter <= len(gnomeSays): 
        os.system('cls') 
        print (gnomeSays[:letter]) 
        time.sleep(0.05)
        letter += 1
    time.sleep(5)
    letter = 0
    gnomeSays = "Gnome: THEY HAVE TWO!! HAHAHAHhaah... Get it? cause ASSASSin HAHaahaAHAH"
    while letter <= len(gnomeSays): 
        os.system('cls') 
        print (gnomeSays[:letter]) 
        time.sleep(0.05)
        letter += 1
    print("*gnome continues to laughing the entire way to the caravan*")
elif classChoice == "3": #Mage selection
    playerClass = "Mage"
    print("*You use a freezing spell* freezing all goblins surrounding the caravan*")
    time.sleep(5)
    letter = 0
    gnomeSays = "Gnome: Woah!! That was so cool! HAHA get it? THAT WAS 'COOOOOOL~' (^̮^) "
    while letter <= len(gnomeSays): 
        os.system('cls') 
        print (gnomeSays[:letter]) 
        time.sleep(0.05)
        letter += 1
    print("*You can tell the gnome is trying to hold in his laughter the entire way to the caravan*")
else:
    print("*You throw a rock you found but missed because you're a boring human")
    print("*Liliput judges you*")
    time.sleep(5)
    print("*The goblins draw all their attention on the rock you threw leaving the caravan vulnerable (least it got the job done")
    time.sleep(3)

#c. if else (with 0 elifs)★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
if moral == -1:
    print("You steal the caravan for yourself, leaving your poor gnome friend to get eaten alive by goblins")
    gold += 1000
else:
    print("You and your annoying friend return to town with the caravan and share the gold you've stolen")
    gold += 500





















