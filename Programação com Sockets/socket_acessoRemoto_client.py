# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: IGOR CARVALHO DE BRITO BATISTA
#
# SCRIPT: Cliente de sockets TCP modificado para enviar um comando ao servidor e o mesmo seja executado localmente (python 3)
#

# importacao das bibliotecas
from socket import *

while 1:
    # definicao das variaveis
    serverName = '192.168.1.112' # ip do servidor
    serverPort = 61000 # porta a se conectar
    clientSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
    clientSocket.connect((serverName, serverPort)) # conecta o socket ao servidor
    
    comando = input('Digite o comando: ') 
    clientSocket.send(comando.encode('utf-8')) # envia o comando para o servidor
    resposta = clientSocket.recv(1024) # tcp precisa receber uma resposta após enviar uma solicitação
    
clientSocket.close() # encerramento o socket do cliente
