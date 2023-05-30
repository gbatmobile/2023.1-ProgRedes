import socket, time

SERVER_NAME = 'httpbin.org'
PORT = 80

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER_NAME, PORT))

HTTP_CMD = ("GET /image/png HTTP/1.1\r\n"+
            "Host: "+SERVER_NAME +"\r\n" +
            "\r\n")

sock.sendall(HTTP_CMD.encode())
buffer = sock.recv(4096)

pos2NL = buffer.find(b"\r\n\r\n")
headers = buffer[:pos2NL]
print ("Headers:", headers.decode())

for header in headers.split(b"\r\n"):
    if header.startswith(b"Content-Length:"):
        lenBody = int(header.split(b":")[1])

body = buffer[pos2NL+4:]
while len(body) < lenBody:
    body += sock.recv(4096)
sock.close()

fd = open ("file.png", "wb")
fd.write(body)
fd.close()
