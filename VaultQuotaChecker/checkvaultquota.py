import requests
import sys
import smtplib
from email.mime.text import MIMEText

def sendNotificationEmail(count,job_interval='hour'):
    """
    Sends the quota violation notification email.
    """
    #TODO Configure past TIME_INTERVAL and leave that to Jenkins
    #TODO NOCHECKIN Requires testing
    text = 'The Vault API has had ' + str(count) + ' quota violaitons in the past {interval}'.format(interval=job_interval)
    msg = MIMEText(text,'plain')
    msg['Subject'] = 'Jenkins Vault Quota Checker Notification'
    msg['From'] = 'ECS DATA Jenkins Instance'
    msg['To'] = 'craryg@oregonstate.edu'
    #TODO have jenkin's pass in a recipients list'

    #This line requires running this command 'python -m smtpd -n -c DebuggingServer localhost:1025'
    #TODO Streamline this
    s = smtplib.SMTP('localhost',1025)
    s.sendmail()

def resetKVMQuotaCount(keymap_url, config_data):
    """
    Executes a post request to the KVM to reset the quota violation count to 0.
    Returns true on request sucess
    """
    jsonbody = json.dumps({'name': 'QVCK_1', 'value': 0})
    r = requests.post(keymap_url, data=jsonbody, auth=(config_data['client_id'],config_data['client_secret']))
    return r.status_code == 200


def buildKeyMapUrl(config_data):
    """
    Formats the KVM Keymap url for us using the config data.
    """
    s ='{hostname}/{version}/organizations/{org}/environments/{env_name}/keyvaluemaps/{map_name}/entries/{entry_name}'
    return s.format(
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
    r = requests.get(keymap_url, auth=(config_data['client_id'],config_data['client_secret']))
    if r.status_code == 200:
        res = r.json()
        val = int( res[u'value'].decode('utf-8') )
    else:
        val = None
    return (r.status_code, val)

    #TODO Try to trash this with invalid responses from the server

if __name__ == '__main__':
    try:
        # Read configuration file in JSON format
        #Add Jenkins job string parameter for job interval
        config_data_file = open(sys.argv[1])
        config_data = json.load(config_data_file)
        keymap_url = buildKeyMapUrl()

        status, val = getKVMQuotaCount(keymap_url, config_data)
        if status == requests.codes.ok:
            print val
        else:
            sys.stderr.write("Get request to KVM failed.")
    except:
        print "Please make sure placing the configuration file in the same directory and pass it as an argument!"
	#getQuotaViolationsCount('https://api.enterprise.apigee.com/v1/organizations/osu/keyvaluemaps/GeorgeLookupJson_1_QVCKVM',)