#!/usr/bin/env python

# imports
import pysnmp
import paramiko
import sys

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

