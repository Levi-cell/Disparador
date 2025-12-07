from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from processDisparo.SuportFunctions.iniciar_chrome import (
    iniciar_chrome_remoto, fechar_chrome_remoto, trazer_chrome_para_frente_e_acessar_aba)
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotInteractableException,
    ElementClickInterceptedException,
    TimeoutException,
    WebDriverException,
    NoSuchWindowException,
    StaleElementReferenceException,
    InvalidElementStateException,
    UnexpectedAlertPresentException
)
import shutil
import time
import os

EXCEPTIONS = (
    NoSuchElementException,
    ElementNotInteractableException,
    ElementClickInterceptedException,
    TimeoutException,
    NoSuchWindowException,
    StaleElementReferenceException,
    InvalidElementStateException,
    UnexpectedAlertPresentException,
    WebDriverException
)



def mover_csv():
    """Move o primeiro arquivo CSV encontrado na pasta Downloads para a pasta do projeto."""
    time.sleep(3)
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


def conecta_chrome():
    opcoes_chrome = Options()
    opcoes_chrome.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

    try:
        driver = webdriver.Chrome(options=opcoes_chrome)
    except WebDriverException as e:
        print(f"❌ Erro ao conectar ao Chrome: {e}")
        print("Dica: não mexa no computador e no navegador enquanto o arquivo estiver sendo baixado")
        time.sleep(5)
        return False

    return driver


def baixa_csv():
    fechar_chrome_remoto()
    time.sleep(4)
    iniciar_chrome_remoto()
    time.sleep(2)
    print("------------------------------")
    print("⚠️ Só mexa no navegador para fazer login")
    time.sleep(2)
    print("------------------------------")

    driver = conecta_chrome()
    if not driver:
        return False

    link = "https://contacts.google.com/"
    # Acessa o Google Contacts
    try:
        driver.get(link)
        trazer_chrome_para_frente_e_acessar_aba(link)
    except (WebDriverException, NoSuchWindowException) as e:
        print(f"❌ Não foi possível abrir o site ou a janela foi fechada: {e}")
        return False

    time.sleep(3)

    # Aguarda carregamento da página

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="gb"]/div[2]/div[2]/div[2]/form/div/div/div/div/div/div[1]/input[1]'))
        )
    except TimeoutException:
        print(f"Validando elementos base")
        pass

    time.sleep(3)

    # Menu principal
    try:
        menu_button = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz[2]/div/div[1]/div[2]/div[3]/div/div[2]/div[3]')
        menu_button.click()
        time.sleep(1)
    except EXCEPTIONS:
        print(f"Validando elementos base")
        pass

    # Botão exportar
    trazer_chrome_para_frente_e_acessar_aba(link)
    try:
        trazer_chrome_para_frente_e_acessar_aba(link)
        export_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        '//*[@id="yDmH0d"]/c-wiz[2]/div/div[1]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div/div[6]/span[2]/button/div'))
        )
        export_button.click()
    except EXCEPTIONS as e:
        print(f"❌ Erro ao localizar ou clicar no botão de exportar: {e}")
        print("Dica: não mexa no computador e no navegador enquanto o arquivo estiver sendo baixado")
        time.sleep(5)
        return False

    time.sleep(2)

    # Seleciona CSV
    trazer_chrome_para_frente_e_acessar_aba(link)
    try:
        trazer_chrome_para_frente_e_acessar_aba(link)
        csv_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="yDmH0d"]/div[4]/div[2]/div/div[1]/div/div[3]/div[2]/div[1]/div'))
        )
        csv_option.click()
    except EXCEPTIONS as e:
        print(f"❌ Erro ao selecionar opção CSV: {e}")
        print("Dica: não mexa no computador e no navegador enquanto o arquivo estiver sendo baixado")
        time.sleep(5)
        return False

    time.sleep(1)

    # Exportar
    trazer_chrome_para_frente_e_acessar_aba(link)
    try:
        trazer_chrome_para_frente_e_acessar_aba(link)
        exportar_final = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/div[4]/div[2]/div/div[2]/div[2]/button/span[5]'))
        )
        exportar_final.click()
    except EXCEPTIONS as e:
        print(f"❌ Erro ao clicar no botão de exportar final: {e}")
        print("Dica: não mexa no computador e no navegador enquanto o arquivo estiver sendo baixado")
        time.sleep(5)
        return False

    print("\n✔ Download iniciado. Arquivo aparecerá em Downloads.\n")

    try:
        mover_csv()
    except Exception as e:
        print(f"❌ Erro ao mover o arquivo CSV: {e}")
        return False

    print("✔ Processo concluído!\n")
    return True
