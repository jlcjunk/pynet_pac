#!/usr/bin/env python

'''
ansible module to create and delete VLANs on Arista switch
'''



# imports
try:
    from ansible.module_utils.basic import *
    import pyeapi
except ImportError:
    print "Could not import a required module.\n Exiting"
    raise SystemExit



# Variables



def main():
    '''
    main app
    '''

#    print(json.dumps({'message':"\n\nJust getting started.\n\n"}))



    module = AnsibleModule(
        argument_spec = dict(
            username  = dict(required=True),
            password  = dict(required=True),
            host      = dict(required=True),
            transport = dict(default='https', choices=['http', 'https']),
            port      = dict(default=443),
            action    = dict(default='add', choices=['add', 'delete', 'check']),
            vlanid    = dict(required=True),
            name      = dict(default='')
        )
    )



    if module.params['action'] == 'add':
        dev_connection = pyeapi.connect(transport=module.params['transport'], host=module.params['host'], username=module.params['username'], password=module.params['password'], port=module.params['port'], return_node=True)
        if dev_connection.api('vlans').get(module.params['vlanid']) is None:
            dev_connection.api('vlans').create(module.params['vlanid'])
            dev_connection.api('vlans').set_name(module.params['vlanid'], module.params['name'])
            module.exit_json(changed=True)
        else:
            module.exit_json(changed=False)

    if module.params['action'] == 'delete':
        dev_connection = pyeapi.connect(transport=module.params['transport'], host=module.params['host'], username=module.params['username'], password=module.params['password'], port=module.params['port'], return_node=True)
        if dev_connection.api('vlans').get(module.params['vlanid']) is None:
            module.exit_json(changed=False)
        else:
            dev_connection.api('vlans').delete(module.params['vlanid'])
            module.exit_json(changed=True)






#    print(json.dumps({'output_module_params':module.params}))


#    module.exit_json(**result)






if __name__ == "__main__":
    main()
