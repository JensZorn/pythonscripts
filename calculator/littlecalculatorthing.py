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
import enquiries
from littlecalculatorthingtexts import *


# global variables
#global start
#start = 1    
global language
language = english

# functions
class math():
# typewriter effect
    def typewriter(input):
        for letter in str(input):
            seconds = random.uniform(0, 0.02)
            sleep(0) #in seconds
            sys.stdout.write(letter)

# greeter and menu
    def startprogramm():
        
        math.language()


# navigate through options
#    def navigator(menu_option):
#        if menu_option == 1:
#            math.typewriter(language['calculatorgreeter'])
#            math.calculator()
#        elif menu_option == 2:
#            math.typewriter(language['convertergreeter'])
#            math.converter()
#        elif menu_option == 9:
#            math.language(2)
#        elif menu_option == 0:
#            sys.exit()
#        elif menu_option == "menu":
#            math.menu()

# menu to choose where to navigate
    def menu():
        options = [language['calculator'], language['converter'], language['chooselanguage'], language['exit']]
        choice = enquiries.choose('Wähle! ', options)
        getattr(math, choice)()


# function to change program language
    def language():
        global language
        options = "english", "deutsch"
        choice = enquiries.choose('Wähle! ', options)
        getattr(math, choice)()

        math.typewriter(language['greeterchooselang'])
        lang = input()
        lang = int(lang)
        if lang == 1:
            language = english
        math.menu()
    #elif lang == 2:
    #    language = deutsch
    #    if a == 1:
    #        pass
    #    elif a == 2:
    #        math.menu()

# this will be the actual calculator
    def calculator():
        while True:
            try:
                print(language['calculatormenu'])
                eq = input()
                if eq == "menu":
                    math.menu()
                else:
                # evtl alternative zu eval ausprobieren, oder die gefährlichen Ausdrücke verbieten. Recherche!
                    print(language['results'], str(eval(eq)))
                    math.calculator()
            except ValueError:
                print("Try again")
            except NameError:
                print("Try again")
            except SyntaxError:
                print("Try again")
            else:
                break

# and this will be the converter for different values
    def converter():
        conv = input()
        if conv == "menu":
            math.menu()
        else:
            math.converter()

# exit programm
    def exit():
        sys.exit()

if __name__ == "__main__":
    math.startprogramm()
else:
    print("This is the main module. You may not import it!")