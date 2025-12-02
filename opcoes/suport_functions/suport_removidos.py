from src.SQLfunctions.ConsultFunctions import *
from opcoes.gerarTabela import print_varios_clientes_tabela
from tratandoErros import *

def mostrar_lista_de_clientes():
    lista_clientes = captura_tudo_banco_sql()

    print("Esses são os clientes na lista, confira logo abaixo:")
    time.sleep(2)
    print("-------------")

    print_varios_clientes_tabela(lista_clientes)

    print("Logo acima você pode conferir os clientes na lista...")
    print("---------")

    return lista_clientes