from datetime import datetime
from src.SuportFunctions.FunRandom import numero_message

def menssangem_aleatoria_quinta():

    mensagem_sorteada = numero_message()

    dict_mensagens = {1: "ola", 2: "oi", 3: "é isso ai", 4: "Vamos que vamos",
                       5: "Ain", 6: "tmj",
                       7: "Ratinho", 8: "Rapaz", 9: "Meu pai amado", 10: "Vai teia"}

    for chave in dict_mensagens:
        if chave == mensagem_sorteada:
            return dict_mensagens[chave]

def menssangem_aleatoria_quarta():

    mensagem_sorteada = numero_message()

    dict_mensagens = {1: "ola", 2: "oi", 3: "é isso ai", 4: "Vamos que vamos",
                       5: "Ain", 6: "tmj",
                       7: "Ratinho", 8: "Rapaz", 9: "Meu pai amado", 10: "Vai teia"}

    for chave in dict_mensagens:
        if chave == mensagem_sorteada:
            return dict_mensagens[chave]

def menssangem_aleatoria_dias_frios():

    mensagem_sorteada = numero_message()


    dict_mensagens = {1: "ola", 2: "oi", 3: "é isso ai", 4: "Vamos que vamos",
                       5: "Ain", 6: "tmj",
                       7: "Ratinho", 8: "Rapaz", 9: "Meu pai amado", 10: "Vai teia"}

    for chave in dict_mensagens:
        if chave == mensagem_sorteada:
            return dict_mensagens[chave]

def mensagem_do_dia():
    # 0 = segunda, 1 = terça, 2 = quarta, 3 = quinta, 4 = sexta...
    dia_semana = datetime.now().weekday()

    if dia_semana == 2:   # 2 = quarta
        mensagem_quarta = menssangem_aleatoria_quarta()
        return mensagem_quarta

    elif dia_semana == 3: # 3 = quinta
        mensagem_quinta = menssangem_aleatoria_quinta()
        return mensagem_quinta

    else:
        mensagem_dia_frio = menssangem_aleatoria_dias_frios()
        return mensagem_dia_frio

