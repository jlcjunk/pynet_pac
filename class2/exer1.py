#!/usr/bin/env python

'''
Demo of module importing - importing a module from 3 different locations
'''

# imports
import sys
import pysnmp
import paramiko

# Part B answer - not sure it's needed
print "\n\n"
print "pysnmp version = " + pysnmp.__version__
print "paramiko version = " + paramiko.__version__
print "\n"

# Part C answer
import hello
hello.hello()

sys.path.append('./random')
import hello_r
hello_r.hello()


import hello_sp
hello_sp.hello()
