from genie.testbed import load
from pprint import pprint
import subprocess
import ipaddress
import sys
from datetime import datetime

testbed = load('/home/marlon/yaml1/my_testbed.yaml')

sys.stdout = open('/home/marlon/temp/NetworkHealth.txt')
#current_datetime = datetime.now()
#filename = f'/temp/NetworkHealth_{current_datetime.strftime("%Y-%m-%d_%H-%M-%S")}.txt'
#sys.stdout = open(filename, 'a')

dev = testbed.devices['ZACDMB1FSO48test']
#dev = testbed

dev.connect(learn_hostname=False)
#pprint(dir(dev.api))

sh_ver_parsed = dev.parse('show version')
sh_ip_int_br = dev.parse("show ip int brief")


#print(sh_ver_parsed)
pprint(sh_ver_parsed['version']['uptime'])
pprint(sh_ip_int_br)

