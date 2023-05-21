import socket

SERVER_IP = "10.27.2.242"
SERVER_PORT = 54321
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input("Mensagem > ")
    if message != "":
        sock.sendto(message.encode("utf-8"), (SERVER_IP, SERVER_PORT))

    data, src = sock.recvfrom(64)
    print (data.decode("utf-8"))

sock.close()

