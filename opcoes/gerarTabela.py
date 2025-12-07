def print_cliente_tabela(resultado):
    """
    Exibe o cliente recém-adicionado em formato de tabela.
    Agora inclui a coluna disparo_status.
    """

    id_cliente, nome, telefone, disparo_status, enviou_dia = resultado

    # Converte booleano para texto mais legível
    status_formatado = "Ativo" if disparo_status else "Inativo"

    # Cabeçalho

    print("+------------+-------------------------------+------------------+----------------+")
    print("| ID Cliente | Nome                          | Telefone         | Disparo Status |")
    print("+------------+-------------------------------+------------------+----------------+")

    # Linha com dados formatados
    print(f"| {str(id_cliente).ljust(10)} | {nome.ljust(29)} | {telefone.ljust(16)} | {status_formatado.ljust(14)} |")

    print("+------------+-------------------------------+------------------+----------------+")

def print_varios_clientes_tabela(registros):
    """
    Exibe uma lista de clientes em formato de tabela.
    Cada registro deve conter: (id_cliente, nome, telefone, disparo_status)
    """


    # Cabeçalho
    print("+------------+-------------------------------+------------------+----------------+")
    print("| ID Cliente | Nome                          | Telefone         | Disparo Status |")
    print("+------------+-------------------------------+------------------+----------------+")

    for registro in registros:
        id_cliente, nome, telefone, disparo_status, enviou_dia = registro

        status_formatado = "Ativo" if disparo_status else "Inativo"

        print(
            f"| {str(id_cliente).ljust(10)} | "
            f"{nome.ljust(29)} | "
            f"{telefone.ljust(16)} | "
            f"{status_formatado.ljust(14)} |"
        )

    print("+------------+-------------------------------+------------------+----------------+")

def print_varios_indesejados_tabela(registros):
    """
    Exibe uma lista de clientes em formato de tabela.
    Cada registro deve conter: (id_cliente, nome, telefone, disparo_status)
    """


    # Cabeçalho
    print("+------------+-------------------------------+------------------")
    print("| ID Cliente | Nome                          | Telefone         ")
    print("+------------+-------------------------------+------------------")

    for registro in registros:
        id_cliente, nome, telefone = registro


        print(
            f"| {str(id_cliente).ljust(10)} | "
            f"{nome.ljust(29)} | "
            f"{telefone.ljust(16)} | "
        )

    print("+------------+-------------------------------+------------------")
