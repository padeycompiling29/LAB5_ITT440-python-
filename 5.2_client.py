import socket
import string 

ClientSocket=socket.socket()
host='192.168.43.200'
port=8889

print('Waiting for connection - client')
try:
	ClientSocket.connect((host,port))
except socket.error as e:
	print(str(e))

Response=ClientSocket.recv(1024)
print(Response)

while True:
	keyin=input( "Say something:  " )
	ClientSocket.send(str.encode(keyin))
	Response=ClientSocket.recv(1024)
	print(Response.decode('utf-8'))

ClientSocket.close()

