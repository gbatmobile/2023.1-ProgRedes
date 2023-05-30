import socket, ssl


SERVER = 'viacep.com.br'
PORT = 80

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Para usar SSL
#context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
#sock = context.wrap_socket(sock, server_hostname=SERVER)

sock.connect((SERVER, PORT))
sock.settimeout(5)

rua = input ("Nome da rua (ou parte) a buscar Natal/RN: ")
if rua != '':
    msg   = 'GET /ws/RN/Natal/'+rua+'/json/ HTTP/1.1\r\n'
    msg  += 'Host: viacep.com.br\r\n'
    msg  += 'User-Agent: PRedesV0.1\r\n'
    msg  += 'Accept: */*\r\n'
    msg  += '\r\n'
    sock.send(msg.encode())


    data = sock.recv(16384)
    print ("Bytes lidos: ", len(data))
    print (data.decode())

sock.close()
