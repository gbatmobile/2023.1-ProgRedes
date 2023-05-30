import socket, time

SERVER_NAME = 'viacep.com.br'
PORT = 80
RUA = "fonseca"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER_NAME, PORT))

HTTP_CMD = ("GET /ws/RN/Natal/"+RUA+"/json/ HTTP/1.1\r\n"+
            "Host: "+SERVER_NAME +"\r\n" +
            "\r\n")

sock.send(HTTP_CMD.encode())
time.sleep(10)
buffer = sock.recv(32000)

pos2NL = buffer.find(b"\r\n\r\n")
headers = buffer[:pos2NL]
body = buffer[pos2NL+4:]

print ("Headers:", headers.decode())
print ("-"*80)
print ("Body:", body.decode())

print ("Len read:", len(buffer))
print ("Len body:", len(body))
sock.close()