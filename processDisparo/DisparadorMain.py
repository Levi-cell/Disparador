from processDisparo.SQLfunctions.ConsultFunctions import (
    consulta_cliente_sql,
    contatos_faltantes_do_ultimo_disparo_sql,
    consulta_cliente_id_sql
)
from processDisparo.SuportFunctions.iniciar_chrome import (
    iniciar_chrome_remoto,
    fechar_chrome_remoto,
    trazer_chrome_para_frente_e_acessar_aba
)
from processDisparo.SQLfunctions.UpdateFunctions import (
    marcar_enviou_dia_sql,
    desativar_enviou_dia_sql
)
from processDisparo.SuportFunctions.PoupTxtfield import detectar_popup_ou_chat
from processDisparo.SuportFunctions.enviar_foto import enviar_foto_whatsapp
from processDisparo.SuportFunctions.FunRandom import numero_randomico
from selenium.webdriver.support import expected_conditions as EC
from opcoes.gerarTabela import print_varios_clientes_tabela
from opcoes.Clientes_invalidos import clientes_invalidados
from processDisparo.SuportFunctions.set_message import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from tratandoErros import confirmar_acao
from selenium import webdriver
import platform
import time
import re
from selenium.common.exceptions import (
    NoSuchElementException, NoSuchWindowException, NoSuchFrameException,
    StaleElementReferenceException, TimeoutException, WebDriverException,
    ElementClickInterceptedException, ElementNotInteractableException,
    InvalidElementStateException, MoveTargetOutOfBoundsException,
    UnexpectedAlertPresentException, JavascriptException,
    InvalidSessionIdException
)
from urllib3.exceptions import MaxRetryError

def prepara_disparo():

    id_cliente = 0
    midia = escolhe_se_midia()
    tipo_mensagem = escolhe_sua_mensagem()
    disparador_promocao(id_cliente, midia, tipo_mensagem)

    print("📭 Não há mais números para enviar mensagem")
    print("----------")
    time.sleep(2)

    print("✅ Disparo finalizado!")
    print("----------")
    time.sleep(2)

    desativar_enviou_dia_sql()
    return

def trata_erro_inicial(id_cliente_anterior, midia, tipo_message):
    fechar_chrome_remoto()
    id_proximo = id_cliente_anterior + 1
    dados = consulta_cliente_id_sql(id_proximo)

    if dados[4]:
        return

    dados_clientes = contatos_faltantes_do_ultimo_disparo_sql(id_cliente_anterior)

    if len(dados_clientes) < 1:
        print("Não há contatos para disparar por enquanto...")
        time.sleep(2)
        print("Fechando o google...")
        time.sleep(2)
        fechar_chrome_remoto()
        return


    print("Algo deu errado no disparo... ")
    time.sleep(2)

    print("Vamos tentar reiniciar o disparador e voltar de onde parou...")
    time.sleep(2)

    print(f"Nome do ultimo cliente: {dados[1]}.")
    time.sleep(2)

    print(f"Número do ultimo cliente: {dados[2]}")
    time.sleep(2)

    disparador_promocao(id_cliente_anterior, midia, tipo_message)
    return

def conecta_ao_chrome_remoto():
    opcoes_chrome = Options()
    opcoes_chrome.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

    try:
        driver = webdriver.Chrome(options=opcoes_chrome)
        return driver

    except (WebDriverException, ConnectionRefusedError, TimeoutException,
            InvalidSessionIdException, MaxRetryError) as e:
        print(e)

        if "DevToolsActivePort" in str(e):
            return False

        return False

    except Exception as e:
        print(e)
        return False

def escolhe_se_midia():
    while True:
        print("Como deseja disparar as mensagens ?")
        print("[1] → Com midia")
        print("[2] → Sem midia")
        escolha = input("Digite sua opção: ").strip()
        time.sleep(2)
        print("---------")

        if escolha in ("1", "2"):
            if confirmar_acao():
                return escolha
            else:
                continue
        else:
            print("❌ Opção inválida. Por favor, escolha 1 ou 2.")
            time.sleep(2)
            print("------------------------------")

