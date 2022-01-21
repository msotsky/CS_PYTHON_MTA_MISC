#COMP SCI 1631
#ASSIGMENT 2
#Date: 2018-10-11
#DUE: 11:55PM OCT 11, 2018 
#MAXIME SOTSKY

import time
import os
#########################################################################################
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
##############################################################################################
print("GAME SETTINGS")
print("Type 'speed' for speed run mode ( 4Testing )") #turns off speech loop and cuts wait times for fast testing
print("Type anything else to keep normal settings.")
setting = input()
print ("___ Type start() for amazing gamplay ___")
##################################################
wait = 5
loading = 10
semiload = 6

if setting == ("speed" or "SPEED"):
    wait = 1
    loading = 1
    semiload = 1
###############################
gold = 0
def start ():

    playerName = getName()
    if playerName == ("Liliput" or "liliput"):
        bagOfGold(10)
    choice = quest1()
    if choice == "1":
        followGnome()
    elif choice == "2":
        spit()
        noChoice()
    else:
        curseAndLeave()
        noChoice()
    if choice == "1" or "2" or "3":
        loadingQuest1()
        goodOrBad = destraction()
#####################################       
    if goodOrBad == "1":
        friend = dontThrowGnome()
    else:
        friend = throwGnome()
####################################
    if friend == True:
        pClass = chooseClass()
        if pClass == "1":
            warrior()
        elif pClass == "2":
            rogue()
        elif pClass == "3":
            mage()
        else:
            rock()
####################################
    if friend == False:
        saveOrLeave = badfriend()
        if saveOrLeave == "1":
            friend = saveGnome()
        else:
            leaveGnome()

    if friend == True:
        endLoading()
        gold = bagOfGold(questCompleteWG())
    else:
        endLoading()
        gold = bagOfGold(questCompleteWOG())
    return
########__GAMEPLAY__##################__GAMEPLAY__##################__GAMEPLAY__##################__GAMEPLAY__##########
def getName ():
    talk("Gnome: Greetings traveler! My name is Liliput the gnome!!! and you are? (^̮^)")
    playerName = input("...") #waiting for a user input
    if playerName == ("liliput" or "Liliput"):
        talk("Gnome: GREAAT NAAME! but that's not gonna stop me from calling you by your real name. My little bootlicker~ (^̮^)")#Faces so extra annoying effect
        print("*The gnome gives you 10 gold for attempting to cheat the system")
        time.sleep(wait)
    elif len(playerName) <= 2:
        talk("Gnome: Come on, atleast try to think of a real name, but thats okay your name is Bootlicker now (^̮^)")
        time.sleep(wait)
    else:
        talk("Gnome: Thats a terrible name! i'ma call you bootlicker instead (^̮^)") #most likely outcome
        print ("*laughs obnoxiously*")
        time.sleep(wait)
    return playerName

########__GAMEPLAY__##################__GAMEPLAY__##################__GAMEPLAY__##################__GAMEPLAY__
def quest1 ():
    talk("Gnome: HEY BOOTLICKER!! Wanna do something wild?!??")
    print("Options: choose a number (':")
    print("1)*Nod and follow gnome* for the wild experience")
    print("2)*spit on gnome*")
    print("3)Tell gnome you don't have time for his !@#$ and to leave you alone.")
    choice = input("what you gonna do?!? [1,2,3]")
    return choice
def followGnome ():
    talk("GREAT!! I knew i'd convince you. Follow me! We gonna be so rich you and me!! I'm talking big money [̲̅$̲̅(̲̅5̲̅)̲̅$̲̅]")
    return
def spit ():
    print("*Gnome spits back*")
    time.sleep(wait)
    return
def curseAndLeave ():
    print("*Gnome follows you as you walk away*(^̮^)")
    time.sleep(wait)
    talk (".  .  .  .")
    print("The gnome doesn't seem to understand no for an answer")
    time.sleep(wait)
    return
def noChoice (): 
    print("Options: [Sorry you're stuck with the annoying gnome for now.]")
    time.sleep(wait)
    print("*He seems to really like you*")
    time.sleep(2)
    print("*You nod and follow the little gnome*")
    time.sleep(wait)
    print("Gnome: GREAT!! I knew i'd convince you. Follow me! We gonna be so rich you and me!! I'm talking BIG MONEY [̲̅$̲̅(̲̅5̲̅)̲̅$̲̅]")
    time.sleep(wait)
    os.system('cls')
    return
def loadingQuest1 (): #info and gnome explaining
    print("**LOADING amazing aventure game**") #This is to give a little context on what goblins are (like wow "tips")               
    print("INFO: Goblins are rude creatures and could be dangerous in large numbers and are known for their greed and great riches")
    time.sleep(loading)
    talk("Gnome: GEEZzZ LOUISE! That was some looong~ loading screen!!")
    time.sleep(wait)
    print("[*Liliput brought you deep into The Goblin Forest*]")
    time.sleep(wait)
    print("*Hiding in a bush* You and you Liliput are examining a nearby goblin camp")
    time.sleep(wait)
    print("*You notice bags of gold being loaded into a caravan*")
    time.sleep(wait)
    talk("Gnome: Okay so here's the plan. . .")
    time.sleep(2)
    talk("Gnome: We gonna rob these leper gnomes by stealing that caravan. Here's a dagger incase of EMERGENCY. . (@_@)")
    print("*Gnome hands you a rusty dagger*")
    time.sleep(wait)
    talk("Gnome: This is so exciting! Our first heist!!(^̮^)")
    time.sleep(wait)    
    return                                                                                                                     

