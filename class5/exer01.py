#!/usr/bin/env python

'''
demo using ansible to gen config files
'''

# imports
try:
    import ansible
    import yaml
except ImportError:
    print "Could not import a required module.\n Exiting"
    raise SystemExit


# Variables
device_file = 'device_list01.yaml'


def main():
    '''
    main app
    '''

    # get list of devices to gen configs for
    with open(device_file,'r') as yaml_file:
        device_list = yaml.load(yaml_file)

    print device_list


if __name__ == "__main__":
    main()
