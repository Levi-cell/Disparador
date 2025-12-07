import subprocess
import socket
import time
import psutil
import win32gui
import win32con
import win32process
import requests
import json
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

def bring_chrome_to_front():
    hwnd = win32gui.FindWindow(None, "WhatsApp")
    if hwnd:
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)  # restaura se estiver minimizado
        time.sleep(0.2)
        win32gui.SetForegroundWindow(hwnd)  # traz para frente

def trazer_chrome_para_frente_e_acessar_aba(url_alvo):
    """
    1. Traz o Chrome (porta 9222) para frente
    2. Ativa a aba que contém a URL desejada
    """
    bring_chrome_to_front()
    PORT = 9222
    pid_do_chrome = None

    # 1️⃣ Encontrar processo do Chrome usando porta 9222
    for proc in psutil.process_iter(["pid", "name", "cmdline"]):
        try:
            cmd = proc.info["cmdline"]
            if cmd and any(f"--remote-debugging-port={PORT}" in arg for arg in cmd):
                pid_do_chrome = proc.info["pid"]
                break
        except:
            continue

    if not pid_do_chrome:
        print(f"...")
        return False

    # 2️⃣ Localizar janela correspondente ao PID
    janelas = []

    def callback(hwnd, lista):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            try:
                _, pid = win32process.GetWindowThreadProcessId(hwnd)
                if pid == pid_do_chrome:
                    lista.append(hwnd)
            except:
                pass

    win32gui.EnumWindows(callback, janelas)

    if not janelas:
        print("...")
        return False

    hwnd = janelas[0]

    # 3️⃣ Restaurar e trazer para frente
    try:
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        win32gui.SetForegroundWindow(hwnd)
        print("Janela movida para frente") # "✔ Chrome (9222) trazido para frente!"
    except Exception:
        print("...") # ❌ Erro ao trazer janela:
        return False

    # 4️⃣ Obter lista das abas abertas via DevTools
    try:
        tabs = requests.get(f"http://localhost:{PORT}/json").json()
    except Exception:
        print("...") # ❌ Não foi possível acessar /json do DevTools:
        return False

    # 5️⃣ Procurar aba com a URL desejada
    target_tab = None
    for tab in tabs:
        if "url" in tab and url_alvo.lower() in tab["url"].lower():
            target_tab = tab
            break

    if not target_tab:
        print("...") # ⚠ Nenhuma aba contém a URL informada.
        print("...") # ℹ Abas abertas:
        for t in tabs:
            print("...") # " -", t.get("url"
        return False

    # 6️⃣ Ativar / focar aba encontrada
    try:
        session_id = requests.get(
            f"http://localhost:{PORT}/json/new?{target_tab['url']}"
        ).json().get("id")

        requests.post(
            f"http://localhost:{PORT}/json/activate/{target_tab['id']}"
        )

        print(f"✔ Aba encontrada e ativada: {target_tab['url']}")
        return True

    except Exception:
        print("...") # ❌ Erro ao ativar aba:
        return False
