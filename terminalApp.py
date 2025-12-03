import tkinter as tk
import threading
import queue
import sys
import time
import os

from menuInterativo import menu_interativo


# -------------------------------------------------------
# TERMINAL TKINTER ESTILIZADO (One Dark Theme)
# -------------------------------------------------------
class TkTerminal:
    def __init__(self, root):
        self.root = root
        self.root.title("Terminal Simulado – Disparador de Promoções")
        self.root.geometry("1150x700")  # JANELA MAIOR
        self.root.configure(bg="#1e1e1e")

        # -------- GRADIENTE LEVE NO FUNDO --------
        self.bg_frame = tk.Frame(root, bg="#1e1e1e")
        self.bg_frame.place(relwidth=1, relheight=1)

        # -------- BARRA SUPERIOR (estilo PyCharm) --------
        top_bar = tk.Frame(root, bg="#242424", height=32)
        top_bar.pack(fill="x", side="top")

        title_label = tk.Label(
            top_bar,
            text="●   ●   ●     Terminal – One Dark Theme",
            fg="#9da5b4",
            bg="#242424",
            font=("Consolas", 12, "bold")
        )
        title_label.pack(side="left", padx=12)

        # -------- ÁREA DE TEXTO --------
        self.text = tk.Text(
            root,
            bg="#1e1e1e",
            fg="#dcdfe4",
            font=("Cascadia Mono", 14),  # FONTE MAIS NÍTIDA
            insertbackground="#ffffff",
            border=0,
            padx=16,
            pady=16,
            spacing1=4,      # espaçamento entre linhas
            spacing2=2,
            spacing3=4
        )
        self.text.pack(fill="both", expand=True)

        # -------- SCROLLBAR MODERNA --------
        scrollbar = tk.Scrollbar(
            self.text,
            command=self.text.yview,
            troughcolor="#1e1e1e",
            bg="#3a3f44",
            activebackground="#4e555b",
            highlightcolor="#1e1e1e",
        )
        self.text.configure(yscrollcommand=scrollbar.set)
        scrollbar.place(relx=1, rely=0, relheight=1, anchor="ne")

        # -------- CORES DAS TAGS --------
        self.text.tag_config("info", foreground="#61afef")     # Azul OneDark
        self.text.tag_config("warning", foreground="#e5c07b")  # Amarelo OneDark
        self.text.tag_config("error", foreground="#e06c75")    # Vermelho
        self.text.tag_config("success", foreground="#98c379")  # Verde OneDark
        self.text.tag_config("emoji", foreground="#dcdfe4")    # Cor padrão clara

        # -------- MENSAGEM INICIAL --------
        self.text.insert("end", "🚀 Gerenciador de disparo iniciado...\n", "success")
        self.text.see("end")

        self.input_queue = queue.Queue()

        # Redireciona saída
        sys.stdout = self
        sys.stderr = self
        sys.stdin = self

    # ---------------- PRINT ----------------
    def write(self, msg):
        tag = "info"

        if "⚠" in msg or "Atenção" in msg:
            tag = "warning"
        elif "❌" in msg or "Erro" in msg:
            tag = "error"
        elif "✔" in msg or "Sucesso" in msg:
            tag = "success"
        elif "📢" in msg or "🚀" in msg or "🔍" in msg or "➕" in msg:
            tag = "emoji"

        self.text.insert("end", msg, tag)
        self.text.see("end")

    def flush(self):
        pass

    # ---------------- INPUT ----------------
    def readline(self):
        self.current_input = tk.StringVar()

        entry = tk.Entry(
            self.text,
            textvariable=self.current_input,
            bg="#2b2b2b",
            fg="#dcdfe4",
            font=("Cascadia Mono", 14),
            insertbackground="#ffffff",
            relief="flat",
            width=50,
        )

        self.text.window_create("end", window=entry)
        self.text.insert("end", "\n")
        entry.focus()

        # pressionar ENTER
        def on_enter(event=None):
            try:
                val = self.current_input.get()
                if val == "" or val is None:
                    self.input_queue.put("\n")
                else:
                    self.input_queue.put(val + "\n")
            except Exception:
                self.input_queue.put("\n")

        entry.bind("<Return>", on_enter)
        entry.bind("<Escape>", lambda e: self.input_queue.put("\n"))

        try:
            value = self.input_queue.get()
        except Exception:
            value = "\n"

        try:
            entry.destroy()
        except:
            pass

        display_value = value.rstrip("\n")
        self.text.insert("end", display_value + "\n", "info")
        self.text.see("end")

        return value


# -------------------------------------------------------
# THREAD QUE EXECUTA O MENU
# -------------------------------------------------------
def thread_menu():
    try:
        menu_interativo()
    except Exception as e:
        print(f"\n❌ Erro durante execução: {e}\n")
        time.sleep(3)


def iniciar_terminal():
    root = tk.Tk()
    terminal = TkTerminal(root)
    threading.Thread(target=thread_menu, daemon=True).start()
    root.mainloop()


if __name__ == "__main__":
    iniciar_terminal()
