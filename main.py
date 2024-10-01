import keyboard
import time
import os
import survey
from art import *

def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

mainloop = True
while mainloop:

    tprint("Anti LS")
    print("UKE PC standard lockscreen activates after 2 minutes of inactivity")
    print("Press the key that you want the program to repeat every set amount of time")
    print("(f8 isn't really used for anything)")
    print("\nWaiting for input...")

    settingRepeatKey = True
    while settingRepeatKey:
        keyEvent = keyboard.read_event()

        if keyEvent.event_type == keyboard.KEY_DOWN:
            keyToPress = keyEvent.name
            print(f"Key '{keyToPress}' selected for repetition")
            settingRepeatKey = False
    

    inputting = True
    while inputting:
        value = survey.routines.numeric("Interval in seconds: ")

        if value <= 0:
            print("Input a positive number")
        else:
            inputting = False

    clearConsole()
    
    tprint("Anti LS")
    print("Hold the 'Backspace' at any time to cancel")
    print("The program will continue to run in the background if minimized")
    print(f"Cancels lock screen every {value} seconds with '{keyToPress}'\n")

    stat = 0
    active = True
    interval = 0.1
    total_time = 0

    while active:
        if keyboard.is_pressed("backspace"):
            active = False
            print("\nBackspace pressed, exiting the loop")
            break
        
        # Instead of sleeping for the whole 'value' time, we sleep in small intervals
        time.sleep(interval)
        total_time += interval

        # Once the accumulated time reaches the user-defined value, send the key
        if total_time >= value:
            keyboard.send(keyToPress)
            stat += 1
            print(f"\rStopped the inevitable lockscreen from taking over {stat} times", end="", flush=True)
            total_time = 0  # Reset the timer
