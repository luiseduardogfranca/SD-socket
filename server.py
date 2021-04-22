import socket

class Server():
    def __init__(self):
        self.HOST=""
        self.PORT=5000
        self.create_tcp_connection()

    def create_tcp_connection(self):
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp.bind((self.HOST, self.PORT))
    
    def run_server(self):
        self.tcp.listen(1)
    
    def accept_connection(self):
        connection, client = self.tcp.accept()
        return connection, client

server = Server()
server.run_server() 

while True:
    connection, client = server.accept_connection()
    print("Conectado por", client)

    while True: 
        msg = connection.recv(1024)
        if not msg: break 
        print(client, msg)

    print("Finalizando conex do cliente", client)
    connection.close()
