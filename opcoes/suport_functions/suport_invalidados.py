from processDisparo.SQLfunctions.UpdateFunctions import atualizar_telefone_cliente_sql, ativar_disparo_por_id_sql
from processDisparo.SQLfunctions.ConsultFunctions import consulta_cliente_sql
from opcoes.adicionar_lead import tratar_telefone_ja_existente
from tratandoErros import trata_telefone
import time

def define_status_disparo(id_cliente):
    """
    Pergunta ao usuário se deseja ativar o disparo_status (promoções)
    para este cliente. Agora usa 1 = sim / 2 = não.
    """

    print("\nDeseja re-ativar o envio de promoções para este cliente?")
    print("[1]  → Sim")
    print("[2]  → Não")
    print("⚠️ Qualquer tecla também serve como não.")
    escolha = input("Digite sua opção: ").strip()

    if escolha in ("1", "s", "ss", "sim"):
        ativar_disparo_por_id_sql(id_cliente)
        print("✔️ Disparo ativado com sucesso!")
        print("----------")
        time.sleep(2)
        return True

    print("🔕 Disparo não ativado. Mantendo como está.")
    print("----------")
    time.sleep(2)
    return False

def captura_novo_telefone():
    while True:
        novo_numero = input("Digite o novo telefone: ").strip()
        novo_numero = trata_telefone(novo_numero)

        cliente_existente = consulta_cliente_sql(novo_numero)

        if cliente_existente is not None:
            tentar_novamente = tratar_telefone_ja_existente()

            if tentar_novamente:
                continue
            else:
                time.sleep(1)
                print("↩ Retornando sem alterar o telefone...")
                print("----------")
                time.sleep(2)
                return None

        print("✔ Número válido e liberado!")
        print("----------")
        time.sleep(2)
        return novo_numero

def confirma_alteracao_telefone(novo_numero, id_cliente):

    print(f"\nTem certeza que deseja alterar para {novo_numero}?")
    print("[1]  → Sim")
    print("[2]  → Não")
    print("⚠️ Qualquer tecla também serve como não.")
    confirmacao = input("Digite sua opção: ").strip()

    if confirmacao in ("1", "s", "ss", "sim"):
        atualizar_telefone_cliente_sql(novo_numero, id_cliente)
        print("✔ Telefone alterado com sucesso!")
        print("----------")
        time.sleep(2)
        return True

    print("❌ Alteração do telefone cancelada.")
    print("----------")
    time.sleep(2)
    return False

