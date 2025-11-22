from src.SuportFunctions.PoupTxtfield import detectar_popup_ou_chat
from selenium.webdriver.support import expected_conditions as EC
from src.SuportFunctions.FunRandom import numero_randomico
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def varre_clientes(dados_clientes, mensagem, driver, espera, lista_clientes_desativados):

    for nome, telefone in dados_clientes:

        # ❗ Adiciona +55 caso não exista
        if telefone.startswith("+"):
            numero_formatado = telefone
        else:
            numero_formatado = "+55" + telefone

        print("📨 Enviando para:", numero_formatado, f"({nome})")
        print("---------------")

        mensagem_personalizada = f"{nome}, {mensagem}"

        link_whatsapp = (
            "https://web.whatsapp.com/send?"
            f"phone={numero_formatado}&text={mensagem_personalizada}"
        )

        driver.get(link_whatsapp)
        time.sleep(3) # tempo extra para o link que direciona pro numero no zap carregar
        """antes de achar encontrar o campo de texto ele irá verificar se o whatsapp avisou
        que o número é inválido caso seja inválido ele ira mudar o status para false"""
        numero_avalidar, cliente_removido = detectar_popup_ou_chat(driver, telefone)

        if numero_avalidar is False:
            print("⏭ Pulando número inválido!\n")
            lista_clientes_desativados.append(cliente_removido)
            time.sleep(3)
            continue

        campo_mensagem = espera.until(
            EC.presence_of_element_located(
                (By.XPATH, "//footer//*[@contenteditable='true']")
            )
        )

        tempo_espera_1 = numero_randomico()
        print("⏳ Esperando %s segundos antes de enviar..." % tempo_espera_1)
        time.sleep(tempo_espera_1)

        campo_mensagem.send_keys(Keys.ENTER)

        print("---------------")
        print("✔ Mensagem enviada!")

        tempo_espera_2 = numero_randomico()
        print("---------------")
        print("⏳ Intervalo de segurança: %s segundos\n" % tempo_espera_2)
        print("---------------")
        time.sleep(tempo_espera_2)

    return lista_clientes_desativados