def abre_link(driver, link_inicial):
    try:
        driver.get(link_inicial)
        trazer_chrome_para_frente_e_acessar_aba(link_inicial)
        return True

    except (WebDriverException, ConnectionRefusedError, TimeoutException,
            InvalidSessionIdException, MaxRetryError) as e:
        print(e)

        if "DevToolsActivePort" in str(e):
            return False

        return False

    except Exception as e:
        print(e)
        return False

def tratativa_disparo(nome, telefone, midia, tipo_message):
    fechar_chrome_remoto()

    dados_ultimo_cliente = consulta_cliente_sql(telefone)
    id_ultimo_cliente = dados_ultimo_cliente[0]
    dados = consulta_cliente_id_sql(id_ultimo_cliente)

    id_ultimo_cliente = id_ultimo_cliente - 1

    if dados[4]:
        return

    dados_clientes = contatos_faltantes_do_ultimo_disparo_sql(id_ultimo_cliente)

    if len(dados_clientes) < 1:
        print("Não há contatos para disparar por enquanto...")
        time.sleep(2)
        print("Fechando o google...")
        time.sleep(2)
        fechar_chrome_remoto()
        return

    print("Algo deu errado no disparo... ")
    time.sleep(2)

    print("Vamos tentar reiniciar o disparador e voltar de onde parou...")
    time.sleep(2)

    print(f"Nome do ultimo cliente: {nome}.")
    time.sleep(2)

    print(f"Número do ultimo cliente: {telefone}")
    time.sleep(2)

    disparador_promocao(id_ultimo_cliente, midia, tipo_message)
    return

def disparador_promocao(id_cliente, midia, tipo_message):
    fechar_chrome_remoto()
    dados_clientes = contatos_faltantes_do_ultimo_disparo_sql(id_cliente)

    if len(dados_clientes) < 1:
        print("Não há contatos para disparar por enquanto...")
        time.sleep(2)
        print("Fechando o google...")
        time.sleep(2)
        fechar_chrome_remoto()
        return

    print("⚠️ ATENÇÃO, não minimize o navegador!")
    print("----------")
    time.sleep(2)
    print("⚠️ ATENÇÃO, se possível não utilize o dispositivo, assim o disparador será mais rapido!")
    print("----------")
    time.sleep(2)
    print("⚠️ ATENÇÃO, não feche o navegador e não use o navegador do disparo!!")
    print("----------")
    time.sleep(2)
    print("⚠️ Caso não esteja logado no whatsapp, encerre o programa, logue no whatsapp em seguida inicie o programa de novo.")
    print("----------")
    time.sleep(2)

    iniciar_chrome_remoto()

    print("📦 Dados dos clientes carregados!")
    print("----------")
    time.sleep(2)

    driver = conecta_ao_chrome_remoto()
    if not driver:
        trata_erro_inicial(id_cliente, midia, tipo_message)
        return

    espera = WebDriverWait(driver, 30)

    print("✔ Conectado ao Chrome remoto!\n")
    print("----------")
    time.sleep(2)

    link_inicial = "https://web.whatsapp.com"
    foi = abre_link(driver, link_inicial)

    if not foi:
        trata_erro_inicial(id_cliente, midia, tipo_message)
        return


    print("🌐 Calibrando o WhatsApp...")
    print("----------")
    time.sleep(8)

    lista_clientes_desativados = []

    if midia == "1":
        lista_clientes_desativados = varre_clientes_com_midia(
            dados_clientes, driver, espera, lista_clientes_desativados, tipo_message, midia
        )
    else:
        lista_clientes_desativados = varre_clientes_sem_midia(
            dados_clientes, driver, espera, lista_clientes_desativados, tipo_message, midia
        )

    if lista_clientes_desativados is not None and len(lista_clientes_desativados) > 0:
        print("🚫 O disparo terminou, confira logo abaixo os clientes inválidos...")
        print("----------")
        time.sleep(2)
        print_varios_clientes_tabela(lista_clientes_desativados)

        clientes_corrigidos = clientes_invalidados(lista_clientes_desativados)

        print("----------")
        time.sleep(2)

        if len(clientes_corrigidos) > 0:
            print("🔄 Confira logo abaixo os clientes com dados alterados...")
            print("----------")
            time.sleep(2)
            print_varios_clientes_tabela(clientes_corrigidos)
        else:
            print("ℹ️ Nenhum cliente foi modificado.")
            print("----------")
            time.sleep(2)

    return

