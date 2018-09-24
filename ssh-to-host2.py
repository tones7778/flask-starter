import paramiko
import socket
# os,sys,re

mydevices = ['vm1.home.lan', 'vm2.home.lan', 'adsads']
mycommand = ['uptime', 'ping -c 3 pi', 'vnstat']
myusername = ['tones']
mypassword = ['password']


for i in mydevices[:]:
    try:
        print(f"Connection to host {i}.")
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(i, username=myusername[0], password=mypassword[0], timeout=30)
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

    try:

        for m in mycommand[:]:
            stdin,stdout,stderr = ssh.exec_command(m)
            results = stdout.read()
            final_results = results.decode(encoding='UTF-8')
            print(final_results)
    except Exception as e:
        print("Operation error: %s", e)

