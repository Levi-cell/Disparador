import subprocess
import socket
import win32gui
import win32con
import win32process
import psutil
import win32api
import requests
import time
import threading
from functools import lru_cache
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PROFILE_PATH = r"C:\SeleniumProfile"
PORT = 9222


def porta_em_uso(porta: int) -> bool:
    """Retorna True se a porta já estiver sendo usada."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status = sock.connect_ex(("127.0.0.1", porta)) == 0
    sock.close()
    return status


def iniciar_chrome_remoto():
    """Inicia o Chrome com remote debugging caso não esteja aberto"""

    if porta_em_uso(PORT):
        print("⚠ Chrome já está aberto no modo remoto. Tudo certo.")
        print("---------------")
        return

    print("🚀 Iniciando Chrome em modo remoto...")
    print("---------------")

    comando = f'"{CHROME_PATH}" --remote-debugging-port={PORT} --user-data-dir="{PROFILE_PATH}"'

    subprocess.Popen(comando)

    # Aguarda o Chrome subir
    time.sleep(3)

    print("✔ Chrome remoto iniciado com sucesso!")
    print("---------------")


def fechar_chrome_remoto():
    """Finaliza qualquer processo que esteja usando a porta 9222."""
    print("Verificando e fechando se o chrome 9222 já está aberto...")
    # Verifica todas conexões abertas
    for conn in psutil.net_connections(kind="inet"):
        if conn.laddr.port == PORT:
            pid = conn.pid
            if pid:
                print(f"🛑 Processo usando porta {PORT} encontrado (PID {pid}). Encerrando...")

                try:
                    subprocess.run(["taskkill", "/F", "/PID", str(pid)], check=False)
                    print("✔ Processo encerrado com sucesso!")
                except Exception as e:
                    print(f"❌ Falha ao encerrar PID {pid}: {e}")
            else:
                print("⚠ A porta está ocupada, mas sem PID associado (pode ser sistema).")
            return

    print(f"⚠ Nenhum processo encontrado na porta {PORT}.")


import win32gui
import win32con
import win32process
import psutil
import requests
import time
from functools import lru_cache

# ==================== CACHE GLOBAL ====================
_CHROME_PID_CACHE = None
_CHROME_PID_CACHE_TIME = 0
_CACHE_TIMEOUT = 30  # segundos
_ULTIMA_JANELA_ENCONTRADA = None


# ==================== FUNÇÕES OTIMIZADAS ====================

@lru_cache(maxsize=1)
def encontrar_chrome_pid_cached(port=9222):
    """Encontra PID do Chrome com CACHE (evita buscar toda hora)"""
    global _CHROME_PID_CACHE, _CHROME_PID_CACHE_TIME

    if _CHROME_PID_CACHE and (time.time() - _CHROME_PID_CACHE_TIME) < _CACHE_TIMEOUT:
        return _CHROME_PID_CACHE

    for proc in psutil.process_iter(["pid", "name"]):
        try:
            name = proc.info["name"] or ""
            if "chrome" in name.lower():
                cmd = proc.info.get("cmdline", [])
                if cmd and any(f"--remote-debugging-port={port}" in arg for arg in cmd):
                    _CHROME_PID_CACHE = proc.info["pid"]
                    _CHROME_PID_CACHE_TIME = time.time()
                    return _CHROME_PID_CACHE
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    return None


def buscar_janela_por_pid_rapido(target_pid):
    """Busca janela por PID de forma otimizada"""
    global _ULTIMA_JANELA_ENCONTRADA

    if _ULTIMA_JANELA_ENCONTRADA:
        try:
            _, pid = win32process.GetWindowThreadProcessId(_ULTIMA_JANELA_ENCONTRADA)
            if pid == target_pid and win32gui.IsWindowVisible(_ULTIMA_JANELA_ENCONTRADA):
                return _ULTIMA_JANELA_ENCONTRADA
        except:
            pass

    hwnd_encontrado = [None]
    start_time = time.time()

    def callback(hwnd, pid_alvo):
        if time.time() - start_time > 1.0:
            return False

        if hwnd_encontrado[0]:
            return False

        if not win32gui.IsWindowVisible(hwnd):
            return True

        try:
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            if pid == pid_alvo:
                hwnd_encontrado[0] = hwnd
                return False
        except:
            pass
        return True

    win32gui.EnumWindows(lambda h, p: callback(h, target_pid), target_pid)

    if hwnd_encontrado[0]:
        _ULTIMA_JANELA_ENCONTRADA = hwnd_encontrado[0]

    return hwnd_encontrado[0]


def focar_janela_sem_falhar(hwnd):
    """Tenta focar janela MAS NÃO FALHA se não conseguir"""
    try:
        # Se já está em foco, ótimo
        if win32gui.GetForegroundWindow() == hwnd:
            return True

        # Restaura se minimizada
        if win32gui.IsIconic(hwnd):
            win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
            time.sleep(0.05)

        # Tenta focar (pode falhar por restrições do Windows)
        try:
            win32gui.SetForegroundWindow(hwnd)
            return True
        except:
            # Fallback: minimize/restore trick
            win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
            time.sleep(0.03)
            win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
            time.sleep(0.03)

            try:
                win32gui.SetForegroundWindow(hwnd)
                return True
            except:
                # Última tentativa: move para topo
                win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,
                                      win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
                win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0,
                                      win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
                return False  # Não conseguiu focar, mas não quebrou
    except Exception as e:
        print(f"⚠ Aviso foco: {str(e)[:50]}")
        return False  # Não conseguiu, mas NÃO FALHA


def trazer_chrome_para_frente_e_acessar_aba_otimizado(url_alvo, port=9222):
    """
    VERSÃO OTIMIZADA - NUNCA QUEBRA, sempre retorna True/False
    True = conseguiu focar E encontrar aba
    False = não conseguiu algo crítico
    """
    start_time = time.time()

    # 🔄 TENTATIVA 1: Busca rápida por título
    hwnd_rapido = None
    hwnd = win32gui.FindWindow(None, "WhatsApp")

    if not hwnd:
        for titulo in ["WhatsApp - Google Chrome", "WhatsApp Web", "whatsapp.com"]:
            hwnd = win32gui.FindWindow(None, titulo)
            if hwnd:
                break

    # Se encontrou por título, tenta focar E ativar aba
    if hwnd:
        focou = focar_janela_sem_falhar(hwnd)
        if focou:
            print("ℹ Chrome focado (método rápido)")

            # Tenta ativar aba mesmo com método rápido
            try:
                tabs = requests.get(f"http://localhost:{port}/json", timeout=1.0).json()
                for tab in tabs:
                    if "url" in tab and url_alvo.lower() in tab["url"].lower():
                        try:
                            requests.post(f"http://localhost:{port}/json/activate/{tab['id']}", timeout=0.5)
                            print(f"✔ Aba ativada (método rápido)")
                            return True
                        except:
                            print(f"ℹ Já na aba (método rápido)")
                            return True
            except:
                pass  # Se falhar, continua para método completo

    # 🔄 TENTATIVA 2: Método completo via PID + DevTools
    pid_chrome = encontrar_chrome_pid_cached(port)
    if not pid_chrome:
        print(f"...")
        # ❗ IMPORTANTE: Não retorna False! Tenta continuar mesmo sem Chrome
        return False

    # Busca janela do Chrome
    hwnd = buscar_janela_por_pid_rapido(pid_chrome)
    if not hwnd:
        # Fallback final: títulos alternativos
        hwnd = win32gui.FindWindow(None, "WhatsApp")
        if not hwnd:
            for titulo in ["WhatsApp - Google Chrome", "WhatsApp Web"]:
                hwnd = win32gui.FindWindow(None, titulo)
                if hwnd:
                    break

    if not hwnd:
        print("....")
        return False

    # Tenta focar (mas não é crítico se falhar)
    focou = focar_janela_sem_falhar(hwnd)
    if focou:
        print("✔ Chrome trazido para frente")
    else:
        print("(Windows bloqueou)")
        # ❗ CONTINUA MESMO SEM FOCO!

    # PARTE CRÍTICA: Tentar ativar a aba (DEVE tentar mesmo sem foco)
    try:
        tabs = requests.get(f"http://localhost:{port}/json", timeout=1.5).json()

        for tab in tabs:
            if "url" in tab and url_alvo.lower() in tab["url"].lower():
                try:
                    requests.post(f"http://localhost:{port}/json/activate/{tab['id']}", timeout=1)
                    print(f"✔ Aba ativada: {tab['url'][:50]}...")
                    return True
                except:
                    print(f"ℹ Já na aba: {tab['url'][:50]}...")
                    return True

        print(f"⚠ URL não encontrada: {url_alvo[:40]}...")
        return False

    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao acessar DevTools: {str(e)[:40]}...")
        return False
    except Exception as e:
        print(f"❌ Erro inesperado: {str(e)[:40]}...")
        return False


# ==================== FUNÇÕES DE COMPATIBILIDADE ====================

def trazer_chrome_para_frente_e_acessar_aba(url_alvo, port=9222):
    """
    WRAPPER PRINCIPAL - SEMPRE RETORNA True/False, NUNCA LANÇA EXCEÇÃO
    """
    try:
        return trazer_chrome_para_frente_e_acessar_aba_otimizado(url_alvo, port)
    except Exception as e:
        print(f"❌ ERRO CRÍTICO em trazer_chrome: {str(e)[:50]}")
        return False  # ❗ SEMPRE RETORNA False em caso de exceção


# def bring_chrome_to_front():
#     hwnd = win32gui.FindWindow(None, "WhatsApp")
#     if hwnd:
#         win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)  # restaura se estiver minimizado
#         time.sleep(0.25)
#         win32gui.SetForegroundWindow(hwnd)
#         return
#     return # traz para frente
#
# def trazer_chrome_para_frente_e_acessar_aba(url_alvo):
#     """
#     1. Traz o Chrome (porta 9222) para frente
#     2. Ativa a aba que contém a URL desejada
#     """
#     bring_chrome_to_front()
#     PORT = 9222
#     pid_do_chrome = None
#
#     # 1️⃣ Encontrar processo do Chrome usando porta 9222
#     for proc in psutil.process_iter(["pid", "name", "cmdline"]):
#         try:
#             cmd = proc.info["cmdline"]
#             if cmd and any(f"--remote-debugging-port={PORT}" in arg for arg in cmd):
#                 pid_do_chrome = proc.info["pid"]
#                 break
#         except:
#             continue
#
#     if not pid_do_chrome:
#         print(f"...")
#         return False
#
#     # 2️⃣ Localizar janela correspondente ao PID
#     janelas = []
#
#     def callback(hwnd, lista):
#         if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
#             try:
#                 _, pid = win32process.GetWindowThreadProcessId(hwnd)
#                 if pid == pid_do_chrome:
#                     lista.append(hwnd)
#             except:
#                 pass
#
#     win32gui.EnumWindows(callback, janelas)
#
#     if not janelas:
#         print("...")
#         return False
#
#     hwnd = janelas[0]
#
#     # 3️⃣ Restaurar e trazer para frente
#     try:
#         win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
#         win32gui.SetForegroundWindow(hwnd)
#         print("Janela movida para frente") # "✔ Chrome (9222) trazido para frente!"
#     except Exception:
#         print("...") # ❌ Erro ao trazer janela:
#         return False
#
#     # 4️⃣ Obter lista das abas abertas via DevTools
#     try:
#         tabs = requests.get(f"http://localhost:{PORT}/json").json()
#     except Exception:
#         print("...") # ❌ Não foi possível acessar /json do DevTools:
#         return False
#
#     # 5️⃣ Procurar aba com a URL desejada
#     target_tab = None
#     for tab in tabs:
#         if "url" in tab and url_alvo.lower() in tab["url"].lower():
#             target_tab = tab
#             break
#
#     if not target_tab:
#         print("...") # ⚠ Nenhuma aba contém a URL informada.
#         print("...") # ℹ Abas abertas:
#         for t in tabs:
#             print("...") # " -", t.get("url"
#         return False
#
#     # 6️⃣ Ativar / focar aba encontrada
#     try:
#         session_id = requests.get(
#             f"http://localhost:{PORT}/json/new?{target_tab['url']}"
#         ).json().get("id")
#
#         requests.post(
#             f"http://localhost:{PORT}/json/activate/{target_tab['id']}"
#         )
#
#         print(f"✔ Aba encontrada e ativada: {target_tab['url']}")
#         return True
#
#     except Exception:
#         print("...") # ❌ Erro ao ativar aba:
#         return False
#

