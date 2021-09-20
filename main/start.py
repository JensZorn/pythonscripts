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
import os

# global variables / config
global language
language = "english"


def typewriter(input):
    for letter in str(input):
        seconds = random.uniform(0, 0.02)
        sleep(0) #in seconds
        sys.stdout.write(letter)


#filepaths = [f.path for f in os.scandir('.') if f.is_file()]
#dirpaths  = [f.path for f in os.scandir('.') if f.is_dir()]
#print(filepaths)
#print(dirpaths)