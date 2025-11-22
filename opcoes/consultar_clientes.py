from opcoes.suport_functions.suport_consult import *
from tratandoErros import *

def consulta_clientes():

    clientes_consultados = mostrar_todos_os_clientes()

    print("-------------")
    print("Logo acima esta uma tabela com todos os clientes do seu banco de dados:")
    time.sleep(2)
    print("-------------")
    print("Deseja alterar algum dado de algum cliente?")

    primeira_vez = True

    clientes_modificados = []

    while True:

        if not primeira_vez:
            print("Antes de prosseguir confira o seu banco de dados novamente:")
            print("-------------")
            time.sleep(2)
            clientes_consultados = mostrar_todos_os_clientes()
            print("Deseja alterar mais algum dado de algum outro cliente?")

        primeira_vez = False

        print("[1]  → Sim")
        print("[2]  → Não (Volta ao menu principal)")
        print("⚠️ Qualquer tecla também serve como não.")
        print("⚠️ Para alterar status de disparo volte ao menu Principal.")
        opcao = input("Digite sua opção: ").strip().lower()
        print("----------")

        if opcao not in ("1", "s", "ss", "sim"):
            break

        id_cliente = input("Digite o ID do cliente:")

        id_cliente = int(id_cliente)

        cliente_encontrado = None
        for cliente in clientes_consultados:
            if cliente[0] == id_cliente:
                cliente_encontrado = cliente
                break

        if cliente_encontrado is None:
            print("❌ ID não encontrado na lista de clientes, tente novamente.")
            print("----------")
            time.sleep(2)
            continue

        id_cliente, nome, telefone_atual, disparo_status_atual = cliente_encontrado

        print(f"\n📌 Cliente selecionado: {nome}")
        print(f"📞 Telefone atual: {telefone_atual}")
        print("----------")
        time.sleep(2)

        cliente_alterado = qual_dado_quer_alterar(id_cliente)

        if cliente_alterado is not None and (cliente_alterado[1] != nome or cliente_alterado[2] != telefone_atual):
            clientes_modificados.append(cliente_alterado)
            continue

        else:
            continue

    if len(clientes_modificados) > 0:
        print("Antes de voltar ao menu principal confira os dados que você alterou:")
        print("----------")
        time.sleep(2)
        print_varios_clientes_tabela(clientes_modificados)

        return

    print("Nenhum dado foi alterado.")
    print("----------")
    time.sleep(2)

    return

