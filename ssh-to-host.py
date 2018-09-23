#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paramiko
import sqlite3
import logging
import configparser

# read a list of hosts from file.
# ssh to the linux host.
# run and capture the results of 'uptime'
# save to a sqlite db

config = configparser.ConfigParser()
config.read('secrets.ini')

logging.basicConfig(filename='demo.log',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(threadName)s -  %(levelname)s - %(message)s')

logging.info("------------------- START ---------------------------------------")

mydevices = config['auth']['hostname']  # catch bad hostname.
mycommand = 'cat /etc/redhat-release'  # catch bad command. Can not seem to catch a bad command.
myusername = config['auth']['username']  # catch bad username.
mypassword = config['auth']['password']  # catch bad password or key


try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(mydevices[0], username=myusername[0])
except Exception as error:
    print("ERROR: " + str(error))
    logging.debug("ERROR: " + str(error))
    quit()

try:
    stdin, stdout, stderr = ssh.exec_command(mycommand)
    results = stdout.readline()
    print(results)
    #for m in mycommand:
    #    stdin,stdout,stderr = ssh.exec_command(m)
    #    for line in stdout.readlines():
    #        myresults =  line.strip()

    ssh.close()
    logging.info("RESULTS: " + str(results))
    logging.info("--------------------- FINISHED -------------------------")
except Exception as error:
    print("ERROR: " + str(error))
    logging.debug("ERROR: " + str(error))
    quit()
