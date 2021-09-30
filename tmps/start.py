#######################################################################################
#
#
#               A small programm to calculate some things
#
#                           by Jens Zorn
#
#
#
#######################################################################################
#!/usr/bin/env python3
# imports
from time import sleep
import random
import sys
import enquiries
import subprocess
import os
from os import system, name
import config
import starttexts
import yaml

#
# to clear the console
#
def clear():
    # windows
    if name =='nt':
        _ = system('cls')
    # MacOS and Linux
    else:
        _ = system('clear')

#
# typewriter effect for text
#
def typewriter(input):
    for letter in str(input):
        seconds = random.uniform(0, 0)
        sleep(seconds) #in seconds
        print(letter, end='')
    print("")

#
# to change programmlanguage
#
def changelanguage():
    global language
    choice = enquiries.choose(config.language['chooselanguage'], starttexts.list_languages)
    with open('tmps/config.yaml') as f:
        doc = yaml.load(f)
    doc['language'] = choice
    with open('tmps/config.yaml', 'w') as f:
        yaml.dump(doc, f)
    config.load_settings()

#
# menu of the programm
# which automatically includes first level subfolders as options to choose from
#
def menu(installpath):
    subfolders = [f.name for f in os.scandir(installpath) if f.is_dir()]
    folders = []
    menulist = []
    dontshow = ["__pycache__"]
    for names in list(subfolders):
        if names in dontshow:
            continue
        elif names not in config.language:
            continue
        else:
            menulist.append(config.language[names])
            folders.append(names)
    menulist.append(config.language['changelanguage'])
    menulist.append(config.language['exit'])
    choice = enquiries.choose(config.language['menugreeter'], menulist)
    choice = list(config.language.keys())[list(config.language.values()).index(choice)]
    typewriter(f"{config.language['menuchoice']} {config.language[f'{choice}']}")
    if choice == 'exit':
        exit()
    elif choice == 'changelanguage':
        changelanguage()
    else:
        subprocess.check_call(["python3.9", f"tmps/{choice}/{choice}.py"])

#
# to exit programm
#
def exit():
    sys.exit()


#
# everything starts here
#
if __name__ == "__main__" or __name__ == "start":
    clear()
    changelanguage()
    clear()
    typewriter(config.language['programmstart'])
    while True:
        menu(config.installpath)
        clear()
        typewriter(config.language['programmgreeter'])
else:
    print("Never import the main module!")
    print(__name__)
