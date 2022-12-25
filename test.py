import pprint
import json
import pandas as pd

with open('sample.json', 'r') as openfile:
 
    # Reading from json file
    json_object = json.load(openfile)

# pprint.pprint(json_object[["title"]])
pprint.pprint(json_object)