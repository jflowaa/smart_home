import socket

port = 5525
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("0.0.0.0", port))
sock.listen(5)
print("Listening on: 0.0.0.0:{}".format(port))

while True:
    clientsocket, address = sock.accept()
    msg = clientsocket.recv(1024)
    print(msg)
