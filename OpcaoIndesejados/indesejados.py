import time
from tratandoErros import *
from tratandoErros import trata_telefone, trata_entrada_de_id
from opcoes.gerarTabela import print_varios_clientes_tabela, print_varios_indesejados_tabela
from src.SQLfunctions.InsertFunction import inserir_cliente_indesejado_sql
from src.SQLfunctions.DeleteFunctions import deletar_cliente_por_id_sql
from src.SQLfunctions.ConsultFunctions import consulta_todos_cliente_sql, lista_desativados_sql, consulta_todos_clientes_indesejados_sql


# ------------------------------------------------------------
#   Funções de interface visual
# ------------------------------------------------------------
def linha():
    print("\n" + "─" * 60 + "\n")

def titulo(txt):
    linha()
    print(f"📌 {txt}")
    linha()
    time.sleep(1)


# ------------------------------------------------------------
def escolhe_como_selecionar():
    time.sleep(3)
    titulo("Seleção de Cliente")

    while True:
        print("Como deseja selecionar o cliente?")
        print(" [1] 🔢 Pelo ID")
        print(" [2] 📱 Pelo Telefone")
        linha()

        escolha = input("Digite sua opção: ").strip()

        if escolha == "1":
            telefone_id = input("\nDigite o ID do cliente: ").strip()
            telefone_id = trata_entrada_de_id(telefone_id)
            return int(telefone_id)

        elif escolha == "2":
            telefone_id = input("\nDigite o telefone do cliente: ").strip()
            telefone_id = trata_telefone(telefone_id)
            return telefone_id

        else:
            print("❌ Opção inválida! Tente novamente.\n")
            time.sleep(2)


# ------------------------------------------------------------
def valida_cliente(clientes_consultados, telefone_id):

    for cliente in clientes_consultados:
        if cliente[2] == telefone_id or cliente[0] == telefone_id:
            return cliente

    print("❌ Cliente não encontrado. Tente novamente.")
    linha()
    time.sleep(2)
    return None


# ------------------------------------------------------------
def confirma_acao():
    titulo("Confirmação de Segurança ⚠️")
    print("Caso mude de ideia, será necessário falar com o desenvolvedor.")
    time.sleep(2)

    print("\nTem certeza que deseja mover o(s) cliente(s) para a Black-list?")
    print(" [1] ✔️  Sim")
    print(" [2] ❌  Não")
    linha()

    escolha = input("Digite sua opção: ").strip().lower()

    if escolha in ("1", "s", "ss", "sim"):
        return True
    return False


# ------------------------------------------------------------
def move_para_black_list(id_cliente, nome, telefone):
    inserir_cliente_indesejado_sql(nome, telefone)
    deletar_cliente_por_id_sql(id_cliente)


# ------------------------------------------------------------
def move_clientes_desativados(clientes_desativados):

    for cliente in clientes_desativados:
        id_cliente = cliente[0]
        nome_cliente = cliente[1]
        telefone_cliente = cliente[2]
        move_para_black_list(id_cliente, nome_cliente, telefone_cliente)

    titulo("✔️ Clientes movidos para a Black-list!")
    print("Retornando ao menu...")
    time.sleep(2)


# ------------------------------------------------------------
def set_indesejados():

    titulo("Gerenciamento de Clientes Indesejados ⚠️")

    print("Adicionar alguém à Black-list o remove automaticamente da lista de disparo.")
    time.sleep(2)

    primeira_vez = True

    while True:
        linha()
        time.sleep(2)

        if primeira_vez:
            print("O que deseja fazer?")
            primeira_vez = False
        else:
            print("Deseja adicionar mais alguém à Black-list? Escolha uma opção:")

        print("\n [1] ➕ Adicionar um cliente específico a black-list")
        print(" [2] 📤 Mover todos os clientes fora do disparo para a black-list")
        print(" ↩️ Qualquer outra tecla para voltar ao menu principal")
        linha()

        escolha = input("Digite sua opção: ").strip()

        # ------------------------------------------------------------
        if escolha == "1":
            titulo("Lista Completa de Clientes")

            todos_clientes = consulta_todos_cliente_sql()

            if len(todos_clientes) < 1:
                print("⚠️ Nenhum cliente encontrado no banco de dados.")
                time.sleep(2)
                break

            print_varios_clientes_tabela(todos_clientes)
            linha()
            time.sleep(2)

            id_ou_telefone = escolhe_como_selecionar()

            cliente_encontrado = valida_cliente(todos_clientes, id_ou_telefone)
            if cliente_encontrado is None:
                continue

            id_cliente, nome, telefone_atual, disparo_status_atual = cliente_encontrado

            titulo("Cliente Selecionado")
            print(f"🧑 Nome: {nome}")
            print(f"📞 Telefone: {telefone_atual}")
            linha()
            time.sleep(2)

            if not confirma_acao():
                print("↩️ Operação cancelada, retornando...")
                time.sleep(2)
                continue

            move_para_black_list(id_cliente, nome, telefone_atual)

            titulo("✔️ Cliente movido para a Black-list!")
            time.sleep(2)
            continue

        # ------------------------------------------------------------
        elif escolha == "2":
            titulo("Clientes Fora do Disparo")

            clientes_desativados = lista_desativados_sql()

            if len(clientes_desativados) < 1:
                print("⚠️ Nenhum cliente desativado encontrado.")
                time.sleep(2)
                break

            print_varios_clientes_tabela(clientes_desativados)
            linha()
            time.sleep(2)

            if not confirma_acao():
                continue

            move_clientes_desativados(clientes_desativados)

        else:
            break

    titulo("Black-list Atual 📃")

    clientes_blacklist = consulta_todos_clientes_indesejados_sql()

    if len(clientes_blacklist) > 0:
        print("⚠️ Para remover alguém da Black-list, contate o desenvolvedor.")
        time.sleep(2)

        print("\nMesmo após resetar o sistema, clientes indesejados são mantidos por segurança.")
        linha()
        time.sleep(2)

        print("Lista atual:")
        print_varios_indesejados_tabela(clientes_blacklist)
        linha()
        time.sleep(2)

        print("Retornando ao menu principal...")
        time.sleep(2)
        return

    print("Nenhum cliente na Black-list no momento.")
    print("Retornando ao menu principal...")
    time.sleep(4)


