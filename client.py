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
    
    def show_response(self, response):
        data = json.loads(response)
        code = data["code"] if "code" in data else None
        msg = data["message"] if "message" in data else None
        obj = data["object"] if "object" in data else None

        print("\n==========")
        print("Resposta protocolo CREATE")
        print("\nCódigo da request:", code)
        print("Menssagem:", msg)
        if (type(obj) is dict):
            print("\nInformação do objeto:\n")
            for key in obj.keys():
                print("\t" + str(key) + ": " + str(obj[key]))
            print()
        print("==========\n")

client = Client()
client.connect_server()

print("<<<   Iniciando conexão com a central   >>>")
print("Conectando a central da empresa. Para sair digite 0.\n")

msg_code = input("Funções disponíveis: \n\n\t1 - FIND - (Buscar produto por code) \n\t2 - ADD - (Adicionar produto) \n\t3 - DEL - (Deletar produto) \n\t0 - Encerrar programa \n>>> ")

while msg_code != "0":
    if msg_code == "1":
        print(">>> \nBuscando por produto...\n")
        code = input("Forneça o código: ")

        req = client.create_request("find", "products", {"code": code})
        client.send_message(req)
        response = client.received_message()

        client.show_response(response)

    elif msg_code == "2":
        print(">>> \nForneça os dados do produto\n")
        
        code = input("Código: ")
        name = input("Nome: ")
        price = input("Preço: ")
        quantity = input("Quantidade: ")

        req = client.create_request("add", "products", {"code": code, "name": name, "price": price, "quantity": quantity})
        
        client.send_message(req)
        response = client.received_message()

        client.show_response(response)

    elif msg_code == "3":
        print(">>> \nForneça o código do produto a ser removido")
        code = input("Código: ")

        req = client.create_request("del", "products", {"code": code})
        client.send_message(req)
        response = client.received_message()

        client.show_response(response)

    msg_code = input("Funções disponíveis: \n\n\t1 - FIND - (Buscar produto por code) \n\t2 - ADD - (Adicionar produto) \n\t3 - DEL - (Deletar produto) \n\t0 - Encerrar programa \n>>> ")

client.close_connection()