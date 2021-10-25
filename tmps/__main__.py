# -*- coding: UTF-8 -*- ###############################################################
#!/usr/bin/env python3
#                             <°))))><
#
#               Main menu for my small projects
#
#               by Jens Zorn
#
#
#               I wrote this to list my projects and to access them using a menu.
#               The scripts is searching for child directories and automatically lists them
#               as options in the menu if they are defined within the language files
#               (found in config directory).
#               The subpackages must contain an __init__.py file which executes the
#               subpackage to run properly.
#               Additionally you can change the language of the program.
#
#
#               /o)_/_/_/__/ )          --         ( \__\_\_\_(o\
#               \ ) \ \ \  \ )          --         ( /  / / / ( /
#######################################################################################
# imports
from time import sleep
from importlib import import_module
import random
import sys
import enquiries
import os
from os import system, name
from config import config
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
    choice = enquiries.choose(config.language['chooselanguage'], config.list_languages)
    with open('tmps/config/config.yaml') as f:
        doc = yaml.load(f)
    doc['language'] = choice
    with open('tmps/config/config.yaml', 'w') as f:
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
        import_module(choice)
        del sys.modules[choice]



#
# to exit programm
#
def exit():
    sys.exit()



# imports
#import tmps
#from config import config

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