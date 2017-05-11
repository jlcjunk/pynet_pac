#!/usr/bin/env python

'''
pexpect demo using netmiko to change
'''

# imports
try:
    import textwrap
    import time
    import netmiko
except ImportError:
    print "Could not import a required module.\n Exiting"
    raise SystemExit


# Variables

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

NEW_BUFFER = str(((time.localtime()[3] * 60 + time.localtime()[4]) * 60) + time.localtime()[5] + 4096)

COMMAND_FILE = 'exer08_commands.txt'

DEVICE_LIST = [
    RTR1,
    RTR2
    ]


LINE_INDENT = 8
LINE_WIDTH = 100

def main():
    '''
    main app
    '''

    for device_to_change in DEVICE_LIST:

        # make connection to device
        dev_connection = netmiko.ConnectHandler(**device_to_change)

        # check config before change
        print device_to_change['host']
        command_result = dev_connection.send_command('sh run | inc buff|logging con')
        for result_line in command_result.splitlines():
            print textwrap.fill(
                result_line,
                width = LINE_WIDTH,
                initial_indent = ' ' * LINE_INDENT,
                subsequent_indent = ' ' * (LINE_INDENT + 4)
                )

        # execute commands
        dev_connection.send_config_from_file(config_file = COMMAND_FILE)

        # check config after change
        command_result = dev_connection.send_command('sh run | inc buff|logging con')
        for result_line in command_result.splitlines():
            print textwrap.fill(
                result_line,
                width = LINE_WIDTH,
                initial_indent = ' ' * LINE_INDENT,
                subsequent_indent = ' ' * (LINE_INDENT + 4)
                )


if __name__ == "__main__":
    main()
