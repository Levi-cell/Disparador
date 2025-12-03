from src.SQLfunctions.ConsultFunctions import captura_nome_numero_banco_sql
from tratandoErros import confirmar_acao
from src.SuportFunctions.iniciar_chrome import iniciar_chrome_remoto
from opcoes.gerarTabela import print_varios_clientes_tabela
from opcoes.Clientes_invalidos import clientes_invalidados
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from src.VarreduraClientes import varre_clientes_com_midia, varre_clientes_sem_midia
from selenium import webdriver
import time

def conecta_ao_chrome_remoto():

    opcoes_chrome = Options()
    opcoes_chrome.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

    driver = webdriver.Chrome(options=opcoes_chrome)

    return driver

def escolhe_se_midia():
    while True:
        print("Como deseja disparar as mensagens ?")
        print("[1]  → Com midia")
        print("[2]  → Sem midia")
        escolha = input("Digite sua opção: ").strip()
        time.sleep(2)
        print("---------")

        if escolha in ("1", "2"):
            if confirmar_acao():
                return escolha
            else:
                continue
        else:
            print("❌ Opção inválida. Por favor, escolha 1 ou 2.")
            time.sleep(2)
            print("------------------------------")

def disparador_promocao():

    opcao = escolhe_se_midia()

    print("⚠️  ATENÇÃO, não use o dispositivo enquanto o disparador estiver sendo executado!!")
    print("⚠️  ATENÇÃO, não minimize o navegador!!")
    print("⚠️  Caso não esteja logado no whatsapp, tente logar dentro de 3 minutos.")
    print("----------")
    time.sleep(2)

    iniciar_chrome_remoto()

    dados_clientes = captura_nome_numero_banco_sql()
    print("📦 Dados dos clientes carregados!")
    print("----------")
    time.sleep(2)

    driver = conecta_ao_chrome_remoto()

    espera = WebDriverWait(driver, 180) # define tempo de espera por ação, use espera.until para cada comando

    print("✔ Conectado ao Chrome remoto!\n")
    print("----------")
    time.sleep(2)

    link_inicial = "https://web.whatsapp.com"
    driver.get(link_inicial)

    print("🌐 Calibrando o WhatsApp...")
    print("----------")

    time.sleep(5)

    lista_clientes_desativados = []

    if opcao == "1":
        lista_clientes_desativados = varre_clientes_com_midia(
            dados_clientes, driver, espera, lista_clientes_desativados
        )
    else:

        lista_clientes_desativados = varre_clientes_sem_midia(
            dados_clientes, driver, espera, lista_clientes_desativados
        )

    if len(lista_clientes_desativados) > 0:
        print("🚫 O disparo terminou, confira logo abaixo os clientes inválidos...")
        print("----------")
        time.sleep(2)

        print_varios_clientes_tabela(lista_clientes_desativados)

        clientes_corrigidos = clientes_invalidados(lista_clientes_desativados)

        print("----------")
        time.sleep(2)

        if len(clientes_corrigidos) > 0:
            print("🔄 Confira logo abaixo os clientes com dados alterados...")
            print("----------")
            time.sleep(2)

            print_varios_clientes_tabela(clientes_corrigidos)
        else:
            print("ℹ️ Nenhum cliente foi modificado.")
            print("----------")
            time.sleep(2)
    else:
        print("✔ Nenhum cliente estava com número inválido.")
        print("----------")
        time.sleep(2)

    print("📭 Não há mais números para enviar mensagem")
    print("----------")
    time.sleep(2)

    print("✅ Disparo finalizado!")
    print("----------")
    time.sleep(2)

    return

# def disparador_promoca_Fallback():   # Caso o disparador trave por algum problema provavelmente gerado pelo cliente
#
#     opcao = escolhe_se_midia()
#
#     print("⚠️  ATENÇÃO, não use o dispositivo enquanto o disparador estiver sendo executado!!")
#     print("⚠️  ATENÇÃO, não minimize o navegador!!")
#     print("⚠️  Caso não esteja logado no whatsapp, tente logar dentro de 3 minutos.")
#     print("----------")
#     time.sleep(2)
#
#     iniciar_chrome_remoto()
#
#     dados_clientes = captura_nome_numero_banco_sql()
#     print("📦 Dados dos clientes carregados!")
#     print("----------")
#     time.sleep(2)
#
#     driver = conecta_ao_chrome_remoto()
#
#     espera = WebDriverWait(driver, 180) # define tempo de espera por ação, use espera.until para cada comando
#
#     print("✔ Conectado ao Chrome remoto!\n")
#     print("----------")
#     time.sleep(2)
#
#     link_inicial = "https://web.whatsapp.com"
#     driver.get(link_inicial)
#
#     print("🌐 Calibrando o WhatsApp...")
#     print("----------")
#
#     time.sleep(5)
#
#     lista_clientes_desativados = []
#
#     if opcao == "1":
#         lista_clientes_desativados = varre_clientes_com_midia(
#             dados_clientes, driver, espera, lista_clientes_desativados
#         )
#     else:
#
#         lista_clientes_desativados = varre_clientes_sem_midia(
#             dados_clientes, driver, espera, lista_clientes_desativados
#         )
#
#     if len(lista_clientes_desativados) > 0:
#         print("🚫 O disparo terminou, confira logo abaixo os clientes inválidos...")
#         print("----------")
#         time.sleep(2)
#
#         print_varios_clientes_tabela(lista_clientes_desativados)
#
#         clientes_corrigidos = clientes_invalidados(lista_clientes_desativados)
#
#         print("----------")
#         time.sleep(2)
#
#         if len(clientes_corrigidos) > 0:
#             print("🔄 Confira logo abaixo os clientes com dados alterados...")
#             print("----------")
#             time.sleep(2)
#
#             print_varios_clientes_tabela(clientes_corrigidos)
#         else:
#             print("ℹ️ Nenhum cliente foi modificado.")
#             print("----------")
#             time.sleep(2)
#     else:
#         print("✔ Nenhum cliente estava com número inválido.")
#         print("----------")
#         time.sleep(2)
#
#     print("📭 Não há mais números para enviar mensagem")
#     print("----------")
#     time.sleep(2)
#
#     print("✅ Disparo finalizado!")
#     print("----------")
#     time.sleep(2)
#
#     return


