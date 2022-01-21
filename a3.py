#COMP SCI 1631
#ASSIGMENT 3
#Date: 2018-10-31
#DUE: OCT 31 11:55PM 
#MAXIME SOTSKY

import time
import os
import random

bag = []
gold = 0
#font color green

#https://www.geeksforgeeks.org/print-colors-python-terminal/
def red(skk): print("\033[91m {}\033[00m" .format(skk)) #for warrior class text
def green(skk): print("\033[92m{}\033[00m" .format(skk)) #for goblin visual and tree leaves
def yellow(skk): print("\033[93m {}\033[00m" .format(skk)) #for rogue class text
def cyan(skk): print("\033[96m {}\033[00m" .format(skk))  #for mage class text
def purple(skk): print("\033[94m {}\033[00m" .format(skk)) # unlocking text color

#positions the player can be in (rooms)
dead = ''
town = ("town",0,'x') #1
bush = ("Bush",1,'rock') #2
caravan = ("Caravan",2,dead) #3 (area)
##########################
# L = leave              #
# t = open map menu      #
# r = view item          # These are all the player commands
# i= open inventory      #
# d = drop               #
##########################

player_position = town
def room(name, position, item): #This function creates a room with the parameters provided for each room
    player_position = position #The number that corresponds for the room for the traveling option
    talk("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    print("You Entered the " +name) #Sets the name of the room you are in
    command = input("[L(LEAVE),T(TRAVEL),R(VIEW ITEMS),I(INVENTORY),D(DROP)]") #These are the options the player who went back to a room
    while command not in 'lL': #player option to leave the room and go back to the main story line
        if command in "tT":# player option to keep traveling to a room they've previously discovered
            show_map()#shows the places discovered
            new_place = input()
            print("Hit L twice to leave")#confirm leaving an area
            if new_place == '1':#################
                room("town",0,'x')             #
            elif new_place == '2':              #
                room("Bush",1,'rock')          #These are the possible room option the player can travel to
            elif new_place == '3':              #
                room("Caravan",2,dead)##########          
            else:
                print("That is not a valid place") #makes sure that the player chooses a valid area to travel
        if command in "rR": #to see what items a room contains
            if item == 'x': #invalid items and exit option for the player
                print("There is nothing of value here")
            else:
                print("You see " +item) #displayers item  that the player can see
                print("type 'the item name' to pick it up, hit 'D' to cancel")
                take(input(':'))#player either types the item they want or hits D to cancel the selected option
        if command in "iI": #view iventory
            show_inventory()
            time.sleep(4)
        if command in "dD": #drop option
            show_inventory()
            print("Type the name of the item you want to drop, if not type anything else")
            drop(input())
        command = input("[L(LEAVE),T(TRAVEL),R(VIEW ITEMS),I(INVENTORY),D(DROP)]") #goes back to command option after the room loop

def gamble():
    talk("Gnome: Wanna gamble?")
    print("Yype y for yes n for no")
    yes_no = input()
    if yes_no in "nN":
        return
    if yes_no in "yY":
        talk("How much you want to bet?")
        bet = input()
        print("You set a bet of", bet,"g")
        time.sleep(3)
        talk("Gnome: Im rolling first")
        gnome_rolls =  (random.randint(1,12))#generating random number between 1 and 12 for gnome
        print("Gnome rolls a ", gnome_rolls)
        time.sleep(3)
        if gnome_rolls == 12: #cause gnome is annoying
            talk("Gnome: HAHAHhahaHahHa!!")
            talk("better luck next time fella")
            time.sleep(2)
            talk("Gnome: Bootlicker is Broke!!")
            time.sleep(2)
            talk("Gnome: How's it feel bootlicker??")
            time.sleep(2)
            talk("Gnome: I got all tha dough")
            time.sleep(2)
            talk("Gnome: All yo cheddar")
            time.sleep(2)
            talk("Gnome: N~~~~~~~")
            time.sleep(3)
            talk("Gnome: Cheeeesssseee~~~~~~")
            time.sleep(2)
            talk("what you gotta say booty?")
        if gnome_rolls < 12:
            print("Type r to roll")
            rol = input()
            if rol in "rR":
                your_roll = (random.randint(1,12))#generates a random number for the player between 1 and 12
                print("You rolled a", your_roll)
                time.sleep(3)
                if gnome_rolls > your_roll:#if the gnomes's number is larger
                    talk("Pay up!")                                         #compares both numbers
                if gnome_rolls == your_roll:#if the player's number is larger
                    talk("Damn we tied")
                    time.sleep(3)
                    return
                if gnome_rolls < your_roll:#gnome never has money ..ha ha
                    talk("Gnome: Jokes on you!")
                    time.sleep(2)
                    talk("Gnome: I don't have no moneyyyy")
                    time.sleep(2)
                    talk("Gnome: what you gonna do eh!")
                    time.sleep(2)
                    talk("Gnome: I'll fight you!")
                    time.sleep(2)
                    talk("Gnome:...")
                    time.sleep(2)
                    talk("YEAH.. Thats what I thought..")
                    time.sleep(2)
                    return
            else:
                return

def show_inventory(): #function for displaying inventory
    print(bag)
 
def take (item):#function for adding items into the inventory
    if item in bag:
        print("You have too many of these")#all items are unique
        time.sleep(3)
    if item in ['dagger','rock',"gnome's hat", "goblin helmet"]:#the possible options
        if item not in bag: #if the item is not in the bag then add it
            bag.append(item)
    else:
        print("Invalid item") #there is only 4 items

def drop(item): #function to drop items
    if item in bag:
        bag.remove(item)
        print("You discarded " +item)#displays what the player has discarded
        time.sleep(3)
    else:
        print("That item is not in your bag")#invalid inputs, item not in bag

place_list = [] #this is the "map" of the places the player has discovered
def places(location):
    if location in place_list:
        return
    if location not in place_list:#places the location on the map if discovered for the first time
        place_list.append(location)

def show_map():#displays the locations the player can travel to (discovered)
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
        time.sleep(0.05) #the delay of the chars appearing   < the delay from being used in functions seems to be enough                       
        letter += 1 #next char                                           

print("GAME SETTINGS")
print("Type 'speed' for speed run mode ( 4Testing )") #turns off speech loop and cuts wait times for fast testing
print("Type anything else to keep normal settings.")  #keeping normal settings by inputing anything
setting = input()
print ("___ Type adventure() for amazing gamplay ___") #instructions on how to start playing

wait = 5 #averag  wait time used for after speech
loading = 10 #loading screen time to make it feel more like a game
semi_load = 6 #for less long loading screens

if setting == ("speed" or "SPEED"): #The changes the speed setting does to wait times (changes all to 1)
    wait = 1
    loading = 1
    semi_load = 1
#==================================================Follower Intro=============================================================
def adventure (): #function that beggins the game
    player_name = get_name() #gets that player's name
    if player_name == ("Liliput" or "liliput"): #incase you dont want the traveler to make fun of your name
        bag_of_gold(10) #reward for cheating the system
    choice = quest1() #choices on what you do to or with the companion

    if choice == "1": #option 1 follow the gnome on an aventure
        follow_gnome()
    elif choice == "2": #spit on gnome then follow gnome, cause the adventure has to happen                       
        spit()
        no_choice()#game does not give you a choice
    else:
        curse_and_leave()#try to make the gnome go away
        no_choice() #cant make the gnome go away
#==================================================Follower Intro==============================================================
    if choice == "1" or "2" or "3": #any of the choices beggin the quest (adventure)
        loading_Quest1()
        
        good_or_bad = destraction() #runs destraction (Bush with the gnome)
    while good_or_bad not in '12': #there are 2 option, will stay in the loop until user decides
        if good_or_bad in "Ii": #meanwhile the user can use their commands
            show_inventory()
            time.sleep(5)
        if good_or_bad in "rR":
            if 'dagger' not in bag:
                print('You see a dagger')
            print("You see some rocks: Type rock to pick it up")
            print("type 'the item name' to pick it up, hit 'D' to cancel")
            take(input(':'))
        if good_or_bad in "Dd":
            show_inventory()
            print("Type the name of the item you want to drop, if not type anything else")
            drop(input())
        if good_or_bad in "tT":
            show_map()
            print("hit the number that corresponds to the place you want to go")
            print("hit 'x' to exit")
            place = input()
            if place == '1':
                room("town",0,'x')
            else:
                print("That is not a valid place")    
        good_or_bad = destraction()# keeps the user in the part they left off if they use the options

    if good_or_bad == "1":
        friend = dont_throw_gnome() #runs dont_throw_gnome function (good path)
    elif good_or_bad == "2":
        friend = throw_gnome()# run throw_Gnome (Evil path)
    if friend == True: #tests if the frienship with the gnome is good or bad
        player_class = choose_class()# player gets to choose a class for not throwing the gnome
        while player_class not in '1234': #there are 4 class choices 
            if player_class in "iI": #user can use there commands
                show_inventory()
                time.sleep(5)
            if player_class in "rR":
                if 'dagger' not in bag:
                    print('You see a dagger')
                print("You see some rocks: Type rock to pick it up")
                print("type 'the item name' to pick it up, hit 'x' to cancel")
                take(input(':'))
            if player_class in "Dd":
                show_inventory()
                print("Type the name of the item you want to drop, if not hit 'x'")
                drop(input())
            if player_class in "tT":
                show_map()
                print("hit the number that corresponds to the place you want to go")
                print("hit 'x' to exit")
                place = input()
                if place == '1':
                    room("town",0,'x')
                else:
                    print("That is not a valid place")
            player_class = choose_class()#keeps player in the part of the story they reached
        if player_class == "1": #runs warrior function if chosen class is warrior
            warrior()
        elif player_class == "2":#runs rogue function if chosen class is rogue
            rogue()
        elif player_class == "3":# runs mage function if chosen class is mage
            mage()
        elif player_class == "4":#runs rock function if player does not want any special abilities
            rock()

    if friend == False: #tests the friendship
        bad_friend_dia() #run bad_friend_Dia if friendship is broken
        save_or_leave = bad_friend() 
        while save_or_leave not in "12":#2 options
            if save_or_leave in "Ii":# user can freely use their commands
                show_inventory()
                time.sleep(5)
            if save_or_leave in "rR":
                if 'dagger' not in bag:
                    print('You see a dagger')
                print("You see some rocks: Type rock to pick it up")
                print("type 'the item name' to pick it up, hit 'D' to cancel")
                take(input(':'))
            if save_or_leave in "Dd":
                show_inventory()
                print("Type the name of the item you want to drop, if not type anything else")
                drop(input())   
            if save_or_leave in "tT":
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
            save_or_leave = bad_friend()#keeps player in their correct part of the story

        if save_or_leave == "1":#player decides to save the friendship or leave it broken
            friend = save_gnome() # runs save_gnome if player chooses to save the gnome
        else:
            leave_gnome()#run leave_gnome if the player wants to leave gnome
    if friend == True:
        end_loading()# run the end_loading function after completing the quest
        dead = "Goblin helmet" #adds an item to the carvan area showing that player has killed some goblins (good path)
        places('3)Caravan')#adds the caravan to the map
        gold = bag_of_gold(quest_complete_with_gnome()) #gold reward with the gnome splitting the 1000g reward
        print("Type 'quit' to finish")
        print("You have unlocked the gamble option")
        print("You can hit g to play dice with your gnome as long as its alive")
        walk_around = input('[i,r,d,t,g]')#after the quest the player can travel and inspect the sites discovered freely
        while walk_around != "quit":
            if walk_around in "gG":
                gamble()
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
            print("Type 'quit' to finish") # player can quit the game by typing quit
            walk_around = input('[i,r,d,t,g]')
    else:
        end_loading()
        dead = "Gnome's hat" #item that appears if gnome was left, showing that he probably died
        gold = bag_of_gold(quest_complete_without_gnome()) #gold reward without gnome of 1000g
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
            print("Type 'quit' to finish") #player can type quit to exit game
            walk_around = input('[i,r,d,t]')
    return
########__GAMEPLAY__##################__GAMEPLAY__##################__GAMEPLAY__##################__GAMEPLAY__##########
#Town##Town##Town##Town##Town##Town##Town##Town##Town##Town##Town##Town##Town##Town##Town##Town##Town##Town##Town##Town#
def get_name ():
    #print("You Discovered the Town!!!")#_______________________________________________Room 0.0 = TOWN
    places("1)The Town")
    print("*You find yourself in a small town*")
    print("          s      *                            *            ")
    print("        s                 *          *              *        ")
    print("  *       s             *          *                         ")
    print("     /\ ||   *                                *             ")
    print("    /  \||        /\         *         *        *          *    ")
    print("   /    ||  *    /..\         *                              ")
    print("  /      \      /....\ *              *  *                     ")
    print(" /________\    /......\                        __     *        ")    # true art 
    print(" |        |   /........\     *                /  \            ")
    print(" | []  [] |  /----------\   _________  *     /|  |\          ")
    print(" |        |  |	       |  |Town Hall|   /\ /\|__|/\ /\     ")
    print(" |        |  |[] []  [] |  | []   [] |   [] ||_/\_|| []    ")
    print(" |        |  |     _	   |  |         |   ||_||____||_||    ")
    print("_|___[]___|__|____| |___|__|___[ ]___|___||____[]____||____")
    time.sleep(wait)
    talk("Gnome: Greetings traveler! My name is Liliput the gnome!!! and you are? (^̮^)")
    player_name = input("...") #waiting for a user input
    if player_name == ("liliput" or "Liliput"):
        talk("Gnome: GREAAT NAAME! but that's not gonna stop me from calling you by your real name. My little bootlicker~ (^̮^)")#Faces so extra annoying effect
        print("*The gnome gives you 10 gold for attempting to cheat the system")
        time.sleep(wait)
    elif len(player_name) <= 2:
        talk("Gnome: Come on, atleast try to think of a real name, but thats okay your name is Bootlicker now (^̮^)")
        time.sleep(wait)
    else:
        talk("Gnome: Thats a terrible name! i'ma call you bootlicker instead (^̮^)") #most likely outcome
        print ("*laughs obnoxiously*")
        time.sleep(wait)
    return player_name

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
def follow_gnome ():
    talk("GREAT!! I knew i'd convince you. Follow me! We gonna be so rich you and me!! I'm talking big money [̲̅$̲̅(̲̅5̲̅)̲̅$̲̅]")
    return
def spit ():
    print("*Gnome spits back*")
    time.sleep(wait)
    return
def curse_and_leave ():
    print("*Gnome follows you as you walk away*(^̮^)")
    time.sleep(wait)
    talk (".  .  .  .")
    print("The gnome doesn't seem to understand no for an answer")
    time.sleep(wait)
    return
def no_choice (): 
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
def loading_Quest1 (): #info and gnome explaining
    print("**LOADING amazing aventure game**") #This is to give a little context on what goblins are (like wow "tips")

    green("              ______    ")
    green("        |\   /------\   /|")   
    green("        | \ /        \ / |")
    green("        \  \   o\/o   /  /") 
    green("         \_,   |  |   ,_/") 
    green("          \    \__/    / " )
    green("           \  ______  /")   
    green("         ___\ \|--|/ /__")  
    green("       /     \      /     \ ")
    green("      /       ------       \ ")
    print("INFO: Goblins are rude creatures and could be dangerous in large numbers and are known for their greed and great riches")
    print("TIP: You may type r or R to show the items in your vicinity.")    
    time.sleep(loading)
    talk("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    talk("Gnome: GEEZzZ LOUISE! That was some looong~ loading screen!!")
    time.sleep(wait)
    print("[*Liliput brought you deep into The Goblin Forest*]")
    
    print("     *      -0-        .        *  .         ")
    print("        .                .  *       - )-     ")
    print("    .      *       o       .       *         ")
    print("  o                |                    *    ")
    print("     *      .     -O-         *    .         ")
    print("             .     -O-                       ")
    print("  .                 |        *      .    -0- ")
    print("         *  o     .    '       *      .    o ")
    print("                .         .        |       * ")
    print("     *             *              -O-       . ")
    green("  @@@@@      @@@@@@                   @@@     ")        
    green(" @@@@@@@    @@@@@@@@   @@@@   @@@@@  @@@@@    ")      
    green("@@@@@@@@@   @@@@@@@@@ @@@@@@ @@@@@@ @@@@@@@   ")      
    green(" @@@@@@      @@@@@@   @@@@@@ @@@@@@ @@@@@@@   ")        
    print("   ||          ||       ||     ||     ||       ")          
    print("___||__________||_______||_____||_____||______ ")        
    time.sleep(wait)
    print("*Hiding in a bush* You and you Liliput are examining a nearby goblin camp")
    time.sleep(wait)
    purple("*You have discovered the bush*")#_______________________________Room 1.0 = BUSH AREA
    time.sleep(wait)
    print("*You notice bags of gold being loaded into a caravan*")
    print("                        ________________              o       o                ")
    print("  ((^--_________       | [][] |[]|  __  |            /|\     /|\  \/'\/        ")
    print("  | /\  --___ __  \    |      | .| |__| |    o       / \     / \  )===(        ")
    print("   (  /  \  ) \     \_ | ___  |  | ___  |   /|\                  /  $  \       ")     
    print("   / |   /  \  \       [( O )_|__|( O ) ]   / \                 (_______)      ")
    time.sleep(wait)
    purple("*You have discovered the caravan*")#__________________________________Room 1.1 = CARAVAN AREA 4later
    time.sleep(wait)
    talk("Gnome: Here's my old bag, you can use this to put all kinds of things!")
    print("*The gnome hands you a dusty linen bag")
    time.sleep(wait)
    purple("Congradulations you have unlocked the inventory! (i opens inventory)")
    time.sleep(wait)
    purple("You can hit 'r' to see what is in your vacinity")
    talk("Gnome: Okay so here's the plan. . .")
    time.sleep(2)
    talk("Gnome: We gonna rob these leper gnomes by stealing that caravan. Here's a dagger incase of EMERGENCY. . (@_@)")
    print("*Gnome hands you a rusty dagger*")
    time.sleep(1)
    print("*You put the dagger in your bag*")
    print("   ()")
    print("   ||")
    print("  o==o")
    print("   ||")
    print("   ||")
    print("   \/")
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
        
def throw_gnome ():#______________________________________________________________Room 1.0 BUSH AREA
    friendship = False
    talk("Gnome: AAAAHHHHHHHHH!!!!!")
    time.sleep(wait)
    print("*You throw the gnome*")
    print("Goblins are destracted killing your only friend, leaving the caravan completely vulnerable")
    time.sleep(wait)
    return friendship

def dont_throw_gnome ():#___________________________________________________________Room 1.0 BUSH AREA
    friendship = True
    talk("Gnome: Great!!")
    print("Options") #This is kinda like class selection
    red("1)*Charge into the goblins like a true warrior!")
    yellow("2)*stealth and sap* the goblins like a sneeky rogue assassin!")
    cyan("3)*Freeze* the goblins like the powerful mage you are!")
    if 'rock' in bag:
        print("4)throw your rock at the goblins")
    return friendship

def choose_class ():#___________________________________________________________Room 1.0 BUSH AREA
    class_choice = input("Choose [1,2,3,4,i,r,d,t]")
    return class_choice
def warrior ():#___________________________________________________________Room 1.1 CARAVAN AREA
    playerClass = "Warrior" 
    places('2)Bush')
    purple("*You entered the Caravan area")
    red("*You charge into the goblins knocking them all out")
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
    purple("*You entered the Caravan area")
    yellow("*You turn invisible and knock all goblins cold that were surrounding the caravan*")
    time.sleep(wait +1)
    talk("Gnome: Heyy~ bootlicker. How many butts does an assassin have?")
    time.sleep(wait)
    talk("Gnome: THEY HAVE TWO!! HAHAHAHhaah... Get it? cause ASSASSin HAHaahaAHAH")
    print("*gnome continues to laughing the entire way to the caravan*")
    return 

def mage ():#___________________________________________________________Room 1.1 CARAVAN AREA  
    playerClass = "Mage"
    places('2)Bush')
    purple("*You entered the Caravan area")
    cyan("*You use a freezing spell* freezing all goblins surrounding the caravan*")
    time.sleep(wait)
    talk("Gnome: Woah!! That was so cool! HAHA get it? THAT WAS 'COOOOOOL~' (^̮^) ")
    print("*You can tell the gnome is trying to hold in his laughter the entire way to the caravan*")
    return

def rock ():#___________________________________________________________Room 1.1 CARAVAN AREA
    drop('rock')
    places('2)Bush')
    purple("You have entered the Carvan area")
    print("*You throw a rock you found but missed because you're a boring human")
    print("*Liliput judges you*")
    playerClass = "Boring Human"
    time.sleep(wait)
    print("*The goblins draw all their attention on the rock you threw leaving the caravan vulnerable (least it got the job done)")
    time.sleep(4)
    return

def bad_friend_dia ():#___________________________________________________________Room 1.1 CARAVAN AREA                                                                                      
    talk("Gnome: HELP!! I DON'T WANT TO DIE!")                                                          
    time.sleep(1)                                                                                       
    talk("Gnome: THEIR GONNA EAT ME")
def bad_friend():
    places('2)Bush')                                                                 
    print("*Gnome cries*")                                                                              
    print("Options")                                                                                    
    print("1) run over the goblins with the caravan saving the little gnome from being eaten")          
    print("2) Drive away, leaving the poor gnome to die")                                               
    gnomeIsGonnaDie = input("[1,2,r,i,d,t]")                                                                    
    return gnomeIsGonnaDie                                                                              

def save_gnome():#___________________________________________________________Room 1.1 CARAVAN AREA                                                                                        
    friendShip = True                                                                                   
    print("*You run over all the goblins")                                                              
    talk("Gnome: YOU CAME BACK FOR ME !! (^̮^) ")                                                                                                                                              #
    print("*The little gnome quickly hops into the caravan*")                                           
    time.sleep(2)                                                                                       
    talk("Gnome: That was intense, i thought you were gonna leave me for a second :C")                  
    time.sleep(2)                                                                                       
    talk("Gnome: WE GOT THE 'BIG MONEY' THOUGH, thats what matters \(^o^)/")                            
    return friendShip                                                                                   
                                                                                                        
def leave_gnome():#___________________________________________________________Room 1.1 CARAVAN AREA                                                                                       
    talk("Gnome: (ToT)")                                                                                                                                                                #
    return                                                                                              
#back to town##back to town# #back to town# #back to town# #back to town# #back to town# #back to town#   
def end_loading (): #< Transitioning effect
    time.sleep(2) 
    places("3)Caravan")             
    print("Leaving Instance")  
    print("LOADING...")         
    time.sleep(semi_load)              
    return
def quest_complete_without_gnome (): #without gnome    #_______________________________________________Room 0.0 = TOWN
    print("*You arrive back to town in the caravan by yourself*")
    time.sleep(2)
    print("*You search the caravan and keep all the gold*")
    print("_____Quest Complete_____")
    return 1000
def quest_complete_with_gnome (): #with gnome        #_______________________________________________Room 0.0 = TOWN
    talk("Gnome we make a good team you and I. <3")
    print("You and your annoying friend return to town with the caravan and share the reward")
    print("_____Quest Complete_____")
    return 500
def bag_of_gold (a):
    amount = a
    print ("You earned ",amount," gold")
    time.sleep(wait)
    return gold
