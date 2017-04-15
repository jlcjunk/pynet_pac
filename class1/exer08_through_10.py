#!/usr/bin/env python


"""
Just a docstring to make lint happy and practice using them
"""

# import needed modules
import ciscoconfparse
import pprint


# setup main executable
def main():

    """
    Just a docstring to make lint happy and practice using them

    Args:
        None

    Returns:
        None

    Raises:
        None
    """


    # fulfil week 1 part 8
    # read in file
    device_cfg = ciscoconfparse.CiscoConfParse("cisco_ipsec.txt")

    pprint.pprint(device_cfg.find_all_children('crypto map CRYPTO'))



    print "\n\n"


    # fulfil week 1 part 9
    print "crypto maps with PFS Group 5:"
    for cfg_object in device_cfg.find_objects_w_child(parentspec=r"^crypto\smap", childspec=r"pfs\sgroup5$"):
        print "  "+cfg_object.text

    print "\n\n"



    # fulfil week 1 part 10
    print "crypto maps without AES:"
    for cfg_object in device_cfg.find_objects_wo_child(parentspec=r"^crypto\smap", childspec=r"transform.*AES.*$"):
        print "  "+cfg_object.text

    print "\n\n"


if __name__ == "__main__":
    main()
