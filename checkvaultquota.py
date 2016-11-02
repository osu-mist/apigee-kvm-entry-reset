import requests
import sys
import json
import logging
from uritemplate import expand
from uritemplate import URITemplate

def resetKVMQuotaCount(keymap_url, config_data):
    """
    Executes a post request to the KVM to reset the quota violation count to 0.
    Returns true on request success
    """
    jsonbody = json.dumps({'name': config_data['entry_name'], 'value': 0})
    headers = {'content-type': 'application/json'}

    r = requests.post(keymap_url, headers=headers, data=jsonbody, auth=(config_data['username'],config_data['password']))
    return r.status_code == 200

def buildKeyMapUrl(config_data):
    """
    Formats the KVM Keymap url for us using the config data.
    """

    t = URITemplate('https://{hostname}/{version}/organizations/{org}/environments/{env_name}/keyvaluemaps/{map_name}/entries/{entry_name}')
    return t.expand(
        hostname    = config_data['hostname'],
        version     = config_data['version'],
        org         = config_data['org'],
        env_name    = config_data['env_name'],
        map_name    = config_data['map_name'],
        entry_name  = config_data['entry_name']
    )

def getKVMQuotaCount(keymap_url, config_data):
    """
    Executes a get request to the KVM Quota count entry
    Returns status code and val as a pair for error handling purposes.
    """
    r = requests.get(keymap_url, auth=(config_data['username'],config_data['password']))
    
    if r.status_code == 200:
        res = r.json()
        val = int( res[u'value'].decode('utf-8') )
    else:
        val = None
    return (r.status_code, val)

"""
This script makes a simple api call to Apigee's kvm api to check the number of quota violcations for a given kvm entry.
"""
if __name__ == '__main__':
    logging.basicConfig(filename='jobinfo.log',level=logging.INFO)
    logging.basicConfig(filename='joberrors.log',level=logging.ERROR)

    try:
        config_data_file = open(sys.argv[1])
        config_data = json.load(config_data_file)
        keymap_url = buildKeyMapUrl(config_data)
        
        status, val = getKVMQuotaCount(keymap_url, config_data)

        if status == requests.codes.ok:
            print val
            if(val > 0):
                if(resetKVMQuotaCount(keymap_url, config_data) == False):
                    logging.error('API Call to reset KVM Quota Count failed.')
                else:
                    logging.info('Reset call to KVM Quota Count succeceded.')
        else:
            sys.stderr.write("Get request to KVM failed.")
    except:
        print "Please make sure placing the configuration file in the same directory and pass it as an argument!"