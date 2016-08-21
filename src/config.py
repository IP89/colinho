from json import load
from os import access, R_OK
from sys import modules

def parse(files):
    with open(next(f for f in files if access(f, R_OK))) as c:
        return load(c)

modules[__name__] = parse(['../config.json'])
