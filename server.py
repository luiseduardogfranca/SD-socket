import socket
from dao_market import Market
from codes import Codes
import json

class Server():

    def __init__(self):
        self.HOST=""
        self.PORT=5000
        self.entitys_alloweds = ["products"]
        self.create_tcp_connection()

    def create_tcp_connection(self):
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp.bind((self.HOST, self.PORT))
    
    def run_server(self):
        self.tcp.listen(1)
    
    def accept_connection(self):
        connection, client = self.tcp.accept()
        return connection, client
    
    def mount_response(self, code, msg, obj=None):
        response = {"code": code, "message": msg}

        if obj:
            response["object"] = obj
        
        return json.dumps(response)
            

    def get_response(self, request):
        codes = Codes() 
        market = Market()

        request = json.loads(request)

        if request["entity"] not in self.entitys_alloweds:
            code, msg = codes.get_msg(14)
            return self.mount_response(code, msg)

        if type(request["object"]) != dict:
            code, msg = codes.get_msg(13)
            return self.mount_response(code, msg)

        if request["method"] == "find":
            obj = request["object"]

            product = market.get_product_by_code(obj["code"])

            code, msg = codes.get_msg(10)

            if not product:
                code, msg = codes.get_msg(11)

            return self.mount_response(code, msg, product)

        elif request["method"] == "add":
            obj = request["object"]

            is_added = market.add_product(obj)
            
            code, msg = codes.get_msg(10)
        
            response = self.mount_response(code, msg, obj)

            if not is_added:
                code, msg = codes.get_msg(13)
                response = self.mount_response(code, msg)

            return response

        elif request["method"] == "del":
            obj = request["object"]

            is_removed = market.remove_product(obj["code"])
            
            code, msg = codes.get_msg(10)

            if not is_removed:
                code, msg = codes.get_msg(11)

            return self.mount_response(code, msg)

        else:
            code, msg = codes.get_msg(12)
            return self.mount_response(code, msg)



server = Server()
server.run_server() 

print("<<<   Iniciando abertura do protocolo CREATE   >>>\n")
while True:
    connection, client = server.accept_connection()
    print(">>> Filial: ", client, "conectada.\n")

    while True: 
        message_request = connection.recv(1024).decode()
        
        if not message_request: break 

        response = server.get_response(message_request)

        connection.send(str(response).encode())

        print("Resposta enviada: ", response)
        print("Resposta enviada com sucesso.\n")
    print("<<< Finalizando conexão com a filial ", client, ".\n")
    connection.close()
