#!/usr/bin/env python


# import needed modules
import yaml
import json
import pprint




# read YAML file
with open('list.yaml','r') as yaml_file:
    data_yaml = yaml.load(yaml_file)


# read JSON file
with open('list.json','r') as json_file:
    data_json = json.load(json_file)



# print YAML
pprint.pprint(data_yaml)

# print YAML
pprint.pprint(data_json)

