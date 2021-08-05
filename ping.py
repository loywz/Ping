import os #Importa Biblioteca os


print('-'*60) #Imprimir '-' 60 vezes 

#Criando uma variavel que vai receber do usuário um IP ou Host
ip_ou_host = input("Digite um Ip ou Host para ser verificado: ")

print('-'*60) #Imprimir '-' 60 vezes 

os.system('ping -n 4 {}'.format(ip_ou_host))#chamando system da biblioteca os 