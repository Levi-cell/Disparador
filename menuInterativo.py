from src.DisparadorMain import disparador_promocao
from opcoes.adicionar_lead import adiciona_cliente_na_lista
from opcoes.remover_lead import remomoca_da_lista_de_disparo
from opcoes.consultar_clientes import consulta_clientes
from tratandoErros import *


 # criar_banco_se_nao_existir() só para negócios de terceiros

parou = False
while not parou:

    print("\n📢 MENU DE DISPARO DE PROMOÇÕES")
    print("[1] - 🚀 Disparar promoções")
    print("[2] - ➕ Adicionar alguém à lista de disparo")
    print("[3] - ➖ Remover alguém da lista de disparo")
    print("[4] - 🔍 Consultar todos os Clientes e alterar dados")
    print("[5] - ❌ Sair")

    opcao = input("\nDigite a opção desejada: ")
    opcao = trata_entrada_de_opcao(opcao)


    if opcao == "1":

        disparador_promocao()
        parou = tratamento_de_retorno(parou)


    elif opcao == "2":

        adiciona_cliente_na_lista()
        parou = tratamento_de_retorno(parou)


    elif opcao == "3":

        remomoca_da_lista_de_disparo()
        parou = tratamento_de_retorno(parou)

    elif opcao == "4":

        consulta_clientes()
        parou = tratamento_de_retorno(parou)

    elif opcao == "5":
        print("\n👋 Saindo do sistema...")
        time.sleep(2)
        break

    else:
        print("\n⚠ Opção inválida. Tente novamente!")
