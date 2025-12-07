from conexao import cursor, conexao

def contatos_faltantes_do_ultimo_disparo_sql(id_anterior):
    query = """
        SELECT nome, telefone 
        FROM clientes 
        WHERE disparo_status = TRUE AND id_cliente > %s and enviou_dia = False
    """

    cursor.execute(query, (id_anterior,))
    resultado_banco = cursor.fetchall()

    return resultado_banco


def captura_tudo_banco_sql():

    cursor.execute("SELECT * FROM clientes WHERE disparo_status = TRUE")
    resultado_banco = cursor.fetchall()

    return resultado_banco

def consulta_todos_cliente_sql():

    query = """
            SELECT * FROM clientes
            
        """
    cursor.execute(query)
    resultado = cursor.fetchall()

    return resultado

def consulta_cliente_sql(telefone):
    query = """
            SELECT id_cliente, nome, telefone, disparo_status, enviou_dia
            FROM clientes
            WHERE telefone = %s
        """
    cursor.execute(query, (telefone,))
    resultado = cursor.fetchone()

    return resultado

def consulta_cliente_id_sql(id_cliente):
    query = """
            SELECT id_cliente, nome, telefone, disparo_status, enviou_dia
            FROM clientes
            WHERE id_cliente = %s
        """
    cursor.execute(query, (id_cliente,))
    resultado = cursor.fetchone()

    return resultado

def consulta_todos_clientes_indesejados_sql():
    query = """
                SELECT * FROM clientes_indesejados
            """
    cursor.execute(query)
    resultado = cursor.fetchall()

    return resultado

def lista_desativados_sql():

    cursor.execute("SELECT * FROM clientes WHERE disparo_status = FALSE")
    resultado_banco = cursor.fetchall()

    return resultado_banco


# x = consulta_todos_clientes_indesejados_sql()
# print(x)
# x = consulta_todos_cliente_sql()
#
# print(x)
#
# cursor.execute("UPDATE clientes SET disparo_status = TRUE")
# conexao.commit()

