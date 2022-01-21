# coding: utf-8
#
# COMP 1631 a1.py
#
# Name: 
#
 
""" 
Title for your adventure:   Dr. Matt's Quest. (update this with your own title!)
 
"""
 
import time

def adventure():
    """ this function runs one session of interactive fiction
        inputs: no inputs    (prompted text doesn't count as input)
        outputs: no outputs  (printing doesn't count as output)
    """
    delay = 0.0          # change to 0.0 for testing/speed runs; larger for dramatic effect!
    
    username = input('Hello stranger, do you have a name?')
    if username == 'Doug':
        print('It seems that your parents loved you very much...')
    else:
        print('I guess that could be a name...')

    print()
    time.sleep(delay)
    print('...Me? I am Bina Ry, ruler of all things digital.')
    follow_murder_plot = input('Were you sent to solve the murder of Powe Rsu Pply? [yes/no]')

    if follow_murder_plot == 'yes':
        murder_plot = True
        print('Very well, let me take you to their corpse.')
        print('Be careful... it has been very dark since they passed.')
    else:
        murder_plot = False
        boring_plot=input('Ah, yes yes, then surely you are the one that has been sent to supervise the drying of the new paint on our case-tle walls!')

    if not murder_plot:
        print('You definitely look like someone who would rather watch paint dry than solve a murder.')
        print('Please follow me to your throne: The Stool of a Thousand Lumps!')
        print('Bina Ry grabs you forcefully by the arm, and take you to toward the edge of his kingdom.')

    time.sleep(delay)
    if murder_plot:
        investigate=input('Here we are, what part of the body would you like to examine? [cable/other]')
        if investigate == 'cable':
            print('There are burn marks, this was definitely intentional')
        else:
            print('There\'s a dent in her case, and her capacitors have been forcefully ripped from her body')
            time.sleep(delay)
            print('Seems like it was natural causes after all!')
            print()
            print()
            print('Well, now that that is settled, I, Bina Ry, officially appoint you '+user_name+': Royal Supervisor of Drying Paint!')
            print('Please follow me to your throne: The Stool of a Thousand Lumps!')		
    else:
        print('Well, here is your stool... I would say get comfortable but you know...')
