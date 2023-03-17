import subprocess
import ipaddress

ipp_net = ipaddress.ip_network('192.168.120.0/30')

ip = []

for ip in  ipp_net:
    print(ip)
    ping =subprocess.run(['ping', str(ip)], capture_output=True, text=True)
    if ping.returncode == 1:
        print('The network is down ')

    else:
        print('The network is up')