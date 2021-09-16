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
from time import sleep
import sys
import random
from littlecalculatorthingtexts import *


# global variables
global start
start = 1    
global language
language = english

# functions

# typewriter effect
def typewriter(input):
    for letter in str(input):
        seconds = random.uniform(0, 0.02)
        sleep(0) #in seconds
        sys.stdout.write(letter)

# greeter and menu
def startprogramm():
    global start
    if start == 1:
        changelang(1)
        typewriter(language['greetermenutextstart'])
        menu_option = input()
        start = 2
        navigator(int(menu_option))
    else:
        print("We encountered an error. Please restart the programm.")

# navigate through options
def navigator(menu_option):
    if menu_option == 1:
        typewriter(language['calculatorgreeter'])
        calculator()
    elif menu_option == 2:
        typewriter(language['convertergreeter'])
        converter()
    elif menu_option == 9:
        changelang(2)
    elif menu_option == 0:
        sys.exit()
    elif menu_option == "menu":
        menu()

# menu to choose where to navigate
def menu():
    typewriter(language['greetermenutext'])
    menu_option = input()
    navigator(int(menu_option))

# function to change program language
def changelang(a):
    global language
    typewriter(language['greeterchooselang'])
    lang = input()
    lang = int(lang)
    if lang == 1:
        language = english
    #elif lang == 2:
    #    language = deutsch
    if a == 1:
        pass
    elif a == 2:
        menu()

# this will be the actual calculator
def calculator():
    eq = input()
    if eq == "menu":
        menu()
    else:
        print(language['results'], str(eval(eq)), language['calculatormenu'])
        calculator()

# and this will be the converter for different values
def converter():
    conv = input()
    if conv == "menu":
        menu()
    else:

        converter()



if __name__ == "__main__":
    startprogramm()
else:
    print("This is the main module. You may not import it!")