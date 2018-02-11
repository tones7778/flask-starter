import paramiko

print('connecting to host .....')

mydevices = ['localhost']
mycommand = 'ifconfig eth0'
myusername = ['root']
mypassword = ['password']

try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(mydevices[0], username=myusername[0], password=mypassword[0])
except paramiko.SSHException:
    print("Connection Failed")
    quit()

stdin,stdout,stderr = ssh.exec_command(mycommand)
results = stdout.read()
print(results)
#for m in mycommand:
#    stdin,stdout,stderr = ssh.exec_command(m)
#    for line in stdout.readlines():
#        myresults =  line.strip()

ssh.close()
