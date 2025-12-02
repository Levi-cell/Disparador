from opcoes.suport_functions.suport_consult import *
from tratandoErros import *

def obter_telefone_ou_id():
    """
    Pergunta ao usuário se deseja consultar por ID ou telefone.
    Faz validação da entrada e só retorna quando for válido.
    """
    while True:
        print("\n📌 Como deseja fazer a consulta?")
        print("[1]  → 🔢 ID do cliente")
        print("[2]  → 📱 Telefone do cliente")

        escolha = input("Digite a opção desejada: ").strip()

        # Consulta por ID
        if escolha == "1":
            telefone_id = input("Digite o ID do cliente: ")
            telefone_id = trata_entrada_de_id(telefone_id)
            return int(telefone_id)

        # Consulta por telefone
        elif escolha == "2":
            telefone_id = input("Digite o telefone do cliente: ")
            telefone_id = trata_telefone(telefone_id)
            return telefone_id

        # Opção inválida
        else:
            print("❌ Opção inválida! Tente novamente.\n")

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

        if opcao not in ("1", "s", "ss", "sim", "Sim"):
            break

        telefone_id = obter_telefone_ou_id()

        cliente_encontrado = None
        for cliente in clientes_consultados:
            if cliente[2] == telefone_id or cliente[0] == telefone_id:
                cliente_encontrado = cliente
                break

        if cliente_encontrado is None:
            print("❌ Cliente não encontrado na lista de clientes, tente novamente.")
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

