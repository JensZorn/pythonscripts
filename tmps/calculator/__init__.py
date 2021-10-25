
# -*- coding: UTF-8 -*- ###############################################################
#!/usr/bin/env python3
#                             <°))))><
#
#               calculator script
#
#               by Jens Zorn
#
#
#               - used with a simple selfmade CLI
#               - currently uses eval() to evaluate the input, security issues to solve!
#               - converter is not yet ready to use
#               - still needs translation and other things
#
#
#               /o)_/_/_/__/ )          --         ( \__\_\_\_(o\
#               \ ) \ \ \  \ )          --         ( /  / / / ( /
#######################################################################################
from time import sleep
import sys
import random
import enquiries
from config import config

#def read_yaml(file_path):
#    with open(file_path, "r") as f:
#        return yaml.safe_load(f)

#test = read_yaml("tmps/config.yaml")
#print(test["APP"])


# global variables
#global start
#start = 1    
#global language
#language = test["APP"]["LANGUAGE"]

# functions
class math():
# typewriter effect
    def typewriter(input):
        for letter in str(input):
            seconds = random.uniform(0, 0.02)
            sleep(seconds) #in seconds
            sys.stdout.write(letter)

# greeter and menu
    def startprogramm():
        print(config.language["greetermenutextstart"])
        math.menu()


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
        options = [config.language['calculator'], config.language['converter'], config.language['exit']]
        choice = enquiries.choose('Wähle! ', options)
        getattr(math, choice)()


# function to change program language
#    def language():
#        global language
#        options = "english", "deutsch"
#        choice = enquiries.choose('Wähle! ', options)
#        if choice == "english":
#            language = english
#        elif choice == "deutsch":
#            language = deutsch
#        print(language)
#        math.menu()
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
                print(config.language['calculatormenu'])
                eq = input()
                if eq == "menu":
                    math.menu()
                else:
                # evtl alternative zu eval ausprobieren, oder die gefährlichen Ausdrücke verbieten. Recherche!
                    print(config.language['results'], str(eval(eq)))
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
        pass



math.startprogramm()
