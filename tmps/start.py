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
# imports
from time import sleep
import random
import sys
import enquiries
import subprocess
import os
from os import system, name
import yaml
import starttexts

# define important variables
language = ""
installpath = ""
config = ""

#
# how to load the config file
#
def read_yaml(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)

#
# load settings and set values for variables
#
def load_settings():
    global language
    global installpath
    global config
    config = read_yaml("tmps/config.yaml")
    installpath = config["installpath"]
    if config["language"] == "english":
        language = starttexts.english
    elif config["language"] == "deutsch":
        language = starttexts.deutsch
    return
# load them already
load_settings()

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
        print(letter, end = '')
    print("")

#
# to change programmlanguage
#
def changelanguage():
    global language
    choice = enquiries.choose(language['chooselanguage'], starttexts.list_languages)
    with open('tmps/config.yaml') as f:
        doc = yaml.load(f)
    doc['language'] = choice
    with open('tmps/config.yaml', 'w') as f:
        yaml.dump(doc, f)
    load_settings()

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
        else:
            menulist.append(language[names])
            folders.append(names)
    menulist.append(language['changelanguage'])
    menulist.append(language['exit'])
    choice = enquiries.choose(language['menugreeter'], menulist)
    choice = list(language.keys())[list(language.values()).index(choice)]
    typewriter(f"{language['menuchoice']} {language[f'{choice}']}")
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
if __name__ == "__main__":
    clear()
    changelanguage()
    clear()
    typewriter(language['programmstart'])
    while True:
        menu(installpath)
        clear()
        typewriter(language['programmgreeter'])
else:
    print("Never import the main module!")