import socket
import sys
 
# Create a TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
server_address = ('0.0.0.0', 2222)
s.bind(server_address)
print >>sys.stderr, 'starting up on %s port %s' % sock.getsockname()
s.listen(1)

while True:
	print >>sys.stderr, 'waiting for a connection'
	client, address = s.accept()
while True:
data = client.recv(1024)
if not data: break
if data == "Close" or data == "close": client.close()
client.send(data)
client.close()