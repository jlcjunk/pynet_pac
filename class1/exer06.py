#!/usr/bin/env python


# import needed modules
import yaml
import json
import pprint


# create list
list = ["text1",3.14159,{"router.ip":"192.168.1.1","router.model":"Cisco2811","switch.ip":"192.168.2.1","switch.model":"3750","router.uptime":"654"},"lemon"]



# write YAML file
with open('list.yaml', 'w') as yaml_file:
    yaml_file.write("---\n")
    yaml_file.write(yaml.dump(list,default_flow_style=False))




# write JSON file
with open('list.json', 'w') as json_file:
    json.dump(list,json_file)


# note program is done due to lack of other output
print "Complete"



