#COMP SCI 1631
#ASSIGMENT 3
#Date: 2018-10-11
#DUE: 11:55PM OCT 11, 2018 
#MAXIME SOTSKY

import time
import os

bag = []
gold = 0

#positions
dead = ''
town = ("town",0,'x') #1
bush = ("Bush",1,'rock') #2
caravan = ("Caravan",2,dead) #3 (area)

# L = leave 
# t = open map menu 
# r = view item 
# i= open inventory 
# d = drop
player_position = town
def room(name, position, item):
    player_position = position
    print("You Entered the " +name)
    command = input("[L(LEAVE),T(TRAVEL),R(VIEW ITEMS),I(INVENTORY),D(DROP)]")
    while command not in 'lL':
        #if commmand in 'lL':
            #return
        if command in "tT":
            show_map()
            newplace = input()
            print("Hit L twice to leave")
            if newplace == '1':
                room("town",0,'x')
            elif newplace == '2':
                room("Bush",1,'rock')
            elif newplace == '3':
                room("Caravan",2,dead)
            else:
                print("That is not a valid place")
        if command in "rR":
            if item == 'x':
                print("There is nothing of value here")
            else:
                print("You see " +item)
                print("type 'the item name' to pick it up, hit 'D' to cancel")
                take(input(':'))
        if command in "iI":
            show_inventory()
            time.sleep(4)
        if command in "dD":
            show_inventory()
            print("Type the name of the item you want to drop, if not type anything else")
            drop(input())
        command = input("[L(LEAVE),T(TRAVEL),R(VIEW ITEMS),I(INVENTORY),D(DROP)]")
        
def show_inventory():
    print(bag)
 
def take (item):
    if item in bag:
        print("You have too many of these")
        time.sleep(3)
    if item in ['dagger','rock',"gnome's hat", "goblin helmet"]:
        if item not in bag:
            bag.append(item)
    else:
        print("Invalid item") #there is only 4 items

def drop(item):
    if item in bag:
        bag.remove(item)
        print("You discarded " +item)
        time.sleep(3)
    else:
        print("That item is not in your bag")

place_list = []
def places(location):
    if location in place_list:
        return
    if location not in place_list:
        place_list.append(location)

def show_map():
    print(place_list)
    return
        
def talk (talking): #This is to make a better speech effect
    if setting == ("speed" or "SPEED"):
        letter = len(talking)
    else:                         
         letter = 0 #start with the first char                                          
    while letter <= len(talking): #keep printing chars until the max of chars of the string  
        os.system('cls') #deletes lines really fast for speech affect                        
        print (talking[:letter]) #prints the char                                            
        time.sleep(0.0) #the delay of the chars appearing   < the delay from being used in functions seems to be enough                       
        letter += 1 #next char                                           

print("GAME SETTINGS")
print("Type 'speed' for speed run mode ( 4Testing )") #turns off speech loop and cuts wait times for fast testing
print("Type anything else to keep normal settings.")
setting = input()
print ("___ Type adventure() for amazing gamplay ___")

wait = 5
loading = 10
semiload = 6

if setting == ("speed" or "SPEED"):
    wait = 1
    loading = 1
    semiload = 1
