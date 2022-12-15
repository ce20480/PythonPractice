# TCP(Transport control protocol) above IP(Internet protocol) layer
# Assumes IP layer loses information and thus stores data and resends if neccessary
# creates a pipe which connects processes together end of pipe is called a socket which is connected to ports 
# which are specific to applications/protocols
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')
mysock.close()
