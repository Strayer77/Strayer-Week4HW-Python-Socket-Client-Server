import socket

#socket.AF_INET refers to IPv4 and socket.SOCK_STREAM refers to TCP
#defines our socket
PORT = 9500
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#binds socket, sets port to 
s.bind(( socket.gethostname(), PORT ))

s.listen(5)

#going to listen to connections in while loop
while True:
    clientsocket, address = s.accept()
    print("Connection from ", address  ," has been established!")

    data = clientsocket.recv(1024)
    decoded_data = data.decode("utf-8")

    #if the message from client is 'Hello' the server sends
    #message saying "Hi", if not - server says "Goodbye"
    if decoded_data == 'Hello':
        clientsocket.send(bytes("Hi", "utf-8"))
    else: 
        clientsocket.send(bytes("Goodbye", "utf-8"))

    clientsocket.close()

 