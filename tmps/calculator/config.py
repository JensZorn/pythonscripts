import yaml
import calculatortexts
from ..config import *

if config["language"] == "english":
    language = calculatortexts.english
elif config["language"] == "deutsch":
    language = calculatortexts.deutsch