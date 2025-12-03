from processDisparo.SuportFunctions.PoupTxtfield import detectar_popup_ou_chat
from selenium.webdriver.support import expected_conditions as EC
from processDisparo.SuportFunctions.set_message import escolhe_sua_mensagem
from processDisparo.SuportFunctions.FunRandom import numero_randomico
from processDisparo.SuportFunctions.enviar_foto import define_foto, enviar_foto_whatsapp
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import platform
import time
import re

try:
    import pyperclip
    _HAS_PYPERCLIP = True
except Exception:
    _HAS_PYPERCLIP = False

# FUNCAO NOVA PARA FORMATAÇÂO DE QUEBRA LINHA

def _remove_non_bmp(text: str) -> str:
    """
    Remove caracteres fora do Basic Multilingual Plane (BMP).
    Útil como fallback caso não possamos colar.
    """
    try:
        # padrão que remove pontos de código U+10000 até U+10FFFF
        return re.sub(r'[\U00010000-\U0010FFFF]', '', text)
    except re.error:
        # Em alguns builds de Python/regex a classe acima pode falhar;
        # alternativa segura: percorre e remove ord(c) > 0xFFFF
        return ''.join(ch for ch in text if ord(ch) <= 0xFFFF)

# FUNCAO NOVA PARA FORMATAÇÂO DE QUEBRA LINHA

def paste_text_into_field(campo, mensagem: str):
    """
    Copia mensagem para área de transferência e cola no campo do WhatsApp Web.
    """
    # tenta usar pyperclip para copiar o texto (mantém emojis e quebras)
    if _HAS_PYPERCLIP:
        pyperclip.copy(mensagem)
        campo.click()
        time.sleep(0.2)

        if platform.system() == "Darwin":
            campo.send_keys(Keys.COMMAND, 'v')
        else:
            campo.send_keys(Keys.CONTROL, 'v')

        time.sleep(0.2)
        return True

    # fallback: remove non-BMP e envia via send_keys (menos recomendado)
    safe = _remove_non_bmp(mensagem)
    campo.click()
    time.sleep(0.2)
    campo.send_keys(safe)
    time.sleep(0.2)
    return False

# Com as funções novas houve pequenas alterações em varre clientes que irei marcar com estrela:

def varre_clientes_com_midia(dados_clientes, driver, espera, lista_clientes_desativados):

    mensagem_escolhida, escolha = escolhe_sua_mensagem()

    for nome, telefone in dados_clientes:

        # ❗ Adiciona +55 caso não exista
        if telefone.startswith("+"):
            numero_formatado = telefone
        else:
            numero_formatado = "+55" + telefone

        print("📨 Enviando para:", numero_formatado, f"({nome})")
        print("---------------")

        mensagem_aleatoria = mensagem_escolhida
        mensagem_personalizada = f"{nome} 🌵, {mensagem_aleatoria}"

        link_whatsapp = (
            "https://web.whatsapp.com/send?"
            f"phone={numero_formatado}" # A mensagem não é mais carregada com o link
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

        ### Localiza campo de texto para inserir a mensagem no campo
        campo_mensagem = espera.until(
            EC.presence_of_element_located(
                (By.XPATH, "//footer//*[@contenteditable='true']")
            )
        )
        # aqui chamamos a função para colar nossa mensagem personalizada formatada no campo de texto
        pasted = paste_text_into_field(campo_mensagem, mensagem_personalizada)
        if pasted:
            print("📋 Mensagem colada com sucesso (via clipboard).")
        else:
            print("⚠ Fallback: mensagem enviada sem alguns emojis (sem clipboard).")

        print("Enviando foto...")
        time.sleep(1)

        enviar_foto_whatsapp(escolha, espera)

        tempo_espera_1 = numero_randomico()
        print("⏳ Esperando %s segundos antes de enviar..." % tempo_espera_1)
        time.sleep(tempo_espera_1)

        ### Localiza o botão de enviar foto junto a mensagem
        botao_enviar = espera.until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div[3]/div/div[3]/div[2]/div/span/div/div/div/div[2]/div/div[2]/div[2]/div/div'))
                )

        # campo_mensagem.send_keys(Keys.ENTER) # descomente para enviar mensagem, e comente as linhas: 109 a 112,
        # 118 a 121 e 125 a 129
        if not botao_enviar:
            print("❌Não foi encontrado o botão de enviar❌")
        # Clica no botão enviar
        botao_enviar.click()

        print("---------------")
        print("✔ Mensagem enviada!")

        tempo_espera_2 = numero_randomico()
        print("---------------")
        print("⏳ Intervalo de segurança: %s segundos\n" % tempo_espera_2)
        print("---------------")
        time.sleep(tempo_espera_2)

    return lista_clientes_desativados