try:
    import pyperclip
    _HAS_PYPERCLIP = True
except Exception:
    _HAS_PYPERCLIP = False

def _remove_non_bmp(text: str) -> str:
    try:
        return re.sub(r'[\U00010000-\U0010FFFF]', '', text)
    except re.error:
        return ''.join(ch for ch in text if ord(ch) <= 0xFFFF)

def paste_text_into_field(campo, mensagem: str):
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

    safe = _remove_non_bmp(mensagem)
    campo.click()
    time.sleep(0.2)
    campo.send_keys(safe)
    time.sleep(0.2)
    return False

def localiza_campo_texto(espera, link_whatsapp):
    foi = True
    try:
        trazer_chrome_para_frente_e_acessar_aba(link_whatsapp)
        campo_mensagem = espera.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div/div/div[3]/div[1]')
            )
        )
        campo_mensagem.send_keys(Keys.CONTROL, "a")
        campo_mensagem.send_keys(Keys.BACKSPACE)
        return campo_mensagem, foi

    except (
        NoSuchElementException, TimeoutException, StaleElementReferenceException,
        WebDriverException, NoSuchFrameException, NoSuchWindowException,
    ) as e:
        print(e)
        return None, not foi

    except Exception as e:
        print(e)
        return None, not foi

def cola_mensagem_campo(link_whatsapp, campo_mensagem, mensagem_personalizada):

    try:
        trazer_chrome_para_frente_e_acessar_aba(link_whatsapp)
        pasted = paste_text_into_field(campo_mensagem, mensagem_personalizada)

        if pasted:
            print("📋 Mensagem colada com sucesso (via clipboard).")
            return True
        else:
            print("⚠ Fallback: mensagem enviada sem alguns emojis (sem clipboard).")

    except (
        NoSuchElementException, TimeoutException, StaleElementReferenceException,
        WebDriverException, NoSuchFrameException, NoSuchWindowException,
        ElementNotInteractableException, InvalidElementStateException,
    ) as e:
        print(e)
        return False

    except Exception as e:
        print(e)
        return False

## possível função descontinuada
def envia_foto_botao(link_whatsapp, espera):

    try:
        trazer_chrome_para_frente_e_acessar_aba(link_whatsapp)
        botao_enviar = espera.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="app"]/div/div/div[3]/div/div[3]/div[2]/div/span/div/div/div/div[2]/div/div[2]/div[2]/span/div/div')
            )
        )
        botao_enviar.click()
        return True

    except (
        NoSuchElementException, TimeoutException, StaleElementReferenceException,
        WebDriverException, NoSuchFrameException, NoSuchWindowException,
        ElementClickInterceptedException, ElementNotInteractableException,
        InvalidElementStateException, MoveTargetOutOfBoundsException,
        UnexpectedAlertPresentException, JavascriptException,
    ) as e:
        print(e)
        print("❌ Não foi encontrado o botão de enviar ❌")
        return False

    except Exception as e:
        print(e)
        print("❌ Não foi encontrado o botão de enviar ❌")
        return False

