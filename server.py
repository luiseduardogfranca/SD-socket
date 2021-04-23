import socket
from dao_market import Market

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

market = Market()

print("<<<   Iniciando abertura da central   >>>\n")
while True:
    connection, client = server.accept_connection()
    print(">>> Filial: ", client, "conectada.\n")

    while True: 
        code_received = connection.recv(1024).decode()
        
        if not code_received: break 

        amount_product = market.get_amount_products_by_code(code_received)
        
        connection.send(str(amount_product).encode())

        print("Produto de cod.", code_received, "com quantidade:", amount_product)
        print("Resposta enviada com sucesso.\n")
    print("<<< Finalizando conexão com a filial ", client, ".\n")
    connection.close()
