import os

with open('hosts.txt') as file:
    cont = file.read()
    cont = cont.splitlines()
    
    for ip in cont:
        os.system('ping {}'.format(ip))