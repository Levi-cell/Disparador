from conexao import *

def inserir_contatos_no_banco():

    caminho = r"C:\Disparo\Projeto\Disparador\ProcedimentosInstalacaoDisparador\contatos.txt"

    with open(caminho, "r", encoding="utf-8") as f:
        linhas = f.readlines()

    for linha in linhas:
        linha = linha.strip()

        # Ignora cabeçalho e linhas fora do padrão
        if not linha.startswith("- "):
            continue

        # Remove "- "
        linha = linha[2:]

        try:
            # Divide em nome e número
            nome, numero = linha.split("|||")
            nome = nome.strip()
            numero = numero.strip()

            # Comando SQL
            sql = """
                INSERT INTO clientes (nome, telefone, disparo_status)
                VALUES (%s, %s, %s)
            """

            cursor.execute(sql, (nome, numero, True))

        except Exception as e:
            print(f"Erro ao processar linha: {linha}")
            print(e)

    conexao.commit()
    print("Todos os contatos foram inseridos com sucesso!")



def encontrar_telefones_duplicados_sql():
    """
    Retorna uma lista de tuplas (telefone, count, [ids]) para telefones com mais de 1 ocorrência.
    Usa SQL (MySQL) para agrupar no servidor.
    """
    sql = """
        SELECT telefone, COUNT(*) AS cnt, GROUP_CONCAT(id_cliente SEPARATOR ',') AS ids
        FROM clientes
        GROUP BY telefone
        HAVING cnt > 1;
    """
    cursor.execute(sql)
    resultados = cursor.fetchall()  # cada linha: (telefone, cnt, ids)

    # transforma ids em lista de ints
    duplicados = []
    for telefone, cnt, ids in resultados:
        lista_ids = [int(x) for x in ids.split(",")] if ids else []
        duplicados.append((telefone, int(cnt), lista_ids))

    return duplicados

def remover_duplicados():
    duplicados = encontrar_telefones_duplicados_sql()

    if not duplicados:
        print("Nenhum telefone duplicado encontrado.")
        return

    for telefone, count, lista_ids in duplicados:
        # queremos manter apenas 1 ID
        id_para_manter = lista_ids[0]

        # todos os outros serão deletados
        ids_para_deletar = lista_ids[1:]

        if ids_para_deletar:
            # monta placeholders (%s, %s, %s...)
            placeholders = ",".join(["%s"] * len(ids_para_deletar))

            sql = f"DELETE FROM clientes WHERE id_cliente IN ({placeholders})"
            cursor.execute(sql, ids_para_deletar)

            print(f"Telefone {telefone}: mantendo ID {id_para_manter}, removendo IDs {ids_para_deletar}")

    conexao.commit()
    print("\n✔ Todos os números repetidos foram removidos com sucesso!")

