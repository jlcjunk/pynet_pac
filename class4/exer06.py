#!/usr/bin/env python

'''
pexpect demo using netmiko to get 'show arp' 
'''

# imports
try:
    import textwrap
    import netmiko
except ImportError:
    print "Could not import a required module.\n Exiting"
    raise SystemExit


# Variables
COMMAND = 'show arp'

RTR1 = {
    'host':'pynet-rtr1',
    'device_type':'cisco_ios',
    'ip':'184.105.247.70',
    'username':'pyclass',
    'password':'88newclass',
    'secret':'',
    'port':22,
    'timeout':60
    }
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
SRX1 = {
    'host':'pynet-jnpr-srx1',
    'device_type':'juniper',
    'ip':'184.105.247.76',
    'username':'pyclass',
    'password':'88newclass',
    'secret':'',
    'port':22,
    'timeout':60
    }



DEVICE_LIST = [
    RTR1,
    RTR2,
    SRX1
    ]

LINE_INDENT = 8
LINE_WIDTH = 100


def main():
    '''
    main app
    '''

    print '-' * LINE_WIDTH
    print ' '

    for device in DEVICE_LIST:
        dev_connection = netmiko.ConnectHandler(**device)
        command_result = dev_connection.send_command(COMMAND)

        print device['host']
        print '    Command: ' + COMMAND
        for result_line in command_result.splitlines():
            print textwrap.fill(
                result_line,
                width = LINE_WIDTH,
                initial_indent = ' ' * LINE_INDENT,
                subsequent_indent = ' ' * (LINE_INDENT + 4)
                )
        print ' '
        print '-' * LINE_WIDTH

if __name__ == "__main__":
    main()
