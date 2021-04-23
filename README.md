# Trabalho SD - Socket 

### Descrição 
##### Uma filial consulta estoque de material na central

A filial informa um produto através do seu código e a central deverá responder a quantidade disponível em estoque deste mesmo produto também através do código informado.

### Pré-requisitos 
- Python (versão 3)
- socket 

### Como executar?

O projeto está dividido em três arquivos, que são: *client.py*, *server.py* e *dao_market.py*. 

- client.py: contém todas as funcionalidades pra abertura de conexão com o servidor bem como a leitura de dados e tratamento das respostas referente a quantidade de produtos em estoque.

- server.py: contém a implementação para a leitura das requests vindo do client e o processamento dos dados com a classe de acesso a dados contida no arquivo dao_market.py

- dao_market.py: contém a gerência dos dados bem como a inicialização do array de dados simulando uma lista de produtos. Essa classe é respnsável por buscar o produto pelo código passado e fazer o cálculo dos valores de cada produto solictado em estoque.

Dado a explicação acima de cada arquivo, podemos passar para o passo a passo de execução do projeto.

#### Passos

Considerando que você já esteja dentro do folder do projeto.

1. Abra dois terminais, ou duas abas, e em cada terminal execute o seguinte comando: 

```bash
python3 server.py
```
e em outro terminal:
```bash
python3 client.py
```

2. No terminal do client, basta que você envie os dados como bem solicitado. No caso, o código do produto. 

3. Para finalizar o programa no lado client basta digitar o valor *0*.

### Equipe:

- Luís Eduardo Gomes França
