import socket

PORT = 54321
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind (('', PORT))

hostInfo = socket.gethostbyname_ex(socket.gethostname())
for ip in hostInfo[2]:
    print (f"Escutando em {ip}:{PORT}")

clients = set()

while True:
    data, src = sock.recvfrom(64)
    clients.add(src)
    data = f'{src} enviou: {data}'.encode('utf-8')

    for client in clients:
        sock.sendto(data, client)

sock.close()

