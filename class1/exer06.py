#!/usr/bin/env python


# import needed modules
import yaml
import json
import pprint


# create list
list = ["text1",3.14159,{"router.ip":"192.168.1.1","router.model":"Cisco2811","switch.ip":"192.168.2.1","switch.model":"3750","router.uptime":"654"},"lemon"]



# write YAML file
yaml_file = open('list.yaml', 'w')
yaml_file.write("---\n")
yaml_file.write(yaml.dump(list,default_flow_style=False))
yaml_file.close()




# write JSON file
json_file = open('list.json', 'w')

print "Complete"



