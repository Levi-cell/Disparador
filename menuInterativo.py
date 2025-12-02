from OpcaoIndesejados.indesejados import set_indesejados
from ProcedimentosInstalacaoDisparador.mainReset import resetar_disparador
from src.SQLfunctions.ConsultFunctions import consulta_todos_cliente_sql
from opcoes.remover_lead import remomoca_da_lista_de_disparo
from opcoes.adicionar_lead import adiciona_cliente_na_lista
from opcoes.consultar_clientes import consulta_clientes
from src.DisparadorMain import disparador_promocao
from tratandoErros import *
from banco import *

## Cria banco caso não exista, # ADM pode comentar a linha 13, 15 e 9 colocar um banco na conexao.

criar_banco_se_nao_existir()

criar_table_clientes()

# antes do menu ela irá verificar se há dados para depois rodar o menu principal
def verifica_dados():
    dados = consulta_todos_cliente_sql()

    if not dados:

        print("❗️❗️️ ATENÇÃO ❗️❗️️ Você não tem cliente no seu banco de dados, acesse a opção 5 do menu...")
        time.sleep(3)

parou = False

while not parou:

    verifica_dados()

    print("\n📢 MENU DE DISPARO DE PROMOÇÕES 📢")
    print("[1] - 🚀 Disparar promoções")
    print("[2] - ➕ Adicionar alguém à lista de disparo")
    print("[3] - ➖ Remover alguém da lista de disparo")
    print("[4] - 🔍 Consultar todos os Clientes e alterar dados")
    print("[5] - 📥 Baixar nova base de dados para o disparo (Também serve para atualizar)")
    print("[6] - 📵 Colocar um contato ou mais na lista de indesejados (Blacklist)")
    print("[7] - ❌ Sair")

    opcao = input("\nDigite a opção desejada: ")
    opcao = trata_entrada_de_opcao(opcao)

    if opcao == "1":
        disparador_promocao()
        parou = tratamento_de_retorno(parou)
        if parou:
            break

    if opcao == "2":
        adiciona_cliente_na_lista()
        parou = tratamento_de_retorno(parou)
        if parou:
            break

    elif opcao == "3":

        remomoca_da_lista_de_disparo()
        parou = tratamento_de_retorno(parou)
        if parou:
            break


    elif opcao == "4":

        consulta_clientes()
        parou = tratamento_de_retorno(parou)
        if parou:
            break


    elif opcao == "5":

        resetar_disparador()
        parou = tratamento_de_retorno(parou)
        if parou:
            break

    elif opcao == "6":

        # Nova função
        set_indesejados()
        parou = tratamento_de_retorno(parou)

        if parou:
            break

    elif opcao == "7":
        print("\n👋 Saindo do sistema...")
        time.sleep(2)
        break

    else:
        print("\n⚠ Opção inválida. Tente novamente!")


