from conexao import cursor, conexao

def inserir_cliente(nome: str, telefone: str, disparo_status: bool):
    """
    Insere um cliente na tabela 'clientes'.
    Executa o INSERT e faz commit no banco.
    """
    sql = """
    INSERT INTO clientes (nome, telefone, disparo_status)
    VALUES (%s, %s, %s)
    """
    valores = (nome, telefone, disparo_status)

    cursor.execute(sql, valores)
    conexao.commit()
