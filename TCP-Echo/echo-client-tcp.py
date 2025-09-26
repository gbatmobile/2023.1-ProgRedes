# Commit para forcar analise de codigo
import socket

SERVER = '127.0.0.1'
PORT = 50000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER, PORT))

while True:
    msg = input("Digite mensagem: ")
    if msg != '':
        msgB = msg.encode('utf-8')
        sock.send (msgB)

        data = sock.recv(4096)
        msg = data.decode('utf-8')
        print (f"Echo recebido: {msg} ")

sock.close()
