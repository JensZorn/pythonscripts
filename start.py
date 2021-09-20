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

# global variables / config
global language
language = "english"


def typewriter(input):
    for letter in str(input):
        seconds = random.uniform(0, 0.02)
        sleep(0) #in seconds
        sys.stdout.write(letter)

