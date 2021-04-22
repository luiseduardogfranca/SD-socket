import socket

class Client():
    def __init__(self):
        self.HOST="127.0.0.1"
        self.PORT=5000
        self.create_tcp_connection()

    def create_tcp_connection(self):
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def connect_server(self):
        self.tcp.connect((self.HOST, self.PORT))

    def close_connection(self):
        self.tcp.close()

    def send_message(self, message):
        self.tcp.send(b"message")

client = Client()
client.connect_server()

print("Conectando ao servidor. Para sair digite 0.")
msg = input("Forneca a menssagem:")

while msg != "0":
    client.send_message(msg)
    msg = input("Forneca a menssagem:")

client.close_connection()