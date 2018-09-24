#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paramiko
import sqlite3
import logging
import configparser


config = configparser.ConfigParser()
config.read('secrets.ini')

mydevices = config['auth']['hostname']  # catch bad hostname.
mycommand = config['auth']['command']  # catch bad command. Can not seem to catch a bad command.
myusername = config['auth']['username']  # catch bad username.
mypassword = config['auth']['password']  # catch bad password or key


logging.basicConfig(filename='demo.log',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(threadName)s -  %(levelname)s - %(message)s')

logging.info("------------------- START ---------------------------------------")



try:
    print("Connection to host: ", mydevices)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(mydevices, username=myusername, password=mypassword, timeout=30)

except paramiko.AuthenticationException:
    print("Authentication failed, please verify your credentials: %s")
    quit()
except paramiko.SSHException as sshException:
    print("Unable to establish SSH connection: %s" % sshException)
    quit()
except paramiko.BadHostKeyException as badHostKeyException:
    print("Unable to verify server's host key: %s" % badHostKeyException)
    quit()
except socket.error:
    print(f"Could not connect to {i}")
    quit()
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
