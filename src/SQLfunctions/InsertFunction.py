from conexao import cursor, conexao

def inserir_cliente_sql(nome: str, telefone: str, disparo_status: bool):
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

def inserir_cliente_indesejado_sql(nome: str, telefone: str):
    """
    Insere um cliente na tabela 'clientes'.
    Executa o INSERT e faz commit no banco.
    """
    sql = """
    INSERT INTO clientes_indesejados (nome, telefone)
    VALUES (%s, %s)
    """
    valores = (nome, telefone)

    cursor.execute(sql, valores)
    conexao.commit()
