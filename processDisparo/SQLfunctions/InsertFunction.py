from conexao import cursor, conexao

def inserir_cliente_sql(nome: str, telefone: str, disparo_status: bool, enviou_dia: bool):
    """
    Insere um cliente na tabela 'clientes'.
    Executa o INSERT e faz commit no banco.
    """
    sql = """
    INSERT INTO clientes (nome, telefone, disparo_status, enviou_dia)
    VALUES (%s, %s, %s, %s)
    """
    valores = (nome, telefone, disparo_status, enviou_dia)

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
