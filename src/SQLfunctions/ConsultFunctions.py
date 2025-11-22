from conexao import cursor, conexao

def captura_nome_numero_banco():

    cursor.execute("SELECT nome, telefone FROM clientes WHERE disparo_status = TRUE")
    resultado_banco = cursor.fetchall()

    return resultado_banco

def captura_tudo_banco():

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
            SELECT id_cliente, nome, telefone, disparo_status
            FROM clientes
            WHERE telefone = %s
        """
    cursor.execute(query, (telefone,))
    resultado = cursor.fetchone()

    return resultado

def consulta_cliente_sql_id(id_cliente):
    query = """
            SELECT id_cliente, nome, telefone, disparo_status
            FROM clientes
            WHERE id_cliente = %s
        """
    cursor.execute(query, (id_cliente,))
    resultado = cursor.fetchone()

    return resultado


# x = consulta_todos_cliente_sql()
#
# print(x)
#
# cursor.execute("UPDATE clientes SET disparo_status = TRUE")
# conexao.commit()

