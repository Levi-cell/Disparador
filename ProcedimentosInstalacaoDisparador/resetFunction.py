import time
from banco import *
from processDisparo.SQLfunctions.DeleteFunctions import *
from processDisparo.SQLfunctions.InsertFunction import inserir_cliente_sql
from tratandoErros import trata_telefone, trata_nome_cliente
from ProcedimentosInstalacaoDisparador.processFunctions import *
from ProcedimentosInstalacaoDisparador.automatedDownload import *
from opcoes.consultar_clientes import tratar_telefone_ja_existente
from ProcedimentosInstalacaoDisparador.tratando_csv import molda_txt_completo
from opcoes.gerarTabela import print_varios_clientes_tabela, print_cliente_tabela
from processDisparo.SQLfunctions.ConsultFunctions import consulta_cliente_sql, consulta_todos_cliente_sql


def perguntar_se_quer_inserir_testes():
    print("Antes de armazenar novos contatos, deseja adicionar contatos de teste por segurança? (recomendável) 🛡️")
    print("[1]  → Sim")
    print("[2]  → Não")
    print("⚠️ Qualquer tecla também serve como não.")
    escolha = input("Digite sua opção: ").strip().lower()
    print("------------------------------")
    return escolha in ("1", "s", "ss", "sim")


def perguntar_se_deseja_continuar():
    print("\nDeseja adicionar mais algum contato de teste? 🤔")
    print("[1] → Sim")
    print("[2] → Não")
    escolha = input("Digite sua opção: ").strip().lower()
    return escolha in ("1", "s", "sim")


def solicitar_telefone():
    telefone = input("Digite o número do contato de teste: ")
    print("----------------")
    time.sleep(2)
    return trata_telefone(telefone)


def solicitar_nome():
    nome = input("Digite o nome do contato de teste: ")
    print("----------------")
    time.sleep(2)
    return trata_nome_cliente(nome)

def adicionar_contato_teste():
    telefone = solicitar_telefone()
    telefone_consulta = consulta_cliente_sql(telefone)

    if telefone_consulta is not None:
        tentar_novamente = tratar_telefone_ja_existente()
        return None if not tentar_novamente else "retry"

    nome = solicitar_nome()

    inserir_cliente_sql(nome, telefone, True, False)
    return telefone


def mostrar_contato_adicionado(telefone):
    contato_teste = consulta_cliente_sql(telefone)
    print("Contato de teste adicionado com sucesso! 🎉 Confira abaixo:")
    print("----------------")
    time.sleep(2)
    print_cliente_tabela(contato_teste)

def insere_dados_teste():

    if not perguntar_se_quer_inserir_testes():
        return

    primeira_vez = True

    while True:

        if primeira_vez:
            print("Adicione quantos contatos de achar necessário... 📝")
            print("----------------")
            time.sleep(3)
            primeira_vez = False
        else:
            if not perguntar_se_deseja_continuar():
                print("Prosseguindo para baixar novos contatos... ⏳")
                print("----------------")
                time.sleep(2)
                return

        resultado = adicionar_contato_teste()

        if resultado is None:
            return
        elif resultado == "retry":
            continue
        else:
            mostrar_contato_adicionado(resultado)

def deletar_csv():
    pasta = r"C:\Disparo\Projeto\Disparador\ProcedimentosInstalacaoDisparador"

    # lista todos os arquivos da pasta
    arquivos = os.listdir(pasta)

    encontrou = False

    for arquivo in arquivos:
        if arquivo.lower().endswith(".csv"):
            caminho = os.path.join(pasta, arquivo)
            os.remove(caminho)
            print(f"✔ CSV antigo deletado: {caminho}")
            encontrou = True

    if not encontrou:
        print("❌ Nenhum arquivo CSV encontrado na pasta.")

def deletar_txt():
    pasta = r"C:\Disparo\Projeto\Disparador\ProcedimentosInstalacaoDisparador"

    # lista todos os arquivos da pasta
    arquivos = os.listdir(pasta)

    encontrou = False

    for arquivo in arquivos:
        if arquivo.lower().endswith(".txt"):
            caminho = os.path.join(pasta, arquivo)
            os.remove(caminho)
            print(f"✔ Txt antigo deletado: {caminho}")
            encontrou = True

    if not encontrou:
        print("❌ Nenhum arquivo Txt encontrado na pasta.")

# Chamada da função
def baixa_nova_base_de_dados():

    deletar_csv()
    deletar_txt()

    time.sleep(2)
    print("------------------------")
    print("❗️ATENÇÃO❗️ No primeiro acesso ao navegador o sistema pode pedir login...")
    print("------------------------")
    time.sleep(2)
    print("caso isso aconteça pare o programa quando o google abrir, faça login, e execute o sistema de novo...")
    time.sleep(4)
    print("------------------------")


    foi = baixa_csv()

    if not foi:
        return
    # Baixando novo csv

    molda_txt_completo()  # Molda o novo txt salvando as alterações e black-list do banco antigo
    deletar_tabela_sql()  # agora podemos deletar a tabela

    criar_table_clientes()  # Cria banco caso não exista para evitar erro em comandos SQL

    insere_dados_teste() # Insere dados de teste.

    inserir_contatos_no_banco() # Insere contatos no banco a partir do novo txt.

    remover_duplicados() # Remove contatos com números iguais dentro do banco.
    time.sleep(2)

    dados = consulta_todos_cliente_sql()
    print("------------------------")
    print("Confira os clientes que foram adicionados logo abaixo sem duplicações de número:")
    time.sleep(2)
    print_varios_clientes_tabela(dados)
    print("Logo acima você verá os clientes que foram adicionados sem duplicações de número")
    time.sleep(2)
    print("------------------------")
    time.sleep(2)

    print("Caso você queira alterar o nome de um cliente "
          "acesse a opção 6 do menu principal em seguida escolha 'sim'")

    time.sleep(5)
    return
