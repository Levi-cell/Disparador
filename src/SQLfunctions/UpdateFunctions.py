from conexao import cursor, conexao

def desativar_disparo(telefone):
    """
    Atualiza o disparo_status de um cliente para False (desativado),
    usando o telefone como referência.
    """
    sql = """UPDATE clientes SET disparo_status = FALSE WHERE telefone = %s """
    cursor.execute(sql, (telefone,))
    conexao.commit()


def ativar_disparo(telefone):
    """
    Atualiza o disparo_status de um cliente para False (desativado),
    usando o telefone como referência.
    """
    sql = """UPDATE clientes SET disparo_status = TRUE WHERE telefone = %s """
    cursor.execute(sql, (telefone,))
    conexao.commit()

def ativar_disparo_por_id(id_cliente):
    """
    Atualiza o disparo_status de um cliente para False (desativado),
    usando o telefone como referência.
    """
    sql = """UPDATE clientes SET disparo_status = TRUE WHERE id_cliente = %s """
    cursor.execute(sql, (id_cliente,))
    conexao.commit()

def desativar_disparo_por_id(id_cliente):
    """
    Atualiza o disparo_status de um cliente para False (desativado),
    usando o telefone como referência.
    """
    sql = """UPDATE clientes SET disparo_status = FALSE WHERE id_cliente = %s """
    cursor.execute(sql, (id_cliente,))
    conexao.commit()

def atualizar_telefone_cliente(novo_telefone, id_cliente):
    """
    Atualiza o telefone do cliente no banco de dados.
    Recebe o ID do cliente.
    """

    sql = """
        UPDATE clientes
        SET telefone = %s
        WHERE id_cliente = %s
    """

    valores = (novo_telefone, id_cliente)

    cursor.execute(sql, valores)
    conexao.commit()

def atualizar_nome_cliente(nome, id_cliente):
    """
    Atualiza o telefone do cliente no banco de dados.
    Recebe o ID do cliente.
    """

    sql = """
        UPDATE clientes
        SET nome = %s
        WHERE id_cliente = %s
    """

    valores = (nome, id_cliente)

    cursor.execute(sql, valores)
    conexao.commit()