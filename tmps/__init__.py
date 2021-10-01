# -*- coding: UTF-8 -*- ###############################################################
#!/usr/bin/env python3
#                             <°))))><
#
#               Main menu for my small projects
#
#               by Jens Zorn
#
#
#               Additional information can be found in tmps.py
#
#
#               /o)_/_/_/__/ )          --         ( \__\_\_\_(o\
#               \ ) \ \ \  \ )          --         ( /  / / / ( /
#######################################################################################
# imports
import tmps
from config import config

#
# everything starts here
#
if __name__ == "__main__" or __name__ == "start":
    tmps.clear()
    tmps.changelanguage()
    tmps.clear()
    tmps.typewriter(config.language['programmstart'])
    while True:
        tmps.menu(config.installpath)
        tmps.clear()
        tmps.typewriter(config.language['programmgreeter'])
else:
    print("Never import the main module!")
    print(__name__)