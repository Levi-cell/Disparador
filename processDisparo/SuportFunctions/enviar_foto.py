import os
import time
import pyautogui
from processDisparo.SuportFunctions.iniciar_chrome import trazer_chrome_para_frente_e_acessar_aba
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
from processDisparo.SuportFunctions.FunRandom import foto_randomica
from selenium.common.exceptions import (
    NoSuchElementException,
    NoSuchWindowException,
    NoSuchFrameException,
    StaleElementReferenceException,
    TimeoutException,
    WebDriverException,
    ElementClickInterceptedException,
    ElementNotInteractableException,
    InvalidElementStateException,
    MoveTargetOutOfBoundsException,
    UnexpectedAlertPresentException,
    JavascriptException
)

def carrega_foto_windows(caminho_foto):
    time.sleep(1)
    pyautogui.write(caminho_foto)
    time.sleep(0.5)
    pyautogui.press("enter")
    print("✔ Caminho enviado ao Windows Explorer!")

def midia_aleatoria():
    midia_sorteada = foto_randomica()

    video_1 = r"C:\Disparo\Projeto\Disparador\processDisparo\Midia\video.mp4"
    foto_1 = r"C:\Disparo\Projeto\Disparador\processDisparo\Midia\caldo.jpeg"

    dict_foto = {1: video_1,
                 2: foto_1}

    for chave in dict_foto:
        if chave == midia_sorteada:
            return dict_foto[chave]


def escolhe_foto_data():
    dia_semana = datetime.now().weekday()

    if dia_semana == 2:  # 2 = quarta
        foto = r"C:\Disparo\Projeto\Disparador\processDisparo\Midia\quarta.png"
        return foto

    elif dia_semana == 3:  # 3 = quinta
        foto = r"C:\Disparo\Projeto\Disparador\processDisparo\Midia\Quinta.jpg"
        return foto

    else:
        foto = midia_aleatoria()
        return foto

def define_foto(opcao):

    if opcao == "1":

        return escolhe_foto_data()

    elif opcao == "2":

        foto = r"C:\Disparo\Projeto\Disparador\processDisparo\Midia\ausencia.png"

        return foto

    elif opcao == "3":

        foto = r"C:\Disparo\Projeto\Disparador\processDisparo\Midia\aviso.jpg"

        return foto

def enviar_foto_whatsapp(opcao, espera, link):

    deu_certo = True

    foto = define_foto(opcao)
    print("\n----------- TESTANDO CAMINHO DA FOTO -----------")

    if os.path.exists(foto):
        print(f"✔ Foto encontrada!\nCaminho: {foto}")
    else:
        print(f"❌ ERRO! Foto não encontrada!\n{foto}")
        return not deu_certo

    print("-----------------------------------------------\n")

    # Abrir botão de anexar
    trazer_chrome_para_frente_e_acessar_aba(link)
    try:
        trazer_chrome_para_frente_e_acessar_aba(link)
        botao_clip = espera.until(
            EC.element_to_be_clickable((By.XPATH, """//*[@id="main"]/footer/div[1]/div/span/div/div/div/div[1]"""))
        )
        botao_clip.click()
        print("✔ Botão de anexar clicado!")

    except (
    NoSuchElementException,
    TimeoutException,
    StaleElementReferenceException,
    WebDriverException,
    NoSuchFrameException,
    NoSuchWindowException,
    ElementClickInterceptedException,
    ElementNotInteractableException,
    InvalidElementStateException,
    MoveTargetOutOfBoundsException,
    UnexpectedAlertPresentException,
    JavascriptException,
)as e:
        print(e)
        return not deu_certo

    except Exception:
        print("❌ ERRO ao carregar a foto!")

        return not deu_certo

    # fotos e videos
    trazer_chrome_para_frente_e_acessar_aba(link)
    try:
        trazer_chrome_para_frente_e_acessar_aba(link)
        input_imagem = espera.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="app"]/div/div/span[6]/div/ul/div/div/div[2]/li/div/span')
            )
        )
        input_imagem.click()
        carrega_foto_windows(foto)

        print("✔ Foto carregada!")
        return deu_certo

    except (
    NoSuchElementException,
    TimeoutException,
    StaleElementReferenceException,
    WebDriverException,
    NoSuchFrameException,
    NoSuchWindowException,
    ElementNotInteractableException,
    InvalidElementStateException,
)as e:
        print(e)
        return not deu_certo

    except Exception:
        print("❌ ERRO ao carregar a foto!")

        return not deu_certo







"//input[@accept='image/*,video/mp4,video/3gpp,video/quicktime']"

'//*[@id="app"]/div/div/span[6]/div/ul/div/div/div[2]/li'


'//*[@id="app"]/div/div/span[6]/div/ul/div/div/div[2]/li/div/span'

'//*[@id="app"]/div/div/span[6]/div/ul/div/div/div[2]/li/div/span'

'//*[@id="app"]/div/div/span[6]/div/ul/div/div/div[2]/li/div'