Jenkins Vault Quota Checker Job
=====================

This role creates a job in Jenkins which automatically runs the Vault Quota Checker script. 

### Dependencies
- [Jenkins "Environment Script Plugin"](https://wiki.jenkins-ci.org/display/JENKINS/Environment+Script+Plugin)
- [This commit adds the environment script plugin to ansible-private-roles](https://github.sig.oregonstate.edu/ecs-data/ansible-private-roles/commit/ebf51d31f1a7acf78719bd1e7fd7bfa1fa89efe4)

### Usage
---------

1. Set [configuration file](/VaultQuotaChecker/configuration.example.json) as secret file and pass it to the Python script.

### Outcome
-----------

If the job works as expected a notification email should be sent from the job to the designated recipients.