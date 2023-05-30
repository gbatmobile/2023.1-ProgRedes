import socket, time

SERVER_NAME = 'viacep.com.br'
PORT = 80
CMD = "/ws/RN/Natal/prudente/json/"

def createSocket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((SERVER_NAME, PORT))
    return sock

def sendHTTPCommand(cmd):
    HTTP_CMD = ("GET "+cmd+" HTTP/1.1\r\n"+
                "Host: "+SERVER_NAME +"\r\n" +
                "\r\n")
    sock.sendall(HTTP_CMD.encode())

def getBodyContentLen(body, lenBody):
    while len(body) < lenBody:
        body += sock.recv(4096)
    return body

def getBodyChunked(response):
    posNL = response.find(b"\r\n")
    lenChunk = int (response[:posNL], 16)
    print ("lenChunk", lenChunk)
    response = response[posNL+2:]

    while len(response) < lenChunk:
        response += sock.recv(4096)
    body = response[:lenChunk]

    return body

def getResponse():
    buffer = sock.recv(4096)

    pos2NL = buffer.find(b"\r\n\r\n")
    headers = buffer[:pos2NL]
    body = buffer[pos2NL+4:]

    print ("Headers:", headers.decode())

    for header in headers.split(b"\r\n"):
        if header.startswith(b"Content-Length:"):
            lenBody = int(header.split(b":")[1])
            body = getBodyContentLen(body, lenBody)
            break
        elif header.startswith(b"Transfer-Encoding:"):
            body = getBodyChunked(body)
            break
    return body

def saveBody(fileName, body):
    fd = open (fileName, "wb")
    fd.write(body)
    fd.close()

sock = createSocket()
sendHTTPCommand(CMD)
body = getResponse()
sock.close()
saveBody("file.bin", body)
