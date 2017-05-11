#!/usr/bin/env python

'''
pexpect demo using netmiko to change 
'''

# imports
try:
    import time
    import netmiko
except ImportError:
    print "Could not import a required module.\n Exiting"
    raise SystemExit


# Variables

RTR2 = {
    'host':'pynet-rtr2',
    'device_type':'cisco_ios',
    'ip':'184.105.247.71',
    'username':'pyclass',
    'password':'88newclass',
    'secret':'',
    'port':22,
    'timeout':60
    }

NEW_BUFFER = str(((time.localtime()[3] * 60 + time.localtime()[4]) * 60) + time.localtime()[5] + 4096)





def main():
    '''
    main app
    '''

    # make connection to device
    dev_connection = netmiko.ConnectHandler(**RTR2)

    # check buffer before change
    print dev_connection.send_command('show runn | inc buffer')

    # change buffer
    dev_connection.send_config_set(['logg buff ' + NEW_BUFFER])

    # verify change has been made
    print dev_connection.send_command('show runn | inc buffer')


if __name__ == "__main__":
    main()
