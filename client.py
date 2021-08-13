import socket
from time import sleep 
import json

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
        self.tcp.sendall(str(message).encode())

    def received_message(self):
        sleep(2)
        return self.tcp.recv(1024).decode()
    
    def create_request(self, method, entity, obj):
        data = {"method": method, "entity": entity, "object": obj}
        return json.dumps(data)

client = Client()
client.connect_server()

print("<<<   Iniciando conexão com a central   >>>")
print("Conectando a central da empresa. Para sair digite 0.\n")

msg_code = input("Forneçaa o código do produto (Ex.: 123): ")

while msg_code != "0":

    req = client.create_request("add", "products", {"code": "123", "name": "Margarina 200g", "price": 6.2, "quantity": 10})
    print(type(req))
    client.send_message(req)

    response = client.received_message()
    print("\n>>>>> Tem", response, "produto(s) com código", msg_code, ".\n")

    msg_code = input("Forneçaa o código do produto (Ex.: 123): ")

client.close_connection()