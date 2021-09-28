import yaml
import yaml
import starttexts

# define important variables
global language
global installpath
global config
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

config = read_yaml("tmps/config.yaml")
installpath = config["installpath"]
if config["language"] == "english":
    language = starttexts.english
elif config["language"] == "deutsch":
    language = starttexts.deutsch
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
