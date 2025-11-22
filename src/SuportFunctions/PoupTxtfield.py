from src.SQLfunctions.ConsultFunctions import consulta_cliente_sql
from selenium.webdriver.support import expected_conditions as EC
from src.SQLfunctions.UpdateFunctions import desativar_disparo
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time

def detectar_popup_ou_chat(driver, telefone):

    espera = WebDriverWait(driver, 30)

    try:
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

            desativar_disparo(telefone)

            novo_cliente_desativado = consulta_cliente_sql(telefone)

            print("⛔ Cliente marcado como INATIVO!")
            print("---------------")
            time.sleep(1)
            return False, novo_cliente_desativado   # ← NÃO CONTINUA O DISPARO

        # ✔ CASO CONTRÁRIO, O CHAT ABRIU NORMALMENTE
        print("📨 Chat carregado — número válido!")
        print("---------------")
        time.sleep(1)
        return True, None

    except TimeoutException:
        print("⚠ Tempo esgotado sem detectar nada!")
        return False, None