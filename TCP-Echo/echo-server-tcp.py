import socket

SERVER = '127.0.0.1'
PORT = 50000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((SERVER, PORT))
sock.listen(1)

print ("aceitando conexoes ...")

con, client = sock.accept()
print ("conexão estabelecida ...")

while True:
    data = con.recv (4096)
    msg = f"received {data} from {client} ..."

    print (msg, " devolvendo ...")
    con.send (data) # msg.encode('utf-8'))

con.close()
sock.close()