#=====================================================================================================================#
def adventure ():
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
    while goodOrBad not in '12':
        if goodOrBad in "Ii":
            show_inventory()
            time.sleep(5)
        if goodOrBad in "rR":
            if 'dagger' not in bag:
                print('You see a dagger')
            print("You see some rocks: Type rock to pick it up")
            print("type 'the item name' to pick it up, hit 'D' to cancel")
            take(input(':'))
        if goodOrBad in "Dd":
            show_inventory()
            print("Type the name of the item you want to drop, if not type anything else")
            drop(input())
        if goodOrBad in "tT":
            show_map()
            print("hit the number that corresponds to the place you want to go")
            print("hit 'x' to exit")
            place = input()
            if place == '1':
                room("town",0,'x')
            else:
                print("That is not a valid place")
                
        goodOrBad = destraction()

    if goodOrBad == "1":
        friend = dontThrowGnome()
    elif goodOrBad == "2":
        friend = throwGnome()
    if friend == True:
        pClass = chooseClass()
        while pClass not in '1234':
            if pClass in "iI":
                show_inventory()
                time.sleep(5)
            if pClass in "rR":
                if 'dagger' not in bag:
                    print('You see a dagger')
                print("You see some rocks: Type rock to pick it up")
                print("type 'the item name' to pick it up, hit 'D' to cancel")
                take(input(':'))
            if pClass in "Dd":
                show_inventory()
                print("Type the name of the item you want to drop, if not type anything else")
                drop(input())
            if pClass in "tT":
                show_map()
                print("hit the number that corresponds to the place you want to go")
                print("hit 'x' to exit")
                place = input()
                if place == '1':
                    room("town",0,'x')
                else:
                    print("That is not a valid place")

        if pClass == "1":
            warrior()
        elif pClass == "2":
            rogue()
        elif pClass == "3":
            mage()
        elif pClass == "4":
            rock()

    if friend == False:
        badfriendDia()
        saveOrLeave = badfriend() 
        while saveOrLeave not in "12":
            if saveOrLeave in "Ii":
                show_inventory()
                time.sleep(5)
            if saveOrLeave in "rR":
                if 'dagger' not in bag:
                    print('You see a dagger')
                print("You see some rocks: Type rock to pick it up")
                print("type 'the item name' to pick it up, hit 'D' to cancel")
                take(input(':'))
            if saveOrLeave in "Dd":
                show_inventory()
                print("Type the name of the item you want to drop, if not type anything else")
                drop(input())   
            if saveOrLeave in "tT":
                show_map()
                print("hit the number that corresponds to the place you want to go")
                print("hit 'x' to exit")
                place = input()
                if place == '1':
                    room("town",0,'x')
                elif place == '2':
                    room("Bush",1,'rock')
                else:
                    print("That is not a valid place")
            saveOrLeave = badfriend()

        if saveOrLeave == "1":
            friend = saveGnome()
        else:
            leaveGnome()
    if friend == True:
        endLoading()
        dead = "Goblin helmet"
        places('3)Caravan')
        gold = bagOfGold(questCompleteWG())
        print("Type 'quit' to finish")
        walk_around = input('[i,r,d,t]')
        while walk_around != "quit":
            if walk_around in "Ii":
                show_inventory()
                time.sleep(5)
            if walk_around in "rR":
                print("There is nothing of value here")
            if walk_around in "Dd":
                show_inventory()
                print("Type the name of the item you want to drop, if not type anything else")
                drop(input())   
            if walk_around in "tT":
                show_map()
                print("hit the number that corresponds to the place you want to go")
                print("hit 'x' to exit")
                place = input()
                if place == '1':
                    room("town",0,'x')
                elif place == '2':
                    room("Bush",1,'rock')
                elif place == '3':
                    room("Caravan",2,dead)
                else:
                    print("That is not a valid place")
            print("Type 'quit' to finish")
            walk_around = input('[i,r,d,t]')
    else:
        endLoading()
        dead = "Gnome's hat"
        gold = bagOfGold(questCompleteWOG())
        places('3)Caravan')
        print("Type 'quit' to finish")
        walk_around = input('[i,r,d,t]')
        while walk_around != "quit":
            if walk_around in "Ii":
                show_inventory()
                time.sleep(5)
            if walk_around in "rR":
                print("There is nothing of value here")
            if walk_around in "Dd":
                show_inventory()
                print("Type the name of the item you want to drop, if not type anything else")
                drop(input())   
            if walk_around in "tT":
                show_map()
                print("hit the number that corresponds to the place you want to go")
                print("hit 'x' to exit")
                place = input()
                if place == '1':
                    room("town",0,'x')
                elif place == '2':
                    room("Bush",1,'rock')
                elif place == '3':
                    room("Caravan",2,dead)
                else:
                    print("That is not a valid place")
            print("Type 'quit' to finish")
            walk_around = input('[i,r,d,t]')
    return
########__GAMEPLAY__##################__GAMEPLAY__##################__GAMEPLAY__##################__GAMEPLAY__##########
#Town##Town##Town##Town##Town##Town##Town##Town##Town##Town##Town##Town##Town##Town##Town##Town##Town##Town##Town##Town#
def getName ():
    #print("You Discovered the Town!!!")#_______________________________________________Room 0.0 = TOWN
    places("1)The Town")
    time.sleep(wait)
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

