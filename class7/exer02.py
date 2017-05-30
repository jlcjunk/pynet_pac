#!/usr/bin/env python

'''
app to add and remove vlans from Arista switch
'''

# imports
try:
    import sys
    import pyeapi
except ImportError:
    print "Could not import a required module.\n Exiting"
    raise SystemExit


# Variables
DEV_NAME = 'pynet-sw4'



def main():
    '''
    main app
    '''

    # connect to device
    dev_connection = pyeapi.connect_to(DEV_NAME)



    if sys.argv[1] == '--name':
        dev_connection = pyeapi.connect_to(DEV_NAME)
        if dev_connection.api('vlans').get(sys.argv[3]) is None:
            dev_connection.api('vlans').create(sys.argv[3])
            dev_connection.api('vlans').set_name(sys.argv[3], sys.argv[2])
            print 'Created VLAN ' + sys.argv[3] + ' ' + sys.argv[2]
        else:
            print 'VLAN ' + sys.argv[3] + ' already exists'
    elif sys.argv[1] == '--remove':
        dev_connection = pyeapi.connect_to(DEV_NAME)
        if dev_connection.api('vlans').get(sys.argv[2]) is None:
            print 'VLAN ' + sys.argv[2] + ' does not exist.'
        else:
            dev_connection.api('vlans').delete(sys.argv[2])
            print 'VLAN ' + sys.argv[2] + ' deleted.'
    else:
        print '\n\nInvalid argument\n\n'




if __name__ == "__main__":
    main()
