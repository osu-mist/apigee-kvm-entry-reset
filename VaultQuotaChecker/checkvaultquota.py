import requests
import sys
import smtplib
from email.mime.text import MIMEText

def sendNotificationEmail(count):
    text = 'The Vault API has had ' + str(count) + ' quota violaitons in the past hour'
    msg = MIMEText(text,'plain')
    msg['Subject'] = 'Jenkins Vault Quota Checker Notification'
    msg['From'] = 'ECS DATA Jenkins Instance'
    msg['To'] = 'craryg@oregonstate.edu'

    #This line requires running this command 'python -m smtpd -n -c DebuggingServer localhost:1025'
    #TODO Streamline this
    s = smtplib.SMTP('localhost',1025)
    s.sendmail()

def resetKVMQuotaCount():
    #TODO FINISH IMPLEMENTING RESET CALL TO KVM.

def getKVMQuotaCount(config_data):
    keymap_url = 
    r = requests.get(keymap_url, auth=(config_data['client_id'],config_data['client_secret']]))
    res = r.json()
    return int(res[u'value'].decode('utf-8'))
    #TODO Try to trash this with invalid responses from the server

if __name__ == '__main__':
    try:
        # Read configuration file in JSON format
        keymap_url = https://api.enterprise.apigee.com/v1/organizations/osu/environments/test/keyvaluemaps/GeorgeLookupJson_1_QVCKVM/entries/QVCK_1
        config_data_file = open(sys.argv[1])
        config_data = json.load(config_data_file)
        count = getKVMQuotaCount(config_data)

        if count > 0:

    except:
        print "Please make sure placing the configuration file in the same directory and pass it as an argument!"
    
	#getQuotaViolationsCount('https://api.enterprise.apigee.com/v1/organizations/osu/keyvaluemaps/GeorgeLookupJson_1_QVCKVM',)