def quest1 ():
    talk("Gnome: HEY BOOTLICKER!! Wanna do something wild?!??")
    print("Options: choose a number (':")
    print("1)*Nod and follow gnome* for the wild experience")
    print("2)*spit on gnome*")
    print("3)Tell gnome you don't have time for his !@#$ and to leave you alone.")
    choice = input("what you gonna do?!? [1,2,3]")
    while choice not in "123":
        talk("What?!")
        time.sleep(1)
        choice = quest1()
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
#Goblin camp##Goblin camp##Goblin camp##Goblin camp##Goblin camp##Goblin camp##Goblin camp##Goblin camp##Goblin camp#
def loadingQuest1 (): #info and gnome explaining
    print("**LOADING amazing aventure game**") #This is to give a little context on what goblins are (like wow "tips")               
    print("INFO: Goblins are rude creatures and could be dangerous in large numbers and are known for their greed and great riches")
    print("TIP: You may type r or R to show the items in your vicinity.")    
    time.sleep(loading)
    talk("Gnome: GEEZzZ LOUISE! That was some looong~ loading screen!!")
    time.sleep(wait)
    print("[*Liliput brought you deep into The Goblin Forest*]")
    time.sleep(wait)
    print("*Hiding in a bush* You and you Liliput are examining a nearby goblin camp")
    time.sleep(wait)
    print("*You have discovered the bush*")#_______________________________Room 1.0 = BUSH AREA
    time.sleep(wait)
    print("*You notice bags of gold being loaded into a caravan*")
    time.sleep(wait)
    print("*You have discovered the caravan*")#__________________________________Room 1.1 = CARAVAN AREA 4later
    time.sleep(wait)
    talk("Gnome: Here's my old bag, you can use this to put all kinds of things!")
    print("*The gnome hands you a dusty linen bag")
    time.sleep(wait)
    print("Congradulations you have unlocked the inventory! (i opens inventory)")
    time.sleep(wait)
    print("You can hit 'r' to see what is in your vacinity")
    talk("Gnome: Okay so here's the plan. . .")
    time.sleep(2)
    talk("Gnome: We gonna rob these leper gnomes by stealing that caravan. Here's a dagger incase of EMERGENCY. . (@_@)")
    print("*Gnome hands you a rusty dagger*")
    time.sleep(1)
    print("*You put the dagger in your bag*")
    take('dagger')
    time.sleep(wait)
    talk("Gnome: This is so exciting! Our first heist!!(^̮^)")
    time.sleep(wait)    
    return                                                                                                                     

def destraction ():#_____________________________________________________________Room 1.0 BUSH AREA
    talk("Gnome: Now, one of us needs to be the destraction. I vote you <3")
    print("Options")
    print("1)Be the destraction while gnome hijacks the caravan")
    print("2)*Throw little gnome into goblins* and hijack the caravan")
    goodOrBad = input("Choose [1,2,i,r,d,t]")
    return goodOrBad
        
def throwGnome ():#______________________________________________________________Room 1.0 BUSH AREA
    friendShip = False
    talk("Gnome: AAAAHHHHHHHHH!!!!!")
    time.sleep(wait)
    print("*You throw the gnome*")
    print("Goblins are destracted killing your only friend, leaving the caravan completely vulnerable")
    time.sleep(wait)
    return friendShip

def dontThrowGnome ():#___________________________________________________________Room 1.0 BUSH AREA
    friendShip = True
    talk("Gnome: Great!!")
    print("Options") #This is kinda like class selection
    print("1)*Charge into the goblins like a true warrior!")
    print("2)*stealth and sap* the goblins like a sneeky rogue assassin!")
    print("3)*Freeze* the goblins like the powerful mage you are!")
    if 'rock' in bag:
        print("4)throw your rock at the goblins")
    return friendShip

def chooseClass ():#___________________________________________________________Room 1.0 BUSH AREA
    classChoice = input("Choose [1,2,3,4,i,r,d,t]")
    return classChoice
def warrior ():#___________________________________________________________Room 1.1 CARAVAN AREA
    playerClass = "Warrior" 
    places('2)Bush')
    print("*You entered the Caravan area")
    print("*You charge into the goblins knocking them all out")
    time.sleep(wait +1)
    talk("Gnome: Hey bootlicker. Why are warriors the worst salesman?!")
    time.sleep(wait)
    talk("Gnome: BECAUSE THEY CHAAAARRRGEEEE TOO MUCH *gnome chuckles*")
    time.sleep(1)
    print("The gnome is tries to hold in his laughter while following you to the caravan")
    return 

