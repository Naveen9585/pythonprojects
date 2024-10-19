import socket
from threading import Thread
 
host = ''
port = 3445

def start_chat_server(conn,addr):
    t = ChatServerThread(conn,addr)
    t.start()
    print("Connection recieved from {}:{}".format(addr[0],addr[1]))

class ChatServerThread(Thread):
    def __init__(self,conn,addr):
        Thread.__init__(self)
        self.conn = conn
        self.addr = addr

    def run(self):
        self.conn.sendall(b"Type your Messages here...\n")
        while True:
            try:
                data = self.conn.recv(2048)
                if not data:
                    self.conn.close()
                    continue
                elif data == exit or data == quit:
                    self.conn.close()
                else:
                    try:
                        data = data.decode()
                        print(data)
                    except:
                        pass
            except:
                pass

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host,port))
s.listen()
while True:
    conn,addr = s.accept()
    start_chat_server(conn,addr)
s.close()
