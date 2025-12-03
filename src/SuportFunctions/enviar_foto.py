import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime


def escolhe_foto_data():
    dia_semana = datetime.now().weekday()

    if dia_semana == 2:  # 2 = quarta
        foto = r"C:\Disparo\Projeto\Disparador\src\Midia\quarta.jpg"
        return foto

    elif dia_semana == 3:  # 3 = quinta
        foto = r"C:\Disparo\Projeto\Disparador\src\Midia\Quinta.jpg"
        return foto

    else:
        foto = r"C:\Disparo\Projeto\Disparador\src\Midia\caldo.jpeg"
        return foto

def define_foto(opcao):

    if opcao == "1":

        return escolhe_foto_data()

    elif opcao == "2":

        foto = r"C:\Disparo\Projeto\Disparador\src\Midia\ausencia.png"

        return foto

    else:

        foto = r"C:\Disparo\Projeto\Disparador\src\Midia\aviso.jpg"

        return foto



def enviar_foto_whatsapp(opcao, espera):

    foto = define_foto(opcao)
    print("\n----------- TESTANDO CAMINHO DA FOTO -----------")

    if os.path.exists(foto):
        print(f"✔ Foto encontrada!\nCaminho: {foto}")
    else:
        print(f"❌ ERRO! Foto não encontrada!\n{foto}")
        return
    time.sleep(2)
    print("-----------------------------------------------\n")

    # Abrir botão de anexar
    try:
        botao_clip = espera.until(
            EC.element_to_be_clickable((By.XPATH, """// *[ @ id = "main"] / footer / div[1] / div / span / div / div[2] / div / div[
        1] / div / span / button / div / div / div[1]"""))
        )
        botao_clip.click()
        print("✔ Botão de anexar clicado!")
    except Exception as e:
        print("❌ ERRO ao clicar no botão de anexar!")
        print(e)
        return

    time.sleep(2)

    # Input de imagem
    try:
        input_imagem = espera.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@accept='image/*,video/mp4,video/3gpp,video/quicktime']")
            )
        )
        input_imagem.send_keys(foto)
        print("✔ Foto carregada!")
    except Exception as e:
        print("❌ ERRO ao carregar a foto!")
        print(e)
        return

