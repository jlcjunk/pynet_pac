#!/usr/bin/env python

'''
4. SNMP Basics
 c. Create a script that connects to both routers (pynet-rtr1 and pynet-rtr2) and prints out both the MIB2 sysName and sysDescr.
'''

import sys
sys.path.append('~/git/pynet/snmp/')
import textwrap        #pylint: disable=wrong-import-position
import snmp_helper     #pylint: disable=wrong-import-position

OID_NAME = '.1.3.6.1.2.1.1.5.0'
OID_DESCRIPTION = '.1.3.6.1.2.1.1.1.0'
SNMP_PORT = 161

# List of OIDs to get in form of ['OID Title', 'OID']
OID_LIST = [
    ['Name', '.1.3.6.1.2.1.1.5.0'],
    ['Description', '.1.3.6.1.2.1.1.1.0']
    ]

# List of devices in the form of {'ip':'10.10.10.10','community':'Community string'},
device_list = [                                            #pylint: disable=invalid-name
    {'ip':'184.105.247.70', 'community':'galileo'},
    {'ip':'184.105.247.71', 'community':'galileo'}
    ]


def main():
    '''
    4. SNMP Basics
     c. Create a script that connects to both routers (pynet-rtr1 and pynet-rtr2) and prints out both the MIB2 sysName and sysDescr.
    '''

    # read Rtore quested OIDs
    for device_in_list in device_list:
        for oid_in_list in OID_LIST:
            device_in_list[oid_in_list[0]] = snmp_helper.snmp_extract(snmp_helper.snmp_get_oid((device_in_list['ip'], device_in_list['community'], SNMP_PORT), oid=oid_in_list[1], display_errors=False))

    # display data
    print '\r\n\r\n\r\n\r\n-------------------------------------------------------'
    for device_in_list in device_list:
        print ' '
        print 'Device IP: ' + device_in_list['ip']
        for oid_in_list in OID_LIST:
            print textwrap.fill('    ' + oid_in_list[0] + ':  ' + device_in_list[oid_in_list[0]], width=120, subsequent_indent=' '*(len('    ' + oid_in_list[0] + ':  ')))
        print ' '
    print '-------------------------------------------------------\r\n\r\n\r\n\r\n'


if __name__ == "__main__":
    main()
