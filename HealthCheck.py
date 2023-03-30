import subprocess
import ipaddress
import sys
from datetime import datetime



sys.stdout = open('c:/temp/NetworkHealth.csv', 'wt')
current_datetime = datetime.now()
filename = f'c:/temp/NetworkHealth_{current_datetime.strftime("%Y-%m-%d_%H-%M-%S")}.csv'
sys.stdout = open(filename, 'a')




print(current_datetime)

with open(r'c:\temp\ip.txt', 'r') as ipp_net:
    print("IP List:")
    for ip_str in ipp_net:
        ip = ipaddress.ip_address(ip_str.rstrip())
        print(ip)

        ping = subprocess.run(['ping', str(ip), '-n', '2', '-w', '2'], capture_output=True, text=True)
        if ping.returncode == 0:
            print(f'The network {ip} is up')
        else:
            print(f'The network {ip} is down')




# with open(r'c:\temp\ip.txt', 'r') as ipp_net:
# #    ip_list = ipp_net.readlines()
#     print("IP List:")
# #    print(ip_list)
#
#     for ip_str in ip_list:
#         ip = ipaddress.ip_address(ip_str.strip())
#         ping = subprocess.run(['ping', str(ip), '-n', '2', '-w', '2'], capture_output=True, text=True)
#         if ping.returncode == 0:
#             print(f'The network {ip} is up')
#         else:
#             print(f'The network {ip} is down')


# with open(r'c:\temp\ip.txt', 'r') as ipp_net:
#     for ip_str in ipp_net:
#         ip = ipaddress.ip_address(ip_str.strip())
#         ping = subprocess.run(['ping', str(ip), '-n', '2', '-w', '2'], capture_output=True, text=True)
#         if ping.returncode == 0:
#             print(f'The network {ip} is up')
#         else:
#             print(f'The network {ip} is down')