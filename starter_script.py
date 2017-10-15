#!/usr/bin/env python

from netmiko import ConnectHandler

ios_l2 = {
'device_type': 'cisco_ios',
'ip': '192.168.122.72',
'username': 'rajan',
'password': 'cisco',
}

net_connect = ConnectHandler(**ios_l2)
output = net_connect.send_command('show version')
print(output)