from json import load
from os import access, R_OK
from sys import modules

def parse(file):
    return load(open(file)) if access(file, R_OK) else {}

modules[__name__] = parse('../config.json')
