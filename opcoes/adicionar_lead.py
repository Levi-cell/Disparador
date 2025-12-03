from processDisparo.SQLfunctions.InsertFunction import inserir_cliente_sql
from processDisparo.SQLfunctions.UpdateFunctions import ativar_disparo_sql
from processDisparo.SQLfunctions.ConsultFunctions import *
from opcoes.gerarTabela import *
from tratandoErros import *
import time


# -------------------------------
# FUNÇÃO PADRÃO DE CONFIRMAÇÃO
# -------------------------------
def confirmar_acao(pergunta):
    print("\n------------------------------")
    time.sleep(1.0)

    print(f"{pergunta}")
    print("[1]  → Sim")
    print("[2]  → Não")
    print("⚠️ Qualquer tecla também serve como não.")

    resposta = input("Digite sua opção: ").strip().lower()
    print("------------------------------")

    # Aceita 1/2 como principais
    if resposta in ("1", "s", "ss", "sim", "Sim"):
        return True
    if resposta == "2":
        return False

    # Fallback para segurança
    return resposta in ("s", "sim", "ss", "sss",  "Sim")


# -------------------------------
# FUNÇÃO PARA TELEFONE EXISTENTE
# -------------------------------
def tratar_telefone_ja_existente():
    print("\n------------------------------")
    print("❌ Este número já está cadastrado no banco de dados!")
    print("------------------------------")
    time.sleep(2)


    print("🔄 Deseja tentar novamente?")
    print("[1]  → Sim")
    print("[2]  → Não (voltar)")
    print("⚠️ Qualquer tecla também serve como não.")
    escolha = input("Digite sua opção: ").strip().lower()
    print("------------------------------")

    if escolha in ("1", "s", "ss", "sim", "Sim"):
        time.sleep(1)
        return True

    else:
        time.sleep(1)
        return False


# -------------------------------
# CONFIRMAÇÕES ESPECÍFICAS
# -------------------------------
def confirmar_novo_cadastro():
    return confirmar_acao("\nDeseja cadastrar outro cliente no banco de dados?")


def confirmar_nova_adicao_lista():
    return confirmar_acao("\nDeseja adicionar outro cliente à lista de disparo?")


# -------------------------------
# REGISTRAR CLIENTE NO BANCO
# -------------------------------
def registra_cliente_no_banco(telefone_cliente):

    primeira_vez = True

    while True:
        print("----------------")
        time.sleep(1)

        if not primeira_vez:

            telefone_digitado = trata_telefone(input("Digite o telefone do novo cliente: "))
            telefone_consulta = consulta_cliente_sql(telefone_digitado)

            if telefone_consulta is not None:
                tentar_novamente = tratar_telefone_ja_existente()

                if not tentar_novamente:
                    return
                else:
                    continue

            telefone_cliente = telefone_digitado

        primeira_vez = False

        nome = trata_nome_cliente(input("Digite o nome do cliente: "))

        print("----------------")
        time.sleep(1)
        print("O cliente está apto a receber promoções da lista de disparo?")
        print("[1]  → Sim")
        print("[2]  → Não")
        print("⚠️ Qualquer tecla também serve como não.")
        disparo_input = input("Digite sua opção: ").strip()

        disparo_status = (disparo_input == "1")

        inserir_cliente_sql(nome, telefone_cliente, disparo_status)

        print("----------------")
        time.sleep(1)
        print("✔️ Cliente cadastrado com sucesso no banco!")
        time.sleep(1)

        cliente_atualizado = consulta_cliente_sql(telefone_cliente)
        print_cliente_tabela(cliente_atualizado)
        time.sleep(3)

        if not confirmar_novo_cadastro():
            break

    return


# -------------------------------
# CASO CLIENTE ESTEJA FORA DA LISTA
# -------------------------------
def processar_cliente_fora_da_lista(nome, telefone):
    print("----------------")
    print(f"⚠️ O número {telefone}, pertencente a {nome}, está no banco mas NÃO está na lista.")
    time.sleep(3)

    if confirmar_acao("Deseja colocá-lo na lista?"):
        ativar_disparo_sql(telefone)
        status_modificado = consulta_cliente_sql(telefone)

        print("✔️ Cliente adicionado à lista!")
        time.sleep(1)
        print_cliente_tabela(status_modificado)
        time.sleep(3)

        return True

    return False


# -------------------------------
# CASO CLIENTE JÁ ESTEJA NA LISTA
# -------------------------------
def processar_cliente_na_lista(nome, telefone):
    print("----------------")
    print(f"ℹ️ O número {telefone}, pertencente a {nome}, já está na lista.")
    time.sleep(2)
    print("Caso queira removê-lo, utilize a opção 3 do menu principal.")
    time.sleep(3)
    return True


# -------------------------------
# CASO CLIENTE NÃO ESTEJA CADASTRADO
# -------------------------------
def processar_cliente_nao_registrado(telefone):
    print("----------------")
    print("📭 Este telefone não está no banco de dados.")
    time.sleep(2)

    if confirmar_acao("Deseja cadastrá-lo agora?"):
        registra_cliente_no_banco(telefone)
        return True

    return False


# -------------------------------
# ADICIONA CLIENTE À LISTA
# -------------------------------
def adiciona_cliente_na_lista():

    while True:
        print("----------------")
        time.sleep(1)
        telefone = trata_telefone(input("Digite o telefone do cliente: "))
        cliente = consulta_cliente_sql(telefone)

        if cliente is not None:

            nome = cliente[1]
            telefone = cliente[2]
            status_disparo = cliente[3]

            if not status_disparo:

                processar_cliente_fora_da_lista(nome, telefone)

                if not confirmar_nova_adicao_lista():
                    break

            else:

                processar_cliente_na_lista(nome, telefone)

                if not confirmar_nova_adicao_lista():
                    break

        else:

            processar_cliente_nao_registrado(telefone)

            if not confirmar_nova_adicao_lista():
                break

    return