def varre_clientes_com_midia(
    dados_clientes, driver, espera, lista_clientes_desativados,
    tipo_message, midia
):

    nao_disparo = nao_quer_disparo()

    for nome, telefone in dados_clientes:

        evita_dupla_mensagem = consulta_cliente_sql(telefone)
        if evita_dupla_mensagem[4]:
            print(f"Já enviou para esse numero {telefone} pulando para o proximo...")
            continue

        if telefone.startswith("+"):
            numero_formatado = telefone
        else:
            numero_formatado = "+55" + telefone

        print("📨 Enviando para:", numero_formatado, f"({nome})")
        print("---------------")

        mensagem_aleatoria = None
        if tipo_message == "1":
            mensagem_aleatoria = mensagem_do_dia()
        elif tipo_message == "2":
            mensagem_aleatoria = aviso_ausencia()
            mensagem_aleatoria = mensagem_aleatoria + nao_disparo
        elif tipo_message == "3":
            mensagem_aleatoria = mensagem_atualizacao()
            mensagem_aleatoria = mensagem_aleatoria + nao_disparo

        mensagem_personalizada = f"{nome} 🌵, {mensagem_aleatoria}"

        link_whatsapp = (
            "https://web.whatsapp.com/send?"
            f"phone={numero_formatado}"
        )

        # ABRINDO LINK DO ZAP

        foi = abre_link(driver, link_whatsapp)
        if not foi:
            tratativa_disparo(nome, telefone, midia, tipo_message)
            return

        time.sleep(3)

        ### DETECTA POPUP OU CHAT

        numero_avalidar, cliente_removido, deu_certo = detectar_popup_ou_chat(
            driver, telefone, link_whatsapp
        )
        if not deu_certo:
            tratativa_disparo(nome, telefone, midia, tipo_message)
            return
        time.sleep(1)
        # NUMEROS INVÁLIDOS CAEM AQUI

        if numero_avalidar is False and cliente_removido is not None:
            print("⏭ Pulando número inválido!\n")
            lista_clientes_desativados.append(cliente_removido)
            time.sleep(3)
            continue

        ## LOCALIZANDO CAMPO DE TEXTO E DELETANDO TUDO QUE TIVER NELE
        campo_mensagem, foi = localiza_campo_texto(espera, link_whatsapp)
        if not foi:
            tratativa_disparo(nome, telefone, midia, tipo_message)
            return

        time.sleep(1)
        ### COLA A MENSAGEM NO CAMPO DE TEXTO

        foi = cola_mensagem_campo(
            link_whatsapp, campo_mensagem, mensagem_personalizada
        )
        if not foi:
            tratativa_disparo(nome, telefone, midia, tipo_message)
            return

        time.sleep(1)

        ## TENTA ANEXAR FOTO NO CAMPO CHAT

        print("tentando anexar foto...")

        time.sleep(1)

        deu_certo = enviar_foto_whatsapp(
            tipo_message, espera, link_whatsapp
        )
        if not deu_certo:
            tratativa_disparo(nome, telefone, midia, tipo_message)
            return

        time.sleep(1)
        ## APERTA O BOTAO FINAL PARA ENVIAR MENSAGEM COM FOTO + TEXTO

        tempo_espera_1 = numero_randomico()
        print("⏳ Esperando %s segundos antes de enviar..." % tempo_espera_1)
        time.sleep(tempo_espera_1)
        foi = envia_foto_botao(link_whatsapp, espera)

        if not foi:
            tratativa_disparo(nome, telefone, midia, tipo_message)
            return

        time.sleep(1)

        print("---------------")
        print("✔ Mensagem enviada!")

        time.sleep(1)
        marcar_enviou_dia_sql(telefone)

        tempo_espera_2 = numero_randomico()
        print("---------------")
        print("⏳ Intervalo de segurança: %s segundos\n" % tempo_espera_2)
        print("---------------")
        time.sleep(tempo_espera_2)

    return lista_clientes_desativados

