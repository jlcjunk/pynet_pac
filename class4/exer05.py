#!/usr/bin/env python

'''
pexpect demo using netmiko to enter config mode
'''

# imports
try:
    import netmiko
except ImportError:
    print "Could not import a required module.\n Exiting"
    raise SystemExit


# Variables
RTR = {
    'host':'pynet-rtr2',
    'device_type':'cisco_ios',
    'ip':'184.105.247.71',
    'username':'pyclass',
    'password':'88newclass',
    'secret':'',
    'port':22,
    'timeout':60
    }




def main():
    '''
    main app
    '''

    rtr_connection = netmiko.ConnectHandler(**RTR)

    print rtr_connection.find_prompt()

    rtr_connection.config_mode()

    print rtr_connection.check_config_mode()

    print rtr_connection.find_prompt()


if __name__ == "__main__":
    main()
