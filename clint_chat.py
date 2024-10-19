import socket

host = ''
port = 3445

name = input(str("Enter Your Name:"))

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.connect((host,port))
print(s.recv(2048).decode())
while True:
    msg = input("Message")
    if(msg=="quit"):
        break
    msg = name +":"+msg
    s.sendall(msg.encode())
s.close()
