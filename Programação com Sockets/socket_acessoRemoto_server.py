# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: IGOR CARVALHO DE BRITO BATISTA
#
# SCRIPT: Servidor de sockets TCP modificado para abrir um arquivo e enviar seu conteúdo ao cliente (python 3)
#

# importacao das bibliotecas
from socket import * # sockets
import os

# definicao das variaveis
serverName = '' # ip do servidor (em branco)
serverPort = 61000 # porta a se conectar
serverSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
serverSocket.bind((serverName,serverPort)) # bind do ip do servidor com a porta
serverSocket.listen(1) # socket pronto para 'ouvir' conexoes
print ('Servidor TCP esperando conexoes na porta %d ...' % (serverPort))

while 1:
    connectionSocket, addr = serverSocket.accept() # aceita as conexoes dos clientes
    comando = connectionSocket.recv(1024) # recebe a informação do comando
    comando = comando.decode('utf-8')
    connectionSocket.send(b'OK') # TCP necessita enviar uma resposta, toda vez que uma solicitação for recebida

    os.system(comando)
    
    connectionSocket.close() # encerra o socket com o cliente

serverSocket.close() # encerra o socket do servidor