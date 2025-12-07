from processDisparo.SQLfunctions.ConsultFunctions import consulta_cliente_sql
from processDisparo.SQLfunctions.UpdateFunctions import desativar_disparo_sql
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from processDisparo.SuportFunctions.iniciar_chrome import trazer_chrome_para_frente_e_acessar_aba
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import (
    NoSuchElementException,
    NoSuchWindowException,
    NoSuchFrameException,
    StaleElementReferenceException,
    TimeoutException,
    WebDriverException,
)

def detectar_popup_ou_chat(driver, telefone, link):

    deu_certo = True
    espera = WebDriverWait(driver, 30)
    trazer_chrome_para_frente_e_acessar_aba(link)
    try:
        trazer_chrome_para_frente_e_acessar_aba(link)
        elemento = espera.until(
            EC.any_of(
                # 🔴 POPUP de número inválido
                EC.presence_of_element_located((
                    By.XPATH,
                    "//div[@role='dialog' and contains(., 'número de telefone')]"
                )),

                # 🟢 Campo de mensagem do WhatsApp
                EC.presence_of_element_located((
                    By.XPATH,
                    "//footer//*[@contenteditable='true']"
                ))
            )
        )

        # ⚠ SE O ELEMENTO QUE APARECEU É O POPUP
        if elemento.tag_name == "div" and "dialog" in elemento.get_attribute("role"):
            print("\n❌ Número inválido detectado!")
            print("---------------")
            time.sleep(1)

            desativar_disparo_sql(telefone)

            novo_cliente_desativado = consulta_cliente_sql(telefone)

            print("⛔ Cliente marcado como INATIVO!")
            print("---------------")
            time.sleep(1)
            return False, novo_cliente_desativado, deu_certo   # ← NÃO CONTINUA O DISPARO

        # ✔ CASO CONTRÁRIO, O CHAT ABRIU NORMALMENTE
        print("📨 Chat carregado — número válido!")
        print("---------------")
        time.sleep(1)
        return True, None, deu_certo

    except (
    NoSuchElementException,
    TimeoutException,
    StaleElementReferenceException,
    WebDriverException,
    NoSuchFrameException,
    NoSuchWindowException,
)as e:
        print(e)
        print("⚠ Tempo esgotado sem detectar nada!")
        deu_certo = True
        return False, None, not deu_certo

    except Exception:
        deu_certo = True
        return False, None, not deu_certo

