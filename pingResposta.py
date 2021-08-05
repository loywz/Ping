
import os

def ping(ip):
    sucesso = os.system('ping -n 4 {}'.format(ip))
    if sucesso:
        print("{} Não respondeu".format(ip))
    else:
        print("{} Respondeu".format(ip))


print(ping('8.8.8.8'))