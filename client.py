import socket

#socket.AF_INET refers to IPv4 and socket.SOCK_STREAM refers to TCP
#defines our socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT = 9500

#to make our connection to the server
s.connect((socket.gethostname(), PORT))

full_msg = ''
while True:
    s.sendall(bytes("Hello", "utf-8"))
    msg = s.recv(8)
    if len(msg) <= 0:
        break
    #prints our decoded message
    #print(msg.decode("utf-8"))
    full_msg += msg.decode("utf-8")

print(full_msg)