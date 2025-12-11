import time
import os
import subprocess
import socket
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import pyautogui


# ============================================================
# CONFIGURAÇÃO DO CHROME REMOTO
# ============================================================

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PROFILE_PATH = r"C:\SeleniumProfile"
PORT = 9222


def porta_em_uso(porta: int) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status = sock.connect_ex(("127.0.0.1", porta)) == 0
    sock.close()
    return status


def iniciar_chrome_remoto():
    if porta_em_uso(PORT):
        print("⚠ Chrome já está aberto no modo remoto.")
        return

    comando = f'"{CHROME_PATH}" --remote-debugging-port={PORT} --user-data-dir="{PROFILE_PATH}"'
    subprocess.Popen(comando)
    time.sleep(3)
    print("✔ Chrome remoto iniciado!")


def conecta_ao_chrome_remoto():
    opcoes = Options()
    opcoes.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    return webdriver.Chrome(options=opcoes)


def trazer_chrome_para_frente(driver):
    """Apenas maximiza a janela para garantir foco."""
    try:
        driver.maximize_window()
    except:
        pass


# ============================================================
# FUNÇÃO QUE ENVIA A MÍDIA (FINAL)
# ============================================================

def enviar_foto(numero, caminho_foto):

    if not os.path.exists(caminho_foto):
        print("❌ ERRO: Foto não encontrada!")
        print(caminho_foto)
        return False

    iniciar_chrome_remoto()
    driver = conecta_ao_chrome_remoto()

    espera = WebDriverWait(driver, 20)

    # Ir para o número
    link = f"https://web.whatsapp.com/send?phone=55{numero}"
    driver.get(link)
    time.sleep(5)

    trazer_chrome_para_frente(driver)

    # Abrir o botão de anexar
    try:
        botao_clip = espera.until(
            EC.element_to_be_clickable((By.XPATH,
                """//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div/div[1]/div/span/button"""
            ))
        )
        botao_clip.click()
        print("✔ Botão de anexar clicado!")

    except Exception as e:
        print("❌ ERRO ao clicar no clipe:", e)
        return False

    time.sleep(1)

    # Clicar no item "Fotos e vídeos"
    try:
        fotos_videos = espera.until(
            EC.element_to_be_clickable((By.XPATH,
                """//*[@id="app"]/div/div/span[6]/div/ul/div/div/div[2]/li/div/span"""
            ))
        )
        fotos_videos.click()
        print("✔ Clicou em Fotos e vídeos!")

    except Exception as e:
        print("❌ ERRO ao clicar em Fotos e vídeos:", e)
        return False

    # ============================================================
    # AQUI ABRE O WINDOWS EXPLORER
    # Vamos digitar o caminho + Enter usando PyAutoGUI
    # ============================================================
    time.sleep(2)
    pyautogui.write(caminho_foto)
    pyautogui.press("enter")
    print("✔ Caminho enviado ao Windows Explorer!")

    # Aguardar o preview carregar
    time.sleep(4)

    # Clicar no botão de enviar
    try:
        enviar = espera.until(
            EC.element_to_be_clickable((By.XPATH,
                '//*[@id="app"]/div/div/div[3]/div/div[3]/div[2]/div/span/div/div/div/div[2]/div/div[2]/div[2]/div/div'
            ))
        )
        enviar.click()
        print("✔ Foto enviada com sucesso!")

    except:
        print("❌ ERRO ao clicar no botão enviar.")
        return False

    return True


# ============================================================
# EXECUTAR O ENVIO
# ============================================================

enviar_foto(
    numero="71994111866",
    caminho_foto=r"C:\Disparo\Projeto\Disparador\processDisparo\Midia\caldo.jpeg"
)









# import os
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from processDisparo.SuportFunctions.iniciar_chrome import iniciar_chrome_remoto
# from processDisparo.DisparadorMain import conecta_ao_chrome_remoto
#
#
# # ================================
# #  CONFIGURAÇÕES IMPORTANTES
# # ================================
#
# FOTO_CAMINHO = r"C:\Disparo\Projeto\Disparador\processDisparo\Midia\quarta.jpg"  # coloque o nome da foto aqui
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
