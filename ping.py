import subprocess

ping = subprocess.run(input('ping: '), capture_output=True, text=True)

#print(ping.returncode)

if ping.returncode == 1:
    print('The network is down ')

else:
    print('The network is up')