from src.SQLfunctions.ConsultFunctions import captura_nome_numero_banco
from src.SuportFunctions.iniciar_chrome import iniciar_chrome_remoto
from src.VarreduraClientes import varre_clientes
from opcoes.gerarTabela import print_varios_clientes_tabela
from opcoes.Clientes_invalidos import clientes_invalidados
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
# from src.SuportFunctions.set_message import *
from selenium import webdriver
import time

def disparador_promocao():

    print("⚠️  ATENÇÃO, não use o dispositivo enquanto o disparador estiver sendo executado!!")
    print("⚠️  ATENÇÃO, não minimize o navegador!!")
    print("----------")
    time.sleep(2)

    iniciar_chrome_remoto()

    dados_clientes = captura_nome_numero_banco()
    print("📦 Dados dos clientes carregados!")
    print("----------")
    time.sleep(2)

    opcoes_chrome = Options()
    opcoes_chrome.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

    driver = webdriver.Chrome(options=opcoes_chrome)
    espera = WebDriverWait(driver, 60)

    print("✔ Conectado ao Chrome remoto!\n")
    print("----------")
    time.sleep(2)

    print("🌐 Abrindo o WhatsApp...")
    print("----------")
    time.sleep(2)

    link_inicial = "https://web.whatsapp.com"
    driver.get(link_inicial)

    time.sleep(5)

    lista_clientes_desativados = []
    lista_clientes_desativados = varre_clientes(
        dados_clientes, driver, espera, lista_clientes_desativados
    )

    if len(lista_clientes_desativados) > 0:
        print("🚫 O disparo terminou, confira logo abaixo os clientes inválidos...")
        print("----------")
        time.sleep(2)

        print_varios_clientes_tabela(lista_clientes_desativados)

        clientes_corrigidos = clientes_invalidados(lista_clientes_desativados)

        print(clientes_corrigidos)
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

disparador_promocao()




