#COMP SCI 1631
#ASSIGMENT 1 PART 1 (IF STATEMENTS)
#Date: 2018-09-27
#DUE: SEPTEMBER 28, 2018 AT 11:55PM
#MAXIME SOTSKY

# using '★' to divide each type of if statements (easier for me to read it)
#World of Warcraft influenced

import time
import os

###################
playerClass = " "  #
gold = 0           ## < these vars are to keep track of choices / inventory
moral = 0          #
####################
print("GAME SETTINGS")
print("Type 'speed' for speed run mode ( 4Testing )") #turns off speech loop and cuts wait times for fast testing
print("Type anything else to keep normal settings.")
setting = input()

def talk (talking): #This is to make a better speech effect
    if setting == ("speed" or "SPEED"):
        letter = len(talking)
    else:                         
         letter = 0 #start with the first char                                          
    while letter <= len(talking): #keep printing chars until the max of chars of the string  
        os.system('cls') #deletes lines really fast for speech affect                        
        print (talking[:letter]) #prints the char                                            
        time.sleep(0) #the delay of the chars appearing   < the delay from being used in functions seems to be enough                       
        letter += 1 #next char

print("Type 'adventure()' to start the game")
def adventure():
    talk("Gnome: Greetings traveler! My name is Liliput the gnome!!! and you are? (^̮^)")
    travelerName = "Liliput"

    playerName = input("...") #waiting for a user input
    #a if elif and else (with exactly one elif)★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★

    if playerName == travelerName:
        talk("Gnome: GREAAT NAAME! but that's not gonna stop me from calling you by your real name. My little bootlicker~ (^̮^)")#Faces so extra annoying effect
        print("*The gnome gives you 10 gold for attempting to cheat the system")
    elif len(playerName) <= 2:
        talk("Gnome: Come on atleast try to think of a name a real name, but thats okay your name is Bootlicker now (^̮^)")
    else:
        talk("Gnome: Thats a terrible name! i'ma call you bootlicker instead (^̮^)") #most likely outcome
        print ("*laughs obnoxiously*")
    time.sleep(4)

    talk("Gnome: HEY BOOTLICKER!! Wanna do something wild?!??")

    print("Options: choose a number (':")
    print("1)*Nod and follow gnome* for the wild experience")
    print("2)*spit on gnome*")
    print("3)Tell gnome you don't have time for his !@#$ and to leave you alone.")
    choice = input("what you gonna do?!? [1,2,3]")

    #d. if elif elif ★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
    if choice == "1":
        talk("GREAT!! I knew i'd convince you. Follow me! We gonna be so rich you and me!! I'm talking big money [̲̅$̲̅(̲̅5̲̅)̲̅$̲̅]")
    elif choice == "2":
        print("*Gnome spits back*")
    elif choice == "3":
        print("*Gnome follows you as you walk away*(^̮^)")
        time.sleep(4)
        talk (".  .  .  .")
        print("The gnome doesn't seem to understand no for an answer")
    time.sleep(5)

    #e. if no trailing elif or else ★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
    if choice != "1": #To keep my story going by not giving the player any real choices
        print("Options: [Sorry you're stuck with the annoying gnome for now.]")
        time.sleep(2)
        print("*He seems to really like you*")
        time.sleep(2)
        print("*You nod and follow the little gnome*")
        time.sleep(4)
        print("Gnome: GREAT!! I knew i'd convince you. Follow me! We gonna be so rich you and me!! I'm talking BIG MONEY [̲̅$̲̅(̲̅5̲̅)̲̅$̲̅]")
        time.sleep(5)
        os.system('cls')
    ##################################################################################################################################
    print("**LOADING amazing aventure game**") #This is to give a little context on what goblins are (like wow "tips")               #
    print("INFO: Goblins are rude creatures and could be dangerous in large numbers and are known for their greed and great riches") #
    time.sleep(10)                                                                                                                   #
    ##################################################################################################################################
    talk("Gnome: GEEZzZ LOUISE! That was some looong~ loading screen!!")
    time.sleep(3)

    print("[*Liliput brought you deep into The Goblin Forest*]")
    time.sleep(5)

    print("*Hiding in a bush* You and you Liliput are examining a nearby goblin camp")
    time.sleep(5)

    print("*You notice bags of gold being loaded into a caravan*")
    time.sleep(2)
    talk("Gnome: Okay so here's the plan. . .")
    time.sleep(2)
    talk("Gnome: We gonna rob these leper gnomes by stealing that caravan. Here's a dagger incase of EMERGENCY. . (@_@)")
    print("*Gnome hands you a rusty dagger*")
    time.sleep(5)
    talk("Gnome: This is so exciting! Our first heist!!(^̮^)")
    time.sleep(5)

    talk("Gnome: Now, one of us needs to be the destraction. I vote you <3")
    print("Options")
    print("1)Be the destraction while gnome hijacks the caravan")
    print("2)*Throw little gnome into goblins* and hijack the caravan")
    choice = input("Choose [1,2]")

    if choice == "2":
        moral = -1
        talk("Gnome: AAAAHHHHHHHHH!!!!!")
        time.sleep(4)
        print("*You throw the gnome*")
        print("Goblins are destracted killing your only friend, leaving the caravan completely vulnerable")
        friendShip = False
        classChoice = "NA"
    elif choice == "1":
        moral = 1
        talk("Gnome: Great!!")
        friendShip = True
        print("Options") #This is kinda like class selection
        print("1)*Charge into the goblins like a true warrior!")
        print("2)*stealth and sap* the goblins like a sneeky rogue assassin!")
        print("3)*Freeze* the goblins like the powerful mage you are!")
        print("Press any other key if you're just a normal human with no powers :(")
        classChoice = input("Choose [1,2,3,#]")
    #b.if elif elif else (least 1 else)★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★ #setting players class
    if classChoice == "1": #Warrior selection
        playerClass = "Warrior" 
        print("*You charge into the goblins knocking them all out")
        time.sleep(5)

        talk("Gnome: Hey bootlicker. Why are warriors the worst salesman?!")
        time.sleep(5)

        talk("Gnome: BECAUSE THEY CHAAAARRRGEEEE TOO MUCH *gnome chuckles*")
        time.sleep(1)
        print("The gnome is tries to hold in his laughter while following you to the caravan")

    elif classChoice == "2": #Rogue selection
        playerClass = "Rogue"
        print("*You turn invisible and knock all goblins cold that were surrounding the caravan*")
        time.sleep(5)

        talk("Gnome: Heyy~ bootlicker. How many butts does an assassin have?")
        time.sleep(5)

        talk("Gnome: THEY HAVE TWO!! HAHAHAHhaah... Get it? cause ASSASSin HAHaahaAHAH")
        print("*gnome continues to laughing the entire way to the caravan*")
    elif classChoice == "3": #Mage selection
        playerClass = "Mage"
        print("*You use a freezing spell* freezing all goblins surrounding the caravan*")
        time.sleep(5)
        talk("Gnome: Woah!! That was so cool! HAHA get it? THAT WAS 'COOOOOOL~' (^̮^) ")
        print("*You can tell the gnome is trying to hold in his laughter the entire way to the caravan*")
    else:
        print("*You throw a rock you found but missed because you're a boring human")
        print("*Liliput judges you*")
        time.sleep(5)
        print("*The goblins draw all their attention on the rock you threw leaving the caravan vulnerable (least it got the job done")
        time.sleep(3)

    if friendShip == False:
        talk("Gnome: HELP!! I DON'T WANT TO DIE!")
        time.sleep(2)
        talk("Gnome: THEIR GONNA EAT ME")
        print("*Gnome cries*")
        print("Options")
        print("1) run over the goblins with the caravan saving the little gnome from being eaten")
        print("2) Drive away, leaving the poor gnome to die")
        gnomeIsGonnaDie = input("[1,2]")
        if gnomeIsGonnaDie == "1":
            print("*You run over all the goblins")
            talk("Gnome: YOU CAME BACK FOR ME !! (^̮^) ")
            moral += 1
            print("*The little gnome quickly hops into the caravan*")
            time.sleep(2)
            talk("Gnome: That was intense, i thought you were gonna leave me for a second :C")
            time.sleep(2)
            talk("Gnome: WE GOT THE 'BIG MONEY' THOUGH, thats what matters ＼(^o^)／")
        else:
            talk("Gnome: (ToT)")
        
    ############################
    time.sleep(2)              #
    print("Leaving Instance")  #
    print("LOADING...")        # < Transitioning effect
    time.sleep(6)              #
    ############################
    #c. if else (with 0 elifs)★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
    if moral == -1:
        print("*You arrive back to town in the caravan by yourself*")
        time.sleep(2)
        print("*You search the caravan and keep all the gold*")
        gold = 1000
        print("You earned 1000g")
        print("_____Quest Complete_____")
    else:
        talk("Gnome we make a good team you and I. <3")
        print("You and your annoying friend return to town with the caravan and share the reward")
        gold = 500
        print("You earned 500g")
        print("_____Quest Complete_____")
