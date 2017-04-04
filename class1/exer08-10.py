#!/usr/bin/env python


# import needed modules
import ciscoconfparse


# fulfil week 1 part 8
# read in file
config = ciscoconfparse.CiscoConfParse("cisco_ipsec.txt")

print "\n\n"


# fulfil week 1 part 9
print "crypto maps with PFS Group 5:"
for object in config.find_objects_w_child(parentspec="^crypto\smap",childspec="pfs\sgroup5$"):
    print "  "+object.text

print "\n\n"



# fulfil week 1 part 10
print "crypto maps without AES:"
for object in config.find_objects_wo_child(parentspec="^crypto\smap",childspec="transform.*AES.*$"):
    print "  "+object.text

print "\n\n"


