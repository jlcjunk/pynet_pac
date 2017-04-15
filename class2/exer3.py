#!/usr/bin/env python

'''
Write a script that connects to the lab pynet-rtr1, logins, and executes the
'show ip int brief' command.
'''

import telnetlib
import time
import socket
import sys
import getpass

TELNET_PORT = 23
TELNET_TIMEOUT = 6

class MyTelnet(telnetlib.Telnet):

    '''
    super set of Telnet class

    __init__(self, host=None, port=0, timeout=<object object>)
    '''

    def send_command(self, cmd, wait_duration=1):
        '''
        Send a command down the telnet channel
        Return the response
        '''
        cmd = cmd.rstrip()
        self.write(cmd + '\n')
        time.sleep(wait_duration)
        return self.read_very_eager()

    def login(self, username, password):
        '''
        Login to network device
        '''
        output = self.read_until("sername:", TELNET_TIMEOUT)
        self.write(username + '\n')
        output += self.read_until("ssword:", TELNET_TIMEOUT)
        self.write(password + '\n')
        return output

    def disable_paging(self, paging_cmd='terminal length 0'):
        '''
        Disable the paging of output (i.e. --More--)
        '''
        return self.send_command(paging_cmd)

    def telnet_connect(self, ip_addr):
        '''
        Establish telnet connection
        '''
        try:
            return self.open(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
        except socket.timeout:
            sys.exit("Connection timed-out")


def main():
    '''
    Write a script that connects to the lab pynet-rtr1, logins, and executes the
    'show ip int brief' command.
    '''


    ip_addr = '184.105.247.70'
    #ip_addr = raw_input("IP address: ")
    ip_addr = ip_addr.strip()
    username = 'pyclass'
    password = '88newclass'
    #password = getpass.getpass()

    remote_conn = MyTelnet()

    remote_conn.telnet_connect(ip_addr)

    remote_conn.login(username, password)

    time.sleep(1)

    remote_conn.read_very_eager()

    remote_conn.disable_paging()

    output = remote_conn.send_command('show ip int brief')

    print "\n\n"
    print output
    print "\n\n"

    remote_conn.close()

if __name__ == "__main__":
    main()
