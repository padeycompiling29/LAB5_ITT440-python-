import socket

s=socket.socket()
print("Berjaya buat soookett")

port=8888

s.bind(('',port))
print("Berjaya bind socket di portt:          "+str(port))

s.listen(5)
print("socket sedang menunggu client! ")

while True:
	c, addr=s.accept()
	print("Dapat capaian dari  :"+ str(addr))

	c.send(b'Terima kasih !')
	buffer=c.recv(1024)
	print(buffer)


c.close()