def varre_clientes_sem_midia(
    dados_clientes, driver, espera, lista_clientes_desativados,
    tipo_message, midia
):

    nao_disparo = nao_quer_disparo()

    for nome, telefone in dados_clientes:

        evita_dupla_mensagem = consulta_cliente_sql(telefone)
        if evita_dupla_mensagem[4]:
            print(f"Já enviou para esse numero {telefone} pulando para o proximo...")
            continue

        if telefone.startswith("+"):
            numero_formatado = telefone
        else:
            numero_formatado = "+55" + telefone

        print("📨 Enviando para:", numero_formatado, f"({nome})")
        print("---------------")

        mensagem_aleatoria = None
        if tipo_message == "1":
            mensagem_aleatoria = mensagem_do_dia()
        elif tipo_message == "2":
            mensagem_aleatoria = aviso_ausencia()
            mensagem_aleatoria = mensagem_aleatoria + nao_disparo
        elif tipo_message == "3":
            mensagem_aleatoria = mensagem_atualizacao()
            mensagem_aleatoria = mensagem_aleatoria + nao_disparo

        mensagem_personalizada = f"{nome} 🌵, {mensagem_aleatoria}"

        link_whatsapp = (
            "https://web.whatsapp.com/send?"
            f"phone={numero_formatado}"
        )

        # ABRINDO LINK DO NUMERO

        foi = abre_link(driver, link_whatsapp)
        if not foi:
            tratativa_disparo(nome, telefone, midia, tipo_message)
            return

        time.sleep(3)

        # DETECTANDO POPUP OU TEXTO

        numero_avalidar, cliente_removido, deu_certo = detectar_popup_ou_chat(
            driver, telefone, link_whatsapp
        )

        time.sleep(1)

        if not deu_certo:
            tratativa_disparo(nome, telefone, midia, tipo_message)
            return

        # NUMEROS INVALIDOS CAEM AQUI

        if numero_avalidar is False and cliente_removido is not None:
            print("⏭ Pulando número inválido!\n")
            lista_clientes_desativados.append(cliente_removido)
            time.sleep(3)
            continue

        # LOCALIZA O CAMPO TEXTO E DELETA TUDO QUE TEM NELE
        campo_mensagem, foi = localiza_campo_texto(espera, link_whatsapp)
        if not foi:
            tratativa_disparo(nome, telefone, midia, tipo_message)


        time.sleep(1)
        # COLA MENSAGEM NO CAMPO TEXTO

        foi = cola_mensagem_campo(
            link_whatsapp, campo_mensagem, mensagem_personalizada
        )
        if not foi:
            tratativa_disparo(nome, telefone, midia, tipo_message)
            return

        time.sleep(1)

        tempo_espera_1 = numero_randomico()
        print("⏳ Esperando %s segundos antes de enviar..." % tempo_espera_1)
        time.sleep(tempo_espera_1)

        # ENVIA MENSAGEM
        foi = envia_mensagem_enter(campo_mensagem)
        if not foi:
            tratativa_disparo(nome, telefone, midia, tipo_message)
            return

        time.sleep(1)

        print("---------------")
        print("✔ Mensagem enviada!")

        time.sleep(1)

        marcar_enviou_dia_sql(telefone)

        tempo_espera_2 = numero_randomico()
        print("---------------")
        print("⏳ Intervalo de segurança: %s segundos\n" % tempo_espera_2)
        print("---------------")
        time.sleep(tempo_espera_2)

    return lista_clientes_desativados


def envia_mensagem_enter(campo_mensagem):
    try:
        campo_mensagem.send_keys(Keys.ENTER)
        return True

    except (
        NoSuchElementException, TimeoutException, StaleElementReferenceException,
        WebDriverException, NoSuchFrameException, NoSuchWindowException,
        ElementNotInteractableException, InvalidElementStateException,
    ) as e:
        print(e)
        return False















"""FUNÇÔES SALVAS QUE PODEM SER UTEIS EM FUTURAS ATUALIAÇÔES DO ZAP """

