from conexao import *
####### O banco só sera criado para negócios de terceiros, desconsidere pro caldão
def criar_banco_se_nao_existir():
    """
    Cria o banco e tabela apenas se não existirem.
    Pode ser executada toda vez sem problemas.
    """

    # Criar banco
    cursor.execute("CREATE DATABASE IF NOT EXISTS BancoDisparo")
    cursor.execute("USE BancoDisparo")

    # Criar tabela
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id_cliente INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            telefone VARCHAR(20) NOT NULL,
            disparo_status BOOLEAN NOT NULL
        ) COMMENT = 'Tabela de clientes da loja';
    """)

    conexao.commit()   # Salva alterações
    print("✔ Banco e tabela verificados/criados com sucesso!")

