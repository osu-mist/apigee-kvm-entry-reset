Jenkins Vault Quota Checker Job
=====================

This role creates a job in Jenkins which automatically runs the Vault Quota Checker script. 

### Usage
---------

1. Set [configuration file](/VaultQuotaChecker/configuration.example.json) as secret file and pass it to the Python script.

### Outcome
-----------

If the job works as expected a notification email should be sent from the job to the designated recipients.