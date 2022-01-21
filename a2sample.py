# coding: utf-8
#
# COMP 1631 a2.py
#
# Name: 
#
 
""" 
Title for your adventure:   Dr. Matt's Quest with Functions. (update this with your own title!)
 
"""
 
import time

def adventure():
    """ this function runs one session of interactive fiction
        inputs: no inputs    (prompted text doesn't count as input)
        outputs: no outputs  (printing doesn't count as output)
    """
    delay = 1.0          # change to 0.0 for testing/speed runs; larger for dramatic effect!
    
    username = getName()
    display_welcome_message(delay)
    plot_choice = choose_a_plot_to_follow()
    if plot_choice=='yes':
        follow_murder_plot(delay)
    else:
        follow_boring_plot(delay+5)
    return

def getName(): 
    """ this function gets the adventure game user's name
        inputs: no inputs 
        outputs: a string containing the name 
    """   
    name = input('Hello stranger, do you have a name? [type your name, please] ')
    if name == 'Doug':
        print('It seems that your parents loved you very much...')
    else:
        print('I guess that could be a name...')
    return name

def display_welcome_message(a_delay):
    """ this function displays a welcome message at the beginning of the game
        inputs: a float corresponding to a delay for message display
        outputs: no outputs 
    """
    print()
    time.sleep(a_delay)
    print('...Me? I am Bina Ry, ruler of all things digital.')
    return 

def choose_a_plot_to_follow():
    """ this function runs one session of interactive fiction
        inputs: no inputs    (prompted text doesn't count as input)
        outputs: a string containing the answer to a question
    """
    query = input('Were you sent to solve the murder of Powe Rsu Pply? [yes/no] ')    
    return query

def follow_murder_plot(a_delay):
    """ this function runs one session of the murder plot option of the adventure game
        inputs: a float corresponding to a delay for message display
        outputs: no outputs  
    """
    print('Very well, let me take you to their corpse.')
    print('Be careful... it has been very dark since they passed.')
    investigate=input('Here we are, what part of the body would you like to examine? [cable/other] ')
    if investigate == 'cable':
        print('There are burn marks, this was definitely intentional')
    else:
        print('There\'s a dent in her case, and her capacitors have been forcefully ripped from her body')
        time.sleep(a_delay)
        print('Seems like it was natural causes after all!')
        print()
        print()
        print('Well, now that that is settled, I, Bina Ry, officially appoint you '+user_name+': Royal Supervisor of Drying Paint!')
        print('Please follow me to your throne: The Stool of a Thousand Lumps!')		
    return

def follow_boring_plot(a_delay):
    """ this function runs one session of the boring plot option of the adventure game
        inputs: a float corresponding to a delay for message display
        outputs: no outputs  (printing doesn't count as output)
    """
    print('Ah, yes yes, then surely you are the one that has been sent to supervise the drying of the new paint on our case-tle walls!...')
    time.sleep(a_delay)
    print('You definitely look like someone who would rather watch paint dry than solve a murder.')
    print('Please follow me to your throne: The Stool of a Thousand Lumps!')
    print('Bina Ry grabs you forcefully by the arm, and takes you to toward the edge of his kingdom.')
    print('Well, here is your stool... I would say get comfortable but you know...')
    print()
    return