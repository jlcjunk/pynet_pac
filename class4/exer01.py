#!/usr/bin/env python

'''
demo retriving show version from cisco router with paramiko. 
'''

# imports
try:
    import time
    import paramiko
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



def pause(shell):
    '''
    pause until data is available to read (or timeout reached)
    '''
    loop_count = 0
    while (shell.recv_ready() is False) and (loop_count >= TIMEOUT):
        time.sleep(1)
        loop_count += 1
    time.sleep(5)


def main():
    '''
    main app
    '''
    # setup connection to router
    router = paramiko.SSHClient()
    router.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    router.connect(RTR_IP, port=RTR_SSH_PORT, username=RTR_USER, password=RTR_PASSWORD, look_for_keys=False)
    router_shell = router.invoke_shell()
    router_shell.settimeout(TIMEOUT)

    # clear read buffer
    router_shell.recv(2500)

    # set no paging
    router_shell.send('terminal length 0\n')
    pause(router_shell)

    # clear read buffer
    router_shell.recv(2500)


    # get show ver
    router_shell.send('sh ver\n')
    pause(router_shell)
    output = router_shell.recv(60000)


    # close connection
    router.close()


    # display output
    print output[6:-11]


if __name__ == "__main__":
    main()
