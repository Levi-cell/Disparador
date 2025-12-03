import subprocess
import socket
import time

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



