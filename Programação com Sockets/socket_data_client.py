# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: IGOR CARVALHO DE BRITO BATISTA 
#
# SCRIPT: Cliente de sockets UDP modificado para solicitar a data atual ao servidor (python 3)
#

# importacao das bibliotecas
from socket import * # sockets

# definicao das variaveis
serverName = '192.168.1.112' # ip do servidor a se conectar
serverPort = 61000 # porta a se conectar
clientSocket = socket(AF_INET, SOCK_DGRAM) # criacao do socket UDP

comando = input('Digite o comando: ')
clientSocket.sendto(comando.encode('utf-8'),(serverName, serverPort)) # envia mensagem para o servidor
currentDate, serverAddress = clientSocket.recvfrom(2048) # recebe do servidor a resposta
print ('O servidor (\'%s\', %d) respondeu: %s' % (serverName, serverPort, currentDate.decode('utf-8')))
clientSocket.close() # encerra o socket do cliente