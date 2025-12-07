import time
from ProcedimentosInstalacaoDisparador.resetFunction import baixa_nova_base_de_dados

def resetar_disparador():
    print("⚠️ Não feche o sistema enquanto estiver baixando a nova base de dados...")
    print("------------------------")
    time.sleep(2)
    print("Essa opção irá baixar os contatos do seu número de telefone para o sistema...")
    print("------------------------")
    time.sleep(4)
    print("Caso já tenha acessado antes, o seu banco de dados será atualizado com os novos contatos...")
    print("------------------------")
    time.sleep(2)
    print("Os nomes alterados aqui serão preservados após a atualização...")
    print("------------------------")
    time.sleep(2)
    print("Os clientes indesejados que você salvou aqui continuarão na Blacklist após a atualização...")
    print("------------------------")
    time.sleep(2)
    print("⚠️ATENÇÃO⚠️ Caso mudou o número de alguém aqui, recomendamos que também mude no seu telefone...")
    print("Esse tipo de atualização não será salva após o reset...")
    print("------------------------")
    time.sleep(4)
    print("Se é sua primeira vez usando apenas ignore esse aviso e continue o procedimento")
    print("------------------------")
    time.sleep(2)


    # -------------------------
    # LINHA 21: while de validação
    # -------------------------
    while True:
        print("Tem certeza que deseja continuar com o Reset/Instalação de dados ? ")
        print("[1]  → Sim")
        print("[2]  → Não")
        escolha = input("Digite sua opção: ").strip()

        if escolha == "1":
            print("Iniciando Instalação/Reset... 🔄")
            time.sleep(2)
            baixa_nova_base_de_dados()
            return

        elif escolha == "2":
            print("Operação cancelada. 👍")
            return

        else:
            print("❌ Opção inválida. Por favor, escolha 1 ou 2.")
            time.sleep(2)
            print("------------------------------")
            continue



