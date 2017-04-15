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

    def send_command(self, cmd):
        '''
        Send a command down the telnet channel
        Return the response
        '''
        cmd = cmd.rstrip()
        self.write(cmd + '\n')
        time.sleep(1)
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
            return telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
        except socket.timeout:
            sys.exit("Connection timed-out")


def main():
    '''
    Write a script that connects to the lab pynet-rtr1, logins, and executes the
    'show ip int brief' command.
    '''
    ip_addr = raw_input("IP address: ")
    ip_addr = ip_addr.strip()
    username = 'pyclass'
    password = '88'

    remote_conn = MyTelnet.telnet_connect(ip_addr)
    #remote_conn.login(username, password)

    time.sleep(1)
    #remote_conn.read_very_eager()
    #disable_paging(remote_conn)

    #output = send_command(remote_conn, 'show ip int brief')

    print "\n\n"
    #print output
    print "\n\n"

    remote_conn.close()

if __name__ == "__main__":
    main()