########__GAMEPLAY__##################__GAMEPLAY__##################__GAMEPLAY__##################
def destraction ():
    talk("Gnome: Now, one of us needs to be the destraction. I vote you <3")
    print("Options")
    print("1)Be the destraction while gnome hijacks the caravan")
    print("2)*Throw little gnome into goblins* and hijack the caravan")
    goodOrBad = input("Choose [1,2]")
    return goodOrBad

def throwGnome ():
    friendShip = False
    talk("Gnome: AAAAHHHHHHHHH!!!!!")
    time.sleep(wait)
    print("*You throw the gnome*")
    print("Goblins are destracted killing your only friend, leaving the caravan completely vulnerable")
    time.sleep(wait)
    #classChoice = "NA"
    return friendShip

def dontThrowGnome ():
    friendShip = True
    talk("Gnome: Great!!")
    print("Options") #This is kinda like class selection
    print("1)*Charge into the goblins like a true warrior!")
    print("2)*stealth and sap* the goblins like a sneeky rogue assassin!")
    print("3)*Freeze* the goblins like the powerful mage you are!")
    print("Press any other key if you're just a normal human with no powers :(")
    return friendShip
########__GAMEPLAY__##################__GAMEPLAY__##################__GAMEPLAY__##################__GAMEPLAY__#######
def chooseClass ():
    classChoice = input("Choose [1,2,3,#]")
    return classChoice
def warrior ():
    playerClass = "Warrior" 
    print("*You charge into the goblins knocking them all out")
    time.sleep(wait)
    talk("Gnome: Hey bootlicker. Why are warriors the worst salesman?!")
    time.sleep(wait)
    talk("Gnome: BECAUSE THEY CHAAAARRRGEEEE TOO MUCH *gnome chuckles*")
    time.sleep(1)
    print("The gnome is tries to hold in his laughter while following you to the caravan")
    return 

def rogue ():
    playerClass = "Rogue"
    print("*You turn invisible and knock all goblins cold that were surrounding the caravan*")
    time.sleep(wait)
    talk("Gnome: Heyy~ bootlicker. How many butts does an assassin have?")
    time.sleep(wait)
    talk("Gnome: THEY HAVE TWO!! HAHAHAHhaah... Get it? cause ASSASSin HAHaahaAHAH")
    print("*gnome continues to laughing the entire way to the caravan*")
    return 

def mage ():  
    playerClass = "Mage"
    print("*You use a freezing spell* freezing all goblins surrounding the caravan*")
    time.sleep(wait)
    talk("Gnome: Woah!! That was so cool! HAHA get it? THAT WAS 'COOOOOOL~' (^̮^) ")
    print("*You can tell the gnome is trying to hold in his laughter the entire way to the caravan*")
    return
def rock ():
    print("*You throw a rock you found but missed because you're a boring human")
    print("*Liliput judges you*")
    playerClass = "Boring Human"
    time.sleep(wait)
    print("*The goblins draw all their attention on the rock you threw leaving the caravan vulnerable (least it got the job done")
    time.sleep(3)
    return
#####badfriend##########badfriend##########badfriend##########badfriend##########badfriend##########badfr
def badfriend ():                                                                                       #
    talk("Gnome: HELP!! I DON'T WANT TO DIE!")                                                          #
    time.sleep(2)                                                                                       #
    talk("Gnome: THEIR GONNA EAT ME")                                                                   #
    print("*Gnome cries*")                                                                              #
    print("Options")                                                                                    #
    print("1) run over the goblins with the caravan saving the little gnome from being eaten")          #
    print("2) Drive away, leaving the poor gnome to die")                                               #
    gnomeIsGonnaDie = input("[1,2]")                                                                    #
    return gnomeIsGonnaDie                                                                              #
#####badfriend##########badfriend##########badfriend##########badfriend##########badfriend##########badfr
def saveGnome():                                                                                        #
    friendShip = True                                                                                   #
    print("*You run over all the goblins")                                                              #
    talk("Gnome: YOU CAME BACK FOR ME !! (^̮^) ")                                                        #                                                                                       #
    print("*The little gnome quickly hops into the caravan*")                                           #
    time.sleep(2)                                                                                       #
    talk("Gnome: That was intense, i thought you were gonna leave me for a second :C")                  #
    time.sleep(2)                                                                                       #
    talk("Gnome: WE GOT THE 'BIG MONEY' THOUGH, thats what matters \(^o^)/")                            #
    return friendShip                                                                                   #
                                                                                                        #
def leaveGnome():                                                                                       #
    talk("Gnome: (ToT)")                                                                                #                                                                                    #
    return                                                                                              #
#########################################################################################################   
def endLoading (): #< Transitioning effect
    time.sleep(2)              
    print("Leaving Instance")  
    print("LOADING...")         
    time.sleep(semiload)              
    return
def questCompleteWOG (): #without gnome    
    print("*You arrive back to town in the caravan by yourself*")
    time.sleep(2)
    print("*You search the caravan and keep all the gold*")
    print("_____Quest Complete_____")
    return 1000
def questCompleteWG (): #with gnome
    talk("Gnome we make a good team you and I. <3")
    print("You and your annoying friend return to town with the caravan and share the reward")
    print("_____Quest Complete_____")
    return 500
def bagOfGold (a):
    amount = a
    print ("Your earned ",amount," gold")
    time.sleep(wait)
    return amount
