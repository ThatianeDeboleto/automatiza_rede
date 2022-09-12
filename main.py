import paramiko

address = '10.0.0.61'
username = 'root'
password = 'pythondevops'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=address, username=username, password=password)
stdin, stdout, stderr = ssh.exec_command('ifconfig') #mostrar o que esta dentro - comando
stdin.close()
print(stdout)

from netmiko import ConnectHandler

cisco_881 = {
    'device_type': 'cisco_ios',
    'host':   '10.10.10.10',
    'username': 'test',
    'password': 'password',
    'port' : 8022,          # optional, defaults to 22
    'secret': 'secret',     # optional, defaults to ''
}

output = net_connect.send_command('show ip int brief')
print(output)

config_commands = [ 'logging buffered 20000',
                    'logging buffered 20010',
                    'no logging console' ]
output = net_connect.send_config_set(config_commands)
print(output)

https://www.youtube.com/watch?v=HKuL4Xu3W5M