# def varre_clientes_com_midia(
#     dados_clientes, driver, espera, lista_clientes_desativados,
#     tipo_message, midia
# ):
#     for nome, telefone in dados_clientes:
#
#         evita_dupla_mensagem = consulta_cliente_sql(telefone)
#         if evita_dupla_mensagem[4]:
#             print(f"Já enviou para esse numero {telefone} pulando para o proximo...")
#             continue
#
#         if telefone.startswith("+"):
#             numero_formatado = telefone
#         else:
#             numero_formatado = "+55" + telefone
#
#         print("📨 Enviando para:", numero_formatado, f"({nome})")
#         print("---------------")
#
#         mensagem_aleatoria = None
#         if tipo_message == "1":
#             mensagem_aleatoria = mensagem_do_dia()
#         elif tipo_message == "2":
#             mensagem_aleatoria = aviso_ausencia()
#         elif tipo_message == "3":
#             mensagem_aleatoria = mensagem_atualizacao()
#
#         mensagem_personalizada = f"{nome} 🌵, {mensagem_aleatoria}"
#
#         link_whatsapp = (
#             "https://web.whatsapp.com/send?"
#             f"phone={numero_formatado}"
#         )
#
#         foi = abre_link(driver, link_whatsapp)
#         if not foi:
#             tratativa_disparo(nome, telefone, midia, tipo_message)
#             return
#
#         trazer_chrome_para_frente_e_acessar_aba(link_whatsapp)
#         time.sleep(3)
#
#         ### DETECTA POPUP OU CHAT
#
#         numero_avalidar, cliente_removido, deu_certo = detectar_popup_ou_chat(
#             driver, telefone, link_whatsapp
#         )
#         if not deu_certo:
#             tratativa_disparo(nome, telefone, midia, tipo_message)
#             return
#
#         if numero_avalidar is False and cliente_removido is not None:
#             print("⏭ Pulando número inválido!\n")
#             lista_clientes_desativados.append(cliente_removido)
#             time.sleep(3)
#             continue
#
#         ## LIMPANDO TEXTO DO CAMPO PRIMARIO SEM MIDIA
#
#         trazer_chrome_para_frente_e_acessar_aba(link_whatsapp)
#         campo_mensagem, foi = localiza_campo_texto(espera, link_whatsapp)
#         if not foi:
#             tratativa_disparo(nome, telefone, midia, tipo_message)
#             return
#
#         ## ENVIANDO FOTO
#
#         print("tentando anexar foto...")
#         time.sleep(1)
#
#         trazer_chrome_para_frente_e_acessar_aba(link_whatsapp)
#         deu_certo = enviar_foto_whatsapp(
#             tipo_message, espera, link_whatsapp
#         )
#         if not deu_certo:
#             tratativa_disparo(nome, telefone, midia, tipo_message)
#             return
#
#         ### LOCALIZANDO CAMPO TEXTO DA MIDIA E DELETA QUALQUER CARACTER
#
#         trazer_chrome_para_frente_e_acessar_aba(link_whatsapp)
#         campo_mensagem, foi = localiza_campo_texto_midia(espera, link_whatsapp)
#         if not foi:
#             tratativa_disparo(nome, telefone, midia, tipo_message)
#             return
#
#         ### COLA A MENSAGEM NO CAMPO DE TEXTO DA MIDIA LIMPO
#
#         foi = cola_mensagem_campo(
#             link_whatsapp, campo_mensagem, mensagem_personalizada
#         )
#         if not foi:
#             tratativa_disparo(nome, telefone, midia, tipo_message)
#             return
#
#         ## ENVIANDO MENSAGEM COM TEXTO E FOTO
#
#         tempo_espera_1 = numero_randomico()
#         print("⏳ Esperando %s segundos antes de enviar..." % tempo_espera_1)
#         time.sleep(tempo_espera_1)
#
#         trazer_chrome_para_frente_e_acessar_aba(link_whatsapp)
#         foi = envia_foto_botao(link_whatsapp, espera)
#
#         if not foi:
#             tratativa_disparo(nome, telefone, midia, tipo_message)
#             return
#
#         print("---------------")
#         print("✔ Mensagem enviada!")
#
#         marcar_enviou_dia_sql(telefone)
#
#         tempo_espera_2 = numero_randomico()
#         print("---------------")
#         print("⏳ Intervalo de segurança: %s segundos\n" % tempo_espera_2)
#         print("---------------")
#         time.sleep(tempo_espera_2)
#
#     return lista_clientes_desativados



# def localiza_campo_texto_midia(espera, link_whatsapp):
#     foi = True
#     try:
#         trazer_chrome_para_frente_e_acessar_aba(link_whatsapp)
#         campo_mensagem = espera.until(
#             EC.presence_of_element_located(
#                 (By.XPATH, '//*[@id="app"]/div/div/div[3]/div/div[3]/div[2]/div/span/div/div/div/div[2]/div/div[1]/div[3]/div/div/div[1]/div[1]/div[1]')
#             )
#         )
#         campo_mensagem.send_keys(Keys.CONTROL, "a")
#         campo_mensagem.send_keys(Keys.BACKSPACE)
#         return campo_mensagem, foi
#
#     except (
#         NoSuchElementException, TimeoutException, StaleElementReferenceException,
#         WebDriverException, NoSuchFrameException, NoSuchWindowException,
#     ) as e:
#
#         print(e)
#         print("ERRO NO CAMPO MIDIA")
#         return None, not foi
#
#     except Exception as e:
#         print(e)
#         print("ERRO NO CAMPO MIDIA")
#         return None, not foi


"""TESTES """

# from conexao import cursor, conexao
#
# def ativar_enviou_dia_sql():
#     sql = "UPDATE clientes SET enviou_dia = True"
#     cursor.execute(sql)
#     conexao.commit()
#
#
# ativar_enviou_dia_sql()
#
# dados = contatos_faltantes_do_ultimo_disparo_sql(id_anterior=0)
#
# print(dados)
#
# if dados is None or len(dados)<1:
#     print("oi")