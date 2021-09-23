import yaml
from calculatortexts import *

def read_yaml(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)

test = read_yaml("tmps/config.yaml")
print(test["APP"])
global language
if test["APP"]["LANGUAGE"] == "english":
    language = english
if test["APP"]["LANGUAGE"] == "deutsch":
    language = deutsch