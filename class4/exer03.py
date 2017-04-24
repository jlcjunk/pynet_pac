#!/usr/bin/env python

'''
demo retriving 'sh int br' from cisco router with pexpect
'''

# imports
try:
    import time
    import pexpect
except ImportError:
    print "Could not import a required module.\n Exiting"
    raise SystemExit


# Variables

RTR_NAME = 'pynet-rtr2'
RTR_IP = '184.105.247.71'
RTR_SSH_PORT = 22
RTR_USER = 'pyclass'
RTR_PASSWORD = '88newclass'
TIMEOUT = 60




def main():
    '''
    main app
    '''

    # start ssh session
    router = pexpect.spawn('ssh -l  {} {} -p {}'.format(RTR_USER, RTR_IP, RTR_SSH_PORT))
    router.timeout = TIMEOUT

    # send password/ complete login
    router.expect('assword')
    time.sleep(1)
    router.sendline(RTR_PASSWORD)

    # turn off paging
    router.expect('pynet-rtr2#')
    router.sendline('terminal length 0')
    router.expect('pynet-rtr2#')

    # get 'sh ip int br'
    router.sendline('sh ip int br')
    router.expect('sh ip int br')
    router.expect('pynet-rtr2#')
    output = router.before
    print output



if __name__ == "__main__":
    main()
