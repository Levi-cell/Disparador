import os
import shutil
import time
from selenium.webdriver.common.by import By
from processDisparo.DisparadorMain import conecta_ao_chrome_remoto
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from processDisparo.SuportFunctions.iniciar_chrome import iniciar_chrome_remoto

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
    time.sleep(2)
    print("------------------------------")
    print("⚠️ Só mecha no navegador para fazer login")
    time.sleep(2)
    print("------------------------------")
    driver = conecta_ao_chrome_remoto()

    driver.get("https://contacts.google.com/")

    # WebDriverWait(driver, 180).until(
    #     EC.presence_of_element_located((By.TAG_NAME, "body")) # desnecessario
    # )

    time.sleep(3)

    try:
        menu_button = driver.find_element(By.CSS_SELECTOR, "div[aria-label='Main menu']")
        menu_button.click()
        time.sleep(1)
    except:
        pass

    export_button = WebDriverWait(driver, 180).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="yDmH0d"]/c-wiz[2]/div/div[1]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div/div[6]/span[2]/button/div'))
    )
    export_button.click()

    time.sleep(2)

    csv_option = WebDriverWait(driver, 180).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="yDmH0d"]/div[4]/div[2]/div/div[1]/div/div[3]/div[2]/div[1]/div'))
    )
    csv_option.click()

    time.sleep(1)

    exportar_final = WebDriverWait(driver, 180).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/div[4]/div[2]/div/div[2]/div[2]/button/span[5]'))
    )
    exportar_final.click()

    print("\n✔ Download iniciado. Arquivo aparecerá em Downloads.\n")
    mover_csv()
    # Move depois que o Chrome baixar
    print("✔ Processo concluído!\n")

