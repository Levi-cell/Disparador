from opcoes.suport_functions.suport_removidos import mostrar_lista_de_clientes
from src.SQLfunctions.UpdateFunctions import desativar_disparo_por_id
from src.SQLfunctions.ConsultFunctions import consulta_cliente_sql_id
from opcoes.gerarTabela import print_varios_clientes_tabela
from opcoes.suport_functions.suport_invalidados import *

def perguntar_continuar_remocao():
    print("\nDeseja remover mais algum cliente?")
    print("[1] → Sim")
    print("[2] → Não")
    escolha = input("Digite sua opção: ").strip().lower()

    if escolha in ("1", "s", "ss", "sim"):
        return True
    return False

def remomoca_da_lista_de_disparo():

    lista_clientes = mostrar_lista_de_clientes()

    clientes_removidos = []

    primeira_vez = True
    while True:

        if len(lista_clientes) == 0:
            print("\n✔ Não restou mais nenhum cliente para remover, todos os clientes foram removidos da lista"
                  "de disparo com sucesso.")
            print("----------")
            time.sleep(2)
            break

        if primeira_vez:
            id_cliente = input("Digite o ID do cliente que deseja remover da lista de disparo:")
        else:
            id_cliente = input("Digite o ID de algum cliente novamente:")

        primeira_vez = False

        id_cliente = int(id_cliente)

        cliente_encontrado = None
        for cliente in lista_clientes:
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

        print(f"Deseja remover {nome} da lista de disparo? ")
        print("[1]  → Sim")
        print("[2]  → Não")
        print("⚠️ Qualquer tecla também serve como não.")
        escolha = input("Digite sua opção: ").strip()
        print("----------")
        time.sleep(2)

        if escolha in ("1", "s", "ss", "sim"):
            desativar_disparo_por_id(id_cliente)
            lista_clientes.remove(cliente_encontrado)

            cliente_removido = consulta_cliente_sql_id(id_cliente)
            clientes_removidos.append(cliente_removido)
            print("✅ Cliente removido da lista com sucesso!")
            time.sleep(1)

            print("Confira os clientes que ainda estão na lista logo abaixo:")
            print("-------------")
            print_varios_clientes_tabela(lista_clientes)
            print("-------------")
            print("Confira os clientes que ainda estão na lista logo acima:")
            print("-------------")

        else:
            print(f"{nome} não foi removido")

        if not perguntar_continuar_remocao():
            break

    if len(clientes_removidos) > 0:
        print("O(s) cliente(s) foram removidos com sucesso, confira logo abaixo:")
        time.sleep(1)
        print("----------")
        print_varios_clientes_tabela(clientes_removidos)
        time.sleep(2)

        return

    print("--------")
    print("Ninguém saiu ou entrou na lista de disparo")

    return











