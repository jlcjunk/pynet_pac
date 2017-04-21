#!/usr/bin/env python

'''
check last changed config time and send notice if config has changed since last check
'''

# imports
try:
    import yaml
    import snmp_helper
    import email_helper
except ImportError:
    print "Could not import a required module.\n Exiting"
    raise SystemExit


# Variables
DATA_FILE = 'dev_list'


def main():
    '''
    simple test with SNMP to see if config has changed and send notice if it has.
    '''
    # read data file - devices to check and last modified time
    try:
        with open(DATA_FILE + '.yaml', 'r') as yaml_file:
            device_list = yaml.load(yaml_file)
    except yaml.scanner.ScannerError:
        print "Data file is corrupt."
        raise SystemExit

    for listed_device in device_list:
        # save last timestamp for later use
        last_known_change = device_list[listed_device][8]

        # Prepare to get timestamp from device
        snmp_device = (device_list[listed_device][0], device_list[listed_device][1])
        snmp_user = (device_list[listed_device][2], device_list[listed_device][4], device_list[listed_device][6])
        oid = device_list[listed_device][7]
        auth_protocol = device_list[listed_device][3]
        encrypt_protocol = device_list[listed_device][5]

        # get timestamp of change from device
        try:
            last_changed = snmp_helper.snmp_extract(snmp_helper.snmp_get_oid_v3(snmp_device, snmp_user, oid=oid, auth_proto=auth_protocol, encrypt_proto=encrypt_protocol, display_errors=False))
        except TypeError:
            print 'There was an error connecting to ' + listed_device + ' via SNMP. \n Device skipped.'
            last_changed = last_known_change

        # provide some visual output for the sake of knowing something was done when timestamps match
        print listed_device

        # act if timestamps do not match
        if last_known_change != last_changed:
            print 'Configuration does not match. Sending email.'
            email_helper.send_mail('jlcjunk@crabtreefamily.us', 'Configuration channge on ' + listed_device, 'Configuration channge on ' + listed_device, 'pythonlab@crabtreefamily.us')

        # allow visual timestamp comparison to verify code is working
        print '    ' + last_known_change
        print '    ' + last_changed

        # Save new timestamp so it can be saved later for subsiquent runs
        device_list[listed_device][8] = last_changed


    # save new timestamps
    with open(DATA_FILE + '.yaml', 'w') as yaml_file:
        yaml_file.write(yaml.dump(device_list, default_flow_style=None, width=200))



if __name__ == "__main__":
    main()
