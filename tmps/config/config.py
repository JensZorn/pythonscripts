# -*- coding: UTF-8 -*- ###############################################################
#!/usr/bin/env python3
#                             <°))))><
#
#               Config script
#
#               by Jens Zorn
#
#
#               - config script, parses information from config.yaml and decides which
#               translation to use
#               - this is the module to be imported in other scripts
#
#
#               /o)_/_/_/__/ )          --         ( \__\_\_\_(o\
#               \ ) \ \ \  \ )          --         ( /  / / / ( /
#######################################################################################
import yaml
from . import english, deutsch


list_languages = ["english", "deutsch"]
# define important variables
global language
global installpath
language = ""
installpath = ""

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
    config = read_yaml("tmps/config/config.yaml")
    installpath = config["installpath"]
    if config["language"] == "english":
        language = english.english
    elif config["language"] == "deutsch":
        language = deutsch.deutsch
    return

load_settings()