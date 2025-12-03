from processDisparo.SQLfunctions.ConsultFunctions import consulta_cliente_id_sql
from tratandoErros import trata_entrada_de_id
from opcoes.suport_functions.suport_invalidados import *
import time


def clientes_invalidados(lista_de_invalidados):

    clientes_alterados = []
    primeira_vez = True

    while True:

        if len(lista_de_invalidados) == 0:
            print("\n✔ Todos os telefones foram alterados.")
            print("----------")
            time.sleep(3)
            return clientes_alterados

        # Pergunta inicial e repetida padronizada
        if primeira_vez:
            print("\nDeseja alterar o telefone de algum cliente?")
        else:
            print("\nDeseja alterar mais algum telefone?")

        print("[1]  → Sim")
        print("[2]  → Não")
        print("⚠️ Qualquer tecla também serve como não.")
        opcao = input("Digite sua opção: ").strip()
        print("----------")
        time.sleep(2)

        primeira_vez = False

        if opcao not in ("1", "s", "ss", "sim", "Sim"):
            print("Encerrando tratamento...")
            print("-----------")
            time.sleep(2)
            return clientes_alterados

        id_digitado = input("Digite o ID do cliente que deseja alterar: ").strip()
        print("----------")
        time.sleep(2)

        id_digitado = trata_entrada_de_id(id_digitado)
        id_digitado = int(id_digitado)

        cliente_encontrado = None
        for cliente in lista_de_invalidados:
            if cliente[0] == id_digitado:
                cliente_encontrado = cliente
                break

        if cliente_encontrado is None:
            print("❌ ID não encontrado na lista de clientes inválidos, tente novamente.")
            print("----------")
            time.sleep(2)
            continue

        id_cliente, nome, telefone_atual, disparo_status_atual = cliente_encontrado

        print(f"\n📌 Cliente selecionado: {nome}")
        print(f"📞 Telefone atual: {telefone_atual}")
        print("----------")
        time.sleep(2)

        novo_numero = captura_novo_telefone()
        alterou_telefone = False

        if novo_numero is not None:
            alterou_telefone = confirma_alteracao_telefone(novo_numero, id_cliente)

        alterou_disparo = define_status_disparo(id_cliente)

        if alterou_telefone or alterou_disparo:
            cliente_modificado = consulta_cliente_id_sql(id_cliente)
            clientes_alterados.append(cliente_modificado)
            lista_de_invalidados.remove(cliente_encontrado)
            print("✔ Cliente foi modificado e removido da lista de inválidos.")
            print("----------")
            time.sleep(2)

    return clientes_alterados


