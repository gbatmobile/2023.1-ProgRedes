import socket, time, ssl


SERVER_NAME = 'portal.ifrn.edu.br'
PORT = 443
RESOURCE = "/media/images/KV-PROITEC-INSTAGRAM-STORY.2e16d0ba.fill-1080x1920.png"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER_NAME, PORT))

if PORT == 443:
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    sock = context.wrap_socket(sock, server_hostname=SERVER_NAME)

HTTP_CMD = ("GET "+RESOURCE+" HTTP/1.1\r\n"+
            "Host: "+SERVER_NAME +"\r\n" +
            "\r\n")

sock.sendall(HTTP_CMD.encode())
buffer = sock.recv(4096)

pos2NL = buffer.find(b"\r\n\r\n")
headers = buffer[:pos2NL]
print ("Headers:\n", headers.decode())

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
