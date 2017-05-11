#!/usr/bin/env python

'''
pexpect demo using netmiko to get 'show arp'
'''

# imports
try:
    import textwrap
    import netmiko
    import Queue
    import multiprocessing
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

proc_list = []                                                                                     #pylint: disable=invalid-name

def execute_command(que, device, command):
    '''
    function to connect to a device and execute a command
    '''
    dev_connection = netmiko.ConnectHandler(**device)
    command_result = dev_connection.send_command(command)
    que.put([device['host'], command_result])

def main():
    '''
    main app
    '''

    que = multiprocessing.Queue()

    # start processes
    for device in DEVICE_LIST:
        proc = multiprocessing.Process(target=execute_command, args = (que, device, COMMAND,))     #pylint: disable=bad-whitespace
        proc.start()
        proc_list.append(proc)

    # wait for processes to complete
    for proc in proc_list:
        proc.join()

    print '-' * LINE_WIDTH
    print ' '

    # print results
    for device in DEVICE_LIST:
        try:
            results = que.get(True, 1)
        except Queue.Empty:
            results = ['no data', 'no data']
        print results[0]
        for result_line in results[1].splitlines():
            print textwrap.fill(
                result_line,                                                                       #pylint: disable=bad-whitespace
                width = LINE_WIDTH,                                                                #pylint: disable=bad-whitespace
                initial_indent = ' ' * LINE_INDENT,                                                #pylint: disable=bad-whitespace
                subsequent_indent = ' ' * (LINE_INDENT + 4)                                        #pylint: disable=bad-whitespace
                )
        print ' '
        print '-' * LINE_WIDTH

if __name__ == "__main__":
    main()
