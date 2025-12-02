import os
import shutil
import time
import socket
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PROFILE_PATH = r"C:\SeleniumProfile"
PORT = 9222




# ============================================================================================
# FUNÇÕES AUXILIARES
# ============================================================================================

def porta_em_uso(porta: int) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status = sock.connect_ex(("127.0.0.1", porta)) == 0
    sock.close()
    return status


def iniciar_chrome_remoto():
    if porta_em_uso(PORT):
        print("⚠ Chrome já está aberto no modo remoto. Tudo certo.")
        print("---------------")
        return

    print("🚀 Iniciando Chrome em modo remoto...")
    print("---------------")

    comando = (
        f'"{CHROME_PATH}" '
        f'--remote-debugging-port={PORT} '
        f'--user-data-dir="{PROFILE_PATH}" '
        f'--disable-popup-blocking '
    )

    subprocess.Popen(comando)
    time.sleep(3)

    print("✔ Chrome remoto iniciado com sucesso!")
    print("---------------")


def conecta_ao_chrome_remoto():
    options = Options()
    options.add_experimental_option("debuggerAddress", f"127.0.0.1:{PORT}")
    return webdriver.Chrome(options=options)

def mover_csv():
    """Move o primeiro arquivo CSV encontrado na pasta Downloads para a pasta do projeto."""

    # Caminhos importantes
    downloads = os.path.join(os.path.expanduser("~"), "Downloads")
    destino_final = r"C:\Disparo\Projeto\Disparador\ProcedimentosInstalacaoDisparador"

    # Aguarda o navegador terminar o download
    time.sleep(3)

    # Lista somente arquivos CSV no Downloads
    arquivos_csv = [
        arquivo for arquivo in os.listdir(downloads)
        if arquivo.lower().endswith(".csv")
    ]

    # Caso não exista nenhum arquivo CSV
    if not arquivos_csv:
        print("❌ Nenhum arquivo CSV encontrado na pasta Downloads.")
        return

    # Seleciona o primeiro CSV encontrado
    arquivo = arquivos_csv[0]

    origem = os.path.join(downloads, arquivo)
    destino = os.path.join(destino_final, arquivo)

    # Move o arquivo
    shutil.move(origem, destino)
    print(f"✔ Arquivo movido com sucesso para: {destino}")

def baixa_csv():

    iniciar_chrome_remoto()
    driver = conecta_ao_chrome_remoto()

    driver.get("https://contacts.google.com/")

    WebDriverWait(driver, 40).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    time.sleep(3)

    try:
        menu_button = driver.find_element(By.CSS_SELECTOR, "div[aria-label='Main menu']")
        menu_button.click()
        time.sleep(1)
    except:
        pass

    export_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="yDmH0d"]/c-wiz[2]/div/div[1]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div/div[6]/span[2]/button/div'))
    )
    export_button.click()

    time.sleep(2)

    csv_option = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="yDmH0d"]/div[4]/div[2]/div/div[1]/div/div[3]/div[2]/div[1]/div'))
    )
    csv_option.click()

    time.sleep(1)

    exportar_final = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/div[4]/div[2]/div/div[2]/div[2]/button/span[5]'))
    )
    exportar_final.click()

    print("\n✔ Download iniciado. Arquivo aparecerá em Downloads.\n")
    mover_csv()
    # Move depois que o Chrome baixar
    print("✔ Processo concluído!\n")






















































# import os
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from src.SuportFunctions.iniciar_chrome import iniciar_chrome_remoto
# from src.DisparadorMain import conecta_ao_chrome_remoto
#
#
# # ================================
# #  CONFIGURAÇÕES IMPORTANTES
# # ================================
#
# FOTO_CAMINHO = r"C:\Disparo\Projeto\Disparador\src\Midia\quarta.jpg"  # coloque o nome da foto aqui
# NUMERO_WHATSAPP = "+5571994111866"  # <<<<<< número que você pediu
#
#
# def enviar_foto_whatsapp():
#     iniciar_chrome_remoto()
#     driver = conecta_ao_chrome_remoto()
#     espera = WebDriverWait(driver, 30)
#
#     print("\n----------- TESTANDO CAMINHO DA FOTO -----------")
#
#     if os.path.exists(FOTO_CAMINHO):
#         print(f"✔ Foto encontrada!\nCaminho: {FOTO_CAMINHO}")
#     else:
#         print(f"❌ ERRO! Foto não encontrada!\n{FOTO_CAMINHO}")
#         return
#
#     print("-----------------------------------------------\n")
#
#     # Acessar chat direto via link do WhatsApp
#     link = f"https://web.whatsapp.com/send?phone=55{NUMERO_WHATSAPP}"
#     driver.get(link)
#     print(f"🔄 Acessando conversa com o número: {NUMERO_WHATSAPP}")
#     time.sleep(6)
#
#     # Verificar se o número existe
#     try:
#         espera.until(
#             EC.presence_of_element_located(
#                 (By.XPATH, "//footer//*[@contenteditable='true']")
#             )
#         )
#         print("✔ Conversa carregada!")
#     except:
#         print("❌ O WhatsApp não abriu a conversa (número pode estar errado ou sem WhatsApp).")
#         return
#
#     # Abrir botão de anexar
#     try:
#         botao_clip = espera.until(
#             EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div/div[1]/button'))
#         )
#         botao_clip.click()
#         print("✔ Botão de anexar clicado!")
#     except Exception as e:
#         print("❌ ERRO ao clicar no botão de anexar!")
#         print(e)
#         return
#
#     time.sleep(1)
#
#     # Input de imagem
#     try:
#         input_imagem = espera.until(
#             EC.presence_of_element_located(
#                 (By.XPATH, "//input[@accept='image/*,video/mp4,video/3gpp,video/quicktime']")
#             )
#         )
#         input_imagem.send_keys(FOTO_CAMINHO)
#         print("✔ Foto carregada!")
#     except Exception as e:
#         print("❌ ERRO ao carregar a foto!")
#         print(e)
#         return
#
#     time.sleep(2)
#
#     # Botão enviar
#     try:
#         botao_enviar = espera.until(
#             EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div[3]/div/div[3]/div[2]/div/span/div/div/div/div[2]/div/div[2]/div[2]/div/div'))
#         )
#         botao_enviar.click()
#         print("📤 Foto enviada com sucesso!")
#     except Exception as e:
#         print("❌ ERRO ao enviar a foto!")
#         print(e)
#         return
#
#     print("\n✔ Processo finalizado!\n")
#
#
# # ================================
# #  EXECUTAR
# # ================================
#
#
#
