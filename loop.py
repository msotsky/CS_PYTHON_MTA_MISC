import os
import time


def talk (talking):
    letter = 0
    while letter <= len(talking): 
        os.system('cls') 
        print (talking[:letter])
        time.sleep(0.05)
        letter += 1
    
talk("Gnome: GREAAT NAAME! but that's not gonna stop me from calling you by your real name. My little bootlicker~ (^̮^)")
