import mysql.connector

# habilitando conexão com banco de dados.
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='filho998874_',
    database='BancoDisparo' # deixar o campo vazio
)

# habilitando cursor.
"""
Atenção, só é necessário importar a conexão caso vá deletar, atualizar e inserir dados.
Para fazer consultas não é necessário.
"""
cursor = conexao.cursor()




