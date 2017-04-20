#!/usr/bin/env python

'''
4. SNMP Basics
 c. Create a script that connects to both routers (pynet-rtr1 and pynet-rtr2) and prints out both the MIB2 sysName and sysDescr.
'''


# updated PYTHONPATH for snmp_helper
import textwrap
import snmp_helper

SNMP_PORT = 161
LINE_WIDTH = 100

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
        for oid_name, oid_value in OID_LIST:
            device_in_list[oid_name] = snmp_helper.snmp_extract(snmp_helper.snmp_get_oid((device_in_list['ip'], device_in_list['community'], SNMP_PORT), oid=oid_value, display_errors=False))

    # display data
    print '\n\n\n\n' + '-' * LINE_WIDTH
    for device_in_list in device_list:
        print ' '
        print 'Device IP: ' + device_in_list['ip']
        for oid_name, loopjunk in OID_LIST:               #pylint: disable=unused-variable
            print textwrap.fill('    ' + oid_name + ':  ' + device_in_list[oid_name], width=LINE_WIDTH, subsequent_indent=' '*(len('    ' + oid_name + ':  ')))
        print ' '
    print '-' * LINE_WIDTH + '\n\n\n\n'


if __name__ == "__main__":
    main()