def rogue ():#___________________________________________________________Room 1.1 CARAVAN AREA
    playerClass = "Rogue"
    places('2)Bush')
    print("*You entered the Caravan area")
    print("*You turn invisible and knock all goblins cold that were surrounding the caravan*")
    time.sleep(wait +1)
    talk("Gnome: Heyy~ bootlicker. How many butts does an assassin have?")
    time.sleep(wait)
    talk("Gnome: THEY HAVE TWO!! HAHAHAHhaah... Get it? cause ASSASSin HAHaahaAHAH")
    print("*gnome continues to laughing the entire way to the caravan*")
    return 

def mage ():#___________________________________________________________Room 1.1 CARAVAN AREA  
    playerClass = "Mage"
    places('2)Bush')
    print("*You entered the Caravan area")
    print("*You use a freezing spell* freezing all goblins surrounding the caravan*")
    time.sleep(wait)
    talk("Gnome: Woah!! That was so cool! HAHA get it? THAT WAS 'COOOOOOL~' (^̮^) ")
    print("*You can tell the gnome is trying to hold in his laughter the entire way to the caravan*")
    return

def rock ():#___________________________________________________________Room 1.1 CARAVAN AREA
    drop('rock')
    places('2)Bush')
    print("*You throw a rock you found but missed because you're a boring human")
    print("*Liliput judges you*")
    playerClass = "Boring Human"
    time.sleep(wait)
    print("*The goblins draw all their attention on the rock you threw leaving the caravan vulnerable (least it got the job done)")
    time.sleep(4)
    return

def badfriendDia ():#___________________________________________________________Room 1.1 CARAVAN AREA                                                                                      
    talk("Gnome: HELP!! I DON'T WANT TO DIE!")                                                          
    time.sleep(1)                                                                                       
    talk("Gnome: THEIR GONNA EAT ME")
def badfriend():
    places('2)Bush')                                                                 
    print("*Gnome cries*")                                                                              
    print("Options")                                                                                    
    print("1) run over the goblins with the caravan saving the little gnome from being eaten")          
    print("2) Drive away, leaving the poor gnome to die")                                               
    gnomeIsGonnaDie = input("[1,2,r,i,d,t]")                                                                    
    return gnomeIsGonnaDie                                                                              

def saveGnome():#___________________________________________________________Room 1.1 CARAVAN AREA                                                                                        
    friendShip = True                                                                                   
    print("*You run over all the goblins")                                                              
    talk("Gnome: YOU CAME BACK FOR ME !! (^̮^) ")                                                                                                                                              #
    print("*The little gnome quickly hops into the caravan*")                                           
    time.sleep(2)                                                                                       
    talk("Gnome: That was intense, i thought you were gonna leave me for a second :C")                  
    time.sleep(2)                                                                                       
    talk("Gnome: WE GOT THE 'BIG MONEY' THOUGH, thats what matters \(^o^)/")                            
    return friendShip                                                                                   
                                                                                                        
def leaveGnome():#___________________________________________________________Room 1.1 CARAVAN AREA                                                                                       
    talk("Gnome: (ToT)")                                                                                                                                                                #
    return                                                                                              
#back to town##back to town# #back to town# #back to town# #back to town# #back to town# #back to town#   
def endLoading (): #< Transitioning effect
    time.sleep(2) 
    places("3)Caravan")             
    print("Leaving Instance")  
    print("LOADING...")         
    time.sleep(semiload)              
    return
def questCompleteWOG (): #without gnome    #_______________________________________________Room 0.0 = TOWN
    print("*You arrive back to town in the caravan by yourself*")
    time.sleep(2)
    print("*You search the caravan and keep all the gold*")
    print("_____Quest Complete_____")
    return 1000
def questCompleteWG (): #with gnome        #_______________________________________________Room 0.0 = TOWN
    talk("Gnome we make a good team you and I. <3")
    print("You and your annoying friend return to town with the caravan and share the reward")
    print("_____Quest Complete_____")
    return 500
def bagOfGold (a):
    amount = a
    print ("Your earned ",amount," gold")
    time.sleep(wait)
    return amount
#After the first quest
#def town_area()#0.0

#def goblin_entrance_area() #1.0
#def bush_area()#1.1
#def caravan_area()#1.2