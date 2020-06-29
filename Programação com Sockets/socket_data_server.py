# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: IGOR CARVALHO DE BRITO BATISTA
#
# SCRIPT: Servidor de sockets UDP modificado para receber um comando de um cliente e responder com a data atual (python 3)
#

# importacao das bibliotecas
from socket import * # sockets
import time

# definicao das variaveis
serverName = '' # ip do servidor (em branco)
serverPort = 61000 # porta a se conectar
serverSocket = socket(AF_INET, SOCK_DGRAM) # criacao do socket UDP
serverSocket.bind((serverName, serverPort)) # bind do ip do servidor com a porta
print ('Servidor UDP esperando conexoes na porta %d ...' % (serverPort))
while 1:
    comando, clientAddress = serverSocket.recvfrom(2048) # recebe do cliente
    comando = comando.decode('utf-8')

    if comando == "data":
        date = time.ctime()
        date = str(date) # converte a data em string
    else:
        continue
    print ('Cliente %s enviou o comando: %s, retornando informacao : %s' % (clientAddress, comando, date))
    serverSocket.sendto(date.encode('utf-8'), clientAddress) 
# envia a resposta para o cliente
serverSocket.close() # encerra o socket do servidor