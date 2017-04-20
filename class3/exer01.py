#!/usr/bin/env python

'''
create first data file
'''

# imports
try:
    import sys
    import pysnmp
    import yaml
    import telnetlib
    import time
    import snmp_helper
except ImportError:
    print "Could not import a required module.\n Exiting"
    raise SystemExit


# Variables
DATA_FILE = 'dev_list'


# create seed data structure
device_list = {
    'pynet-rtr2':['184.105.247.71',161,'pysnmp','SHA','galileo1','AES','galileo1','1.3.6.1.4.1.9.9.43.1.1.1.0','0'],
    'pynet-rtr1':['184.105.247.70',161,'pysnmp','SHA','galileo1','AES','galileo1','1.3.6.1.4.1.9.9.43.1.1.1.0','0']
    }

# print device list
print '\n'
print device_list
print '\n'


# create data file
with open(DATA_FILE + '.yaml', 'w') as yaml_file:
    yaml_file.write(yaml.dump(device_list,default_flow_style=None,width=120))


# read YAML file
with open(DATA_FILE + '.yaml','r') as yaml_file:
    device_list = yaml.load(yaml_file)



# print reconstituted data so I know it ended w/o dieing and data reads ok
print '\n' 
print device_list
print '\n'


