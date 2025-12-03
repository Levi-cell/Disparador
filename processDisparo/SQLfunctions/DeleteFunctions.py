from conexao import *

def deletar_tabela_sql():
    cursor.execute(f"DROP TABLE IF EXISTS clientes;")
    conexao.commit()


def deletar_cliente_por_id_sql(id_cliente):
    sql = "DELETE FROM clientes WHERE id_cliente = %s"
    cursor.execute(sql, (id_cliente,))
    conexao.commit()



