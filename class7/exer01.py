#!/usr/bin/env python

'''
Use Arista's eAPI to obtain 'show interfaces' from the switch.
'''

# imports
try:
    import ssl
    import jsonrpclib
except ImportError:
    print "Could not import a required module.\n Exiting"
    raise SystemExit


# Variables
DEV_NAME = 'pynet-sw4'
DEV_USERID = 'eapi'
DEV_PASSWORD = '17mendel'
DEV_IP = '184.105.247.75'
DEV_PORT = '443'

COMMAND_TO_RUN = ['show interfaces']


# set url to use when connecting to device
DEV_URL = 'https://{}:{}@{}:{}/command-api'.format(DEV_USERID, DEV_PASSWORD, DEV_IP, DEV_PORT)


def main():
    '''
    main app
    '''

    # Allow trusting unntrusted certs
    ssl._create_default_https_context = ssl._create_unverified_context

    # setup connection to device
    dev_connection = jsonrpclib.Server(DEV_URL)

    # execute commands
    cmd_results = dev_connection.runCmds(1, COMMAND_TO_RUN)

    # print header
    print '\n\n'
    print 'Interface     inOctets      outOctets'

    # print octets for each interface
    for dev_interface in cmd_results[0]['interfaces']:
        if 'Ethernet' in dev_interface:
            print dev_interface,
            print ' '*(12-len(dev_interface)),
            print cmd_results[0]['interfaces'][dev_interface]['interfaceCounters']['inOctets'],
            print ' '*(12-len(str(cmd_results[0]['interfaces'][dev_interface]['interfaceCounters']['inOctets']))),
            print cmd_results[0]['interfaces'][dev_interface]['interfaceCounters']['outOctets']

    # print fotter
    print '\n\n'



if __name__ == "__main__":
    main()