def varre_clientes_sem_midia(dados_clientes, driver, espera, lista_clientes_desativados):

    mensagem_escolhida, escolha = escolhe_sua_mensagem()

    for nome, telefone in dados_clientes:

        # ❗ Adiciona +55 caso não exista
        if telefone.startswith("+"):
            numero_formatado = telefone
        else:
            numero_formatado = "+55" + telefone

        print("📨 Enviando para:", numero_formatado, f"({nome})")
        print("---------------")

        mensagem_aleatoria = mensagem_escolhida
        mensagem_personalizada = f"{nome} 🌵, {mensagem_aleatoria}"

        link_whatsapp = (
            "https://web.whatsapp.com/send?"
            f"phone={numero_formatado}" # A mensagem não é mais carregada com o link
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

        ### Localiza campo de texto para inserir a mensagem no campo
        campo_mensagem = espera.until(
            EC.presence_of_element_located(
                (By.XPATH, "//footer//*[@contenteditable='true']")
            )
        )
        # aqui chamamos a função para colar nossa mensagem personalziada formatada no campo de texto
        pasted = paste_text_into_field(campo_mensagem, mensagem_personalizada)
        if pasted:
            print("📋 Mensagem colada com sucesso (via clipboard).")
        else:
            print("⚠ Fallback: mensagem enviada sem alguns emojis (sem clipboard).")

        # print("Enviando foto...")
        # time.sleep(1)
        #
        # enviar_foto_whatsapp(espera)

        tempo_espera_1 = numero_randomico()
        print("⏳ Esperando %s segundos antes de enviar..." % tempo_espera_1)
        time.sleep(tempo_espera_1)

        ### Localiza o botão de enviar foto junto a mensagem
        # botao_enviar = espera.until(
        #             EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div[3]/div/div[3]/div[2]/div/span/div/div/div/div[2]/div/div[2]/div[2]/div/div'))
        #         )

        campo_mensagem.send_keys(Keys.ENTER) # descomente para enviar mensagem, e comente as linhas: 109 a 112,
        # 118 a 121 e 125 a 129
        # if not botao_enviar:
        #     print("❌Não foi encontrado o botão de enviar❌")
        # # Clica no botão enviar
        # botao_enviar.click()

        print("---------------")
        print("✔ Mensagem enviada!")

        tempo_espera_2 = numero_randomico()
        print("---------------")
        print("⏳ Intervalo de segurança: %s segundos\n" % tempo_espera_2)
        print("---------------")
        time.sleep(tempo_espera_2)

    return lista_clientes_desativados


###### FUNCAO ANTIGA, DELETE TUDO QUE TEM ACIMA E DESCOMENTE TUDO ABAIXO #####
###### ESTÁ 100% FUNCIONA E SEM BUGS, SOMENTE NÃO FORMATA QUEBRA LINHA ######



# from processDisparo.SuportFunctions.PoupTxtfield import detectar_popup_ou_chat
# from processDisparo.SuportFunctions.enviar_foto import enviar_foto_whatsapp
# from selenium.webdriver.support import expected_conditions as EC
# from processDisparo.SuportFunctions.set_message import mensagem_do_dia
# from processDisparo.SuportFunctions.FunRandom import numero_randomico
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import platform
# import time
# import re

# def varre_clientes(dados_clientes, driver, espera, lista_clientes_desativados):
#
#     for nome, telefone in dados_clientes:
#
#         # ❗ Adiciona +55 caso não exista
#         if telefone.startswith("+"):
#             numero_formatado = telefone
#         else:
#             numero_formatado = "+55" + telefone
#
#         print("📨 Enviando para:", numero_formatado, f"({nome})")
#         print("---------------")
#
#         mensagem_aleatoria = mensagem_do_dia()
#         mensagem_personalizada = f"{nome} 🌵, {mensagem_aleatoria}"
#
#         link_whatsapp = (
#             "https://web.whatsapp.com/send?"
#             f"phone={numero_formatado}&text={mensagem_personalizada}"
#         )
#
#         driver.get(link_whatsapp)
#         time.sleep(3) # tempo extra para o link que direciona pro numero no zap carregar
#         """antes de achar encontrar o campo de texto ele irá verificar se o whatsapp avisou
#         que o número é inválido caso seja inválido ele ira mudar o status para false"""
#         numero_avalidar, cliente_removido = detectar_popup_ou_chat(driver, telefone)
#
#         if numero_avalidar is False:
#             print("⏭ Pulando número inválido!\n")
#             lista_clientes_desativados.append(cliente_removido)
#             time.sleep(3)
#             continue
#
#         ### Localiza campo de texto para inserir a mensagem no campo
#         espera.until(
#             EC.presence_of_element_located(
#                 (By.XPATH, "//footer//*[@contenteditable='true']")
#             )
#         )
#
#         print("Enviando foto...")
#         time.sleep(1)
#
#         enviar_foto_whatsapp(espera)
#
#         tempo_espera_1 = numero_randomico()
#         print("⏳ Esperando %s segundos antes de enviar..." % tempo_espera_1)
#         time.sleep(tempo_espera_1)
#
#         #### Localiza o botão de enviar foto junto a mensagem
#         botao_enviar = espera.until(
#                     EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div[3]/div/div[3]/div[2]/div/span/div/div/div/div[2]/div/div[2]/div[2]/div/div'))
#                 )
#
#         if not botao_enviar:
#             print("❌Não foi encontrado o botão de enviar❌")
#         # Clica no botão enviar
#         botao_enviar.click()
#
#         print("---------------")
#         print("✔ Mensagem enviada!")
#
#         tempo_espera_2 = numero_randomico()
#         print("---------------")
#         print("⏳ Intervalo de segurança: %s segundos\n" % tempo_espera_2)
#         print("---------------")
#         time.sleep(tempo_espera_2)
#
#     return lista_clientes_desativados
#

