#!/usr/bin/env python

'''
help create device list datafile
'''

# imports
try:
    import yaml
    import readline
except ImportError:
    print "Could not import a required module.\n Exiting"
    raise SystemExit



def main():
    '''
    main app
    '''

    # Variables
    device_list = {}
    hostname = 'default'
    save_file = 'device_list01.yaml'

    while hostname != '':
        # gather info from user
        hostname = raw_input('device host name : ')
        if hostname != '':
            secret = raw_input('enable secret : ')
            vlan = raw_input('vlan for access ports : ')
            ip = raw_input('device vlan1/ management IP : ')
            gw = raw_input('device vlan1/ management gateway IP : ')
            snmp = raw_input('SNMP read only community string : ')
            
            device_list[ hostname ] = { 
                'secret' : secret , 
                'access_vlan' : vlan , 
                'ip_addr' : ip ,
                'default_gateway' : gw ,
                'snmp_community' : snmp
                }

    print device_list
    print ''

    for device , null in device_list.items():
        print 'device : ' + device
        print "device_list[device]['secret'] : " + device_list[device]['secret']        
        print "null['secret'] : " + null['secret']

    with open(save_file, 'w') as yaml_file:
        yaml_file.write("---\n")
        yaml_file.write(yaml.dump(device_list,default_flow_style=False))


if __name__ == "__main__":
    main()
