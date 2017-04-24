#!/usr/bin/env python

'''
graph a few oids from a a device using SNMPv3 to gather data
'''

# imports
try:
    import time
    import pygal
    import snmp_helper
except ImportError:
    print "Could not import a required module.\n Exiting"
    raise SystemExit


# Variables
INTERVAL = 5      # how often in minutes to record data
DURATION = 60     # how man minutes to keep recording data

# to make time scaling for testinng easier
# set to 60 to make INTERVAL & DURATION be inn minutes
TIME_MULTIPLIER = 60


DEVICE_TO_MONITOR = '184.105.247.70'
DEVICE_PORT = 161
DEVICE_USER = 'pysnmp'
DEVICE_AUTH_PROTOCOL = 'sha'
DEVICE_AUTH_KEY = 'galileo1'
DEVICE_ENCRYPT_PROTOCOL = 'aes128'
DEVICE_ENCRYPT_KEY = 'galileo1'


OIDS_TO_GRAPH = {
    'In_Octets':'1.3.6.1.2.1.2.2.1.10.5',
    'Out_Octets':'1.3.6.1.2.1.2.2.1.16.5',
    'In_Packets':'1.3.6.1.2.1.2.2.1.11.5',
    'Out_Packets':'1.3.6.1.2.1.2.2.1.17.5'
    }


RUN_TIME = time.localtime()
RUN_REFERENCE = str(RUN_TIME[0]) + str(RUN_TIME[1]).zfill(2) + str(RUN_TIME[2]).zfill(2) + str(RUN_TIME[3]).zfill(2) + str(RUN_TIME[4]).zfill(2) + str(RUN_TIME[5]).zfill(2)


def main():
    '''
    Main application
    '''

    snmp_device = (DEVICE_TO_MONITOR, DEVICE_PORT)
    snmp_user = (DEVICE_USER, DEVICE_AUTH_KEY, DEVICE_ENCRYPT_KEY)


    # set baseline
    data_to_graph = {}
    data_last_read = {}
    for oid_name in OIDS_TO_GRAPH:
        oid = OIDS_TO_GRAPH[oid_name]
        data_to_graph[oid_name] = []
        data_last_read[oid_name] = \
            snmp_helper.snmp_extract(snmp_helper.snmp_get_oid_v3(snmp_device, snmp_user, oid=oid, auth_proto=DEVICE_AUTH_PROTOCOL, encrypt_proto=DEVICE_ENCRYPT_PROTOCOL, display_errors=False))

    # gather data for set period
    loop_counter = 0
    while (loop_counter < (TIME_MULTIPLIER * DURATION)):             #pylint: disable=superfluous-parens
        loop_counter += (TIME_MULTIPLIER * INTERVAL)
        time.sleep(TIME_MULTIPLIER * INTERVAL)
        for oid_name in OIDS_TO_GRAPH:
            oid = OIDS_TO_GRAPH[oid_name]
            temp_store = snmp_helper.snmp_extract(snmp_helper.snmp_get_oid_v3(snmp_device, snmp_user, oid=oid, auth_proto=DEVICE_AUTH_PROTOCOL, encrypt_proto=DEVICE_ENCRYPT_PROTOCOL, display_errors=False))
            data_to_graph[oid_name].append(int(temp_store) - int(data_last_read[oid_name]))
            data_last_read[oid_name] = temp_store


    # graph collected data
    graph_octets = pygal.Line()
    graph_octets.title = 'Interface FA4 octets'
    graph_octets.x_label = map(str,range(INTERVAL, DURATION + INTERVAL, INTERVAL))
    graph_octets.add('In', data_to_graph['In_Octets'])
    graph_octets.add('Out', data_to_graph['Out_Octets'])
    graph_octets.render_to_file('octets_' + RUN_REFERENCE + '.svg')

    graph_packets = pygal.Line()
    graph_packets.title = 'Interface FA4 packets'
    graph_packets.x_label = map(str,range(INTERVAL, DURATION + INTERVAL, INTERVAL))
    graph_packets.add('In', data_to_graph['In_Packets'])
    graph_packets.add('Out', data_to_graph['Out_Packets'])
    graph_packets.render_to_file('packets_' + RUN_REFERENCE + '.svg')


if __name__ == "__main__":
    main()
