from processDisparo.SQLfunctions.ConsultFunctions import consulta_todos_cliente_sql, consulta_cliente_sql, consulta_cliente_id_sql
from processDisparo.SQLfunctions.UpdateFunctions import atualizar_telefone_cliente_sql, atualizar_nome_cliente_sql
from opcoes.adicionar_lead import tratar_telefone_ja_existente
from opcoes.gerarTabela import *
from tratandoErros import *
import time


def mostrar_todos_os_clientes():
    clientes_consultados = consulta_todos_cliente_sql()
    print("Logo abaixo esta uma tabela com todos os clientes do seu banco de dados:")
    time.sleep(2)
    print_varios_clientes_tabela(clientes_consultados)
    return clientes_consultados

def altera_numero(id_cliente):

    while True:

        numero = input("Digite o novo telefone:")
        print("------")
        time.sleep(2)

        numero = trata_telefone(numero)

        telefone_consulta = consulta_cliente_sql(numero)

        if telefone_consulta is not None:
            tentar_novamente = tratar_telefone_ja_existente()

            if not tentar_novamente:
                return
            else:
                continue

        atualizar_telefone_cliente_sql(numero, id_cliente)

        dados_alterados = consulta_cliente_id_sql(id_cliente)

        print("Cliente alterado com sucesso, confira logo abaixo:")
        print("----------")
        time.sleep(2)

        print_cliente_tabela(dados_alterados)
        print("----------")
        time.sleep(2)
        print("Recomendamos que faça a mesma alteração na lista de contatos do seu telefone comercial")
        print("Alterações de números não são salvas após atualizar o banco de dados na opção 5 do menu principal.")
        print("----------")
        time.sleep(5)
        return dados_alterados


def altera_nome(id_cliente):
    while True:

        nome = input("Digite o novo nome:")

        nome = trata_nome_cliente(nome)

        atualizar_nome_cliente_sql(nome, id_cliente)

        dados_alterados = consulta_cliente_id_sql(id_cliente)

        print("Cliente alterado com sucesso, confira logo abaixo:")
        print("----------")
        time.sleep(2)
        print_cliente_tabela(dados_alterados)
        print("----------")
        time.sleep(2)
        return dados_alterados


def qual_dado_quer_alterar(id_cliente):

    primeira_vez = True

    print("O que deseja alterar do cliente?  ")
    print("----------")
    time.sleep(2)
    dados_alterados = None
    while True:

        if not primeira_vez:

            print("Ainda deseja alterar alguma coisa do cliente ou consertar alguma alteração?")
            print("Caso sim escolha uma das opções: ")
            print("----------")

        primeira_vez = False

        print("[1]  → Número")
        print("[2]  → Nome")
        print("⚠️ Pressione qualquer outra tecla para sair.")

        opcao = input("Digite sua opção: ").strip().lower()
        print("----------")

        if opcao == "1":
            dados_alterados = altera_numero(id_cliente)

        elif opcao == "2":
            dados_alterados = altera_nome(id_cliente)

        else:
            return dados_alterados


# Obervação : Caso o usuário faça uma alteração e depois reverta para o estado original, o sistema
#
