import time
from datetime import datetime
from tratandoErros import confirmar_acao
from processDisparo.SuportFunctions.FunRandom import numero_message

def pergunta_antecede():

    while True:
        print("Deseja enviar com ou sem aviso de antecedência?")
        print("[1]  → Sim")
        print("[2]  → Não")

        escolha = input("Digite sua opção: ").strip()
        time.sleep(2)
        print("---------")

        if escolha == "1":
            if confirmar_acao():
                return escolha
            else:
                continue

        elif escolha == "2":
            if confirmar_acao():
                return escolha
            else:
                continue

        else:
            print("❌ Opção inválida. Tente novamente.")
            time.sleep(2)
            print("------------------------------")
            continue

def nao_quer_disparo():

    message = "\n\nCaso não queira receber nossos avisos e promoções, é só avisar."

    return message

def message_antencede():

    message = ("\n\nFaça o seu pedido no nosso Link para garantir o seu Caldão! ás 18 horas iremos te notificar "
               "e preparar o seu pedido 😊")

    return message

def message_cardapio():

    message = ("\n\n- *Novidade!! agora você pode fazer seu pedido no nosso site com mais praticidade:*"
               "  https://sites.google.com/view/cardpiocaldonordestino/in%C3%ADcio")

    return message


def menssangem_aleatoria_quinta():

    mensagem_sorteada = numero_message()

    mensagem_quinta_1 = (
        "Caldolover de plantão! 😊\n"
        "Hoje é a nossa tradicional Quinta Nordestina, caldo sabor nordestino está com R$3 de desconto! Peça já o seu 🌵🔥!\n Exclusivo aqui no WhatsApp!"

    )

    mensagem_quinta_2 = (
        "Atenção querido(a) Caldolover! 😊\n"
        "A Quinta Nordestina chegou trazendo caldo sabor nordestino com tamanhos a partir de 6,99! Vem de caldinho 🌵🔥!\n Somente para pedidos feitos pelo WhatsApp!"

    )

    mensagem_quinta_3 = (
        "querido(a) Caldolover! 😊\n"
        "Hoje todos os caldos sabor nordestino estão com R$3 OFF! Não perca o seu caldinho 🌵🔥!\n Promoção exclusiva do WhatsApp!"

    )

    mensagem_quinta_4 = (
        "Atenção Caldolover! 😊👀\n"
        "A Quinta Nordestina tá daquele jeitinho: caldo sabor nordestino com R$3 OFF em qualquer tamanho! Garanta o seu 🌵🔥!\n Exclusivo pelo WhatsApp!"

    )

    mensagem_quinta_5 = (
        "Caldolover! 😊\n"
        "Hoje tem caldo sabor nordestino com tamanhos a partir de 6,99! Aproveite e peça o seu 🌵🔥!\n Válido somente no WhatsApp!"

    )

    mensagem_quinta_6 = (
        "Atenção querido(a) Caldolover! 😊\n"
        "Na Quinta Nordestina, todos os caldos sabor nordestino estão com R$3 OFF para esquentar a noite do nosso Caldolover! Faça já seu pedido 🌵🔥!\n Mas somente aqui no WhatsApp!"

    )

    mensagem_quinta_7 = (
        "Caldolover! 😊\n"
        "O caldo sabor nordestino está com R$3 OFF em todos os tamanhos! Garanta o seu caldinho 🌵🔥!\n Promoção exclusiva do WhatsApp!"

    )

    mensagem_quinta_8 = (
        "Atenção Caldolover! 😊👀\n"
        "Hoje a Quinta Nordestina traz caldo sabor nordestino a partir de 6,99 para nosso Caldolover aproveitar! Chame e peça já 🌵🔥!\n Exclusivo pelo WhatsApp!"

    )

    mensagem_quinta_9 = (
        "Caldolover querido(a)! 😊\n"
        "Temos caldo nordestino com R$3 OFF hoje! Não deixe para depois 🌵🔥!\n Oferta exclusiva do WhatsApp!"

    )

    mensagem_quinta_10 = (
        "Atenção querido(a) Caldolover! 😊\n"
        "A Quinta Nordestina chegou trazendo caldo nordestino com R$3 de desconto para alegrar sua noite! Peça agora mesmo 🌵🔥!\n Promoção válida somente aqui pelo WhatsApp!"

    )

    dict_mensagens = {
        0: mensagem_quinta_1,
        1: mensagem_quinta_2,
        2: mensagem_quinta_3,
        3: mensagem_quinta_4,
        4: mensagem_quinta_5,
        5: mensagem_quinta_6,
        6: mensagem_quinta_7,
        7: mensagem_quinta_8,
        8: mensagem_quinta_9,
        9: mensagem_quinta_10
    }

    for chave in dict_mensagens:
        if chave == mensagem_sorteada:
            return dict_mensagens[chave]

def menssangem_aleatoria_quarta():

    mensagem_sorteada = numero_message()

    mensagem1 = (
        "Caldolover de plantão, atenção que hoje tá imperdível! 😊👀\n"
        "Todos os caldos de sururu estão com R$3 OFF! Peça já o seu 🌵🔥!\n Exclusivamente para pedidos no WhatsApp!"

    )

    mensagem2 = (
        "Caldolover querido(a)! 😊\n"
        "Hoje é dia de aproveitar o caldo de sururu com tamanhos a partir de R$8,99! Vem de caldinho 🌵🔥!\n Somente pelo WhatsApp!"

    )

    mensagem3 = (
        "Atenção, Caldolover! 😊👀\n"
        "O sururu tá liberado com R$3 OFF em todos os tamanhos! Não perca seu caldinho 🌵🔥!\n Promoção exclusiva no WhatsApp!"

    )

    mensagem4 = (
        "Caldolover! 😊\n"
        "A quarta do sururuvis está garantida com R$3 OFF nos caldos de sururu! Garanta o seu 🌵🔥!\n Apenas aqui no WhatsApp!"

    )

    mensagem5 = (
        "Atenção Caldolover! 😊👀\n"
        "Hoje tem caldo de sururu com tamanhos a partir de R$8,99! Peça já 🌵🔥!\n Exclusivo para WhatsApp!"

    )

    mensagem6 = (
        "Caldolover! 😊\n"
        "O caldo de sururu está com R$3 OFF em todos os tamanhos! Aproveite agora 🌵🔥!\n Promoção exclusiva do WhatsApp!"

    )

    mensagem7 = (
        "Atenção Caldolover! 😊👀\n"
        "Caldo de sururu com tamanhos a partir de R$8,99! Garanta o seu 🌵🔥!\n Exclusivo para WhatsApp!"

    )

    mensagem8 = (
        "Caldolover querido(a)! 😊\n"
        "Hoje tem sururu com tamanhos a partir de R$8,99! Não deixe para depois 🌵🔥!\n Somente válido no WhatsApp!"

    )

    mensagem9 = (
        "Atenção Caldolover! 😊👀\n"
        "O caldo de sururu está com R$3 OFF em todos os tamanhos para esquentar a noite do nosso Caldolover! Peça já o seu 🌵🔥!\n Disponível somente no WhatsApp"

    )

    mensagem10 = (
        "Caldolover! 😊\n"
        "Hoje tem Caldo de sururu com tamanhos a partir de R$8,99! Vem garantir o seu 🌵🔥!\n Disponível somente no WhatsApp"

    )

    dict_mensagens = {
        0: mensagem1,
        1: mensagem2,
        2: mensagem3,
        3: mensagem4,
        4: mensagem5,
        5: mensagem6,
        6: mensagem7,
        7: mensagem8,
        8: mensagem9,
        9: mensagem10
    }

    for chave in dict_mensagens:
        if chave == mensagem_sorteada:
            return dict_mensagens[chave]

def menssangem_aleatoria_dias_frios():

    mensagem_sorteada = numero_message()

    mensagem_1 = (
        "Friozinho no fim de semana…\n"
        "O que falta para nosso CaldoLover fechar a noite com chave de ouro? 🤔🌵 Um caldinho quentinho! 😋🔥"

    )

    mensagem_2 = (
        "Aquele friozinho no fim de semana chegou…\n"
        "E para o nosso CaldoLover fechar a noite com perfeição só falta um caldinho delicioso! 🤗🔥"

    )

    mensagem_3 = (
        "Friozinho gostoso no fim de semana…\n"
        "O que falta para nosso CaldoLover fechar a noite com chave de ouro? 🤔🌵 Um caldinho bem quente! 😍🔥"

    )

    mensagem_4 = (
        "Fim de semana geladinho…\n"
        "E nosso CaldoLover já sabe o que falta pra completar, né? 😏🌵 Um caldinho quentinho irresistível! 🔥"

    )

    mensagem_5 = (
        "Friozinho no fim de semana pedindo aquele aconchego…\n"
        "O que falta para nosso CaldoLover fechar a noite com chave de ouro? 🤔🌵 Um caldinho quentinho e delicioso! 🤗🔥"

    )

    mensagem_6 = (
        "Chegou o friozinho no fim de semana…\n"
        "E o que falta para nosso CaldoLover fechar bem a noite? 🤔 Aquele caldinho quentinho que abraça! 🌵🔥"

    )

    mensagem_7 = (
        "Friozinho do fim de semana batendo…\n"
        "E só falta uma coisa para nosso CaldoLover fechar a noite com chave de ouro 🌵: um caldinho perfeito pra aquecer! 😌🔥"

    )

    mensagem_8 = (
        "Com esse friozinho no fim de semana…\n"
        "O que falta para nosso CaldoLover completar a noite? 🤔🌵 Um caldinho saboroso! 🥰🔥"

    )

    mensagem_9 = (
        "Fim de semana geladinho chegando…\n"
        "O que falta para nosso CaldoLover fechar a noite com chave de ouro? 🤔🌵 Um caldinho quentinho daqueles! 😋🔥"

    )

    mensagem_10 = (
        "Friozinho no fim de semana… perfeito pra quê? 🤔🌵\n"
        "Para nosso CaldoLover fechar a noite com chave de ouro com um caldinho delicioso! 😋🔥"

    )

    # Dicionário com todas as mensagens
    dict_mensagens = {
        0: mensagem_1,
        1: mensagem_2,
        2: mensagem_3,
        3: mensagem_4,
        4: mensagem_5,
        5: mensagem_6,
        6: mensagem_7,
        7: mensagem_8,
        8: mensagem_9,
        9: mensagem_10
    }

    for chave in dict_mensagens:
        if chave == mensagem_sorteada:
            return dict_mensagens[chave]

def mensagem_do_dia():
    # 0 = segunda, 1 = terça, 2 = quarta, 3 = quinta, 4 = sexta...
    dia_semana = datetime.now().weekday()

    horario = datetime.now().hour

    mensagem_cardapio = message_cardapio()
    mensagem_nao_disparo = nao_quer_disparo()

    if dia_semana == 2:
        # 2 = quarta
        mensagem_quarta = menssangem_aleatoria_quarta()

        if horario < 18:

            messagem_antecendencia = message_antencede()

            mensagem_quarta = mensagem_quarta + messagem_antecendencia

        mensagem_quarta = mensagem_quarta + mensagem_cardapio + mensagem_nao_disparo

        return mensagem_quarta

    elif dia_semana == 3: # 3 = quinta

        mensagem_quinta = menssangem_aleatoria_quinta()

        if horario < 18:

            messagem_antecendencia = message_antencede()

            mensagem_quinta = mensagem_quinta + messagem_antecendencia

        mensagem_quinta = mensagem_quinta + mensagem_cardapio + mensagem_nao_disparo

        return mensagem_quinta

    else:

        mensagem_dia_frio = menssangem_fim_de_semana()

        if horario < 18:

            messagem_antecendencia = message_antencede()

            mensagem_dia_frio = mensagem_dia_frio + messagem_antecendencia

        mensagem_dia_frio = mensagem_dia_frio + mensagem_cardapio + mensagem_nao_disparo

        return mensagem_dia_frio

def aviso_ausencia():

    mensagem = (
        "🌵 AUSENCIA, CaldoLover! 🌵\n"
        "Tem novidade chegando na nossa agenda do Caldão Nordestino!\n"
        "\n"
        "A partir de hoje, estaremos abrindo de terça a sábado, sempre prontos para servir "
        "aquele caldinho gostoso que abraça a alma e aquece o coração. 💛🔥\n"
        "\n"
        "Terça estaremos te esperando!\n"
    )

    return mensagem

def mensagem_atualizacao():

    mensagem = (
        " CaldoLover! 🌵\n"
        "Já estamos abertos e seguindo a agenda nova 😊!\n"
        "\n"
        "Lembrando que estaremos abrindo das terças aos sábados, sempre prontos para servir "
        "aquele caldinho gostoso que abraça a alma e aquece o coração! 💛🔥\n"

    )

    return mensagem

    # 0 = segunda, 1 = terça, 2 = quarta, 3 = quinta, 4 = sexta...


def escolhe_sua_mensagem():
    while True:
        print("Qual tipo de mensagem deseja enviar ?")
        print("[1]  → Mensagem promocional do dia")
        print("[2]  → Mensagem de ausência")
        print("[3]  → Mensagem informando mudança")

        escolha = input("Digite sua opção: ").strip()
        time.sleep(2)
        print("---------")

        if escolha == "1":
            if confirmar_acao():
                return escolha
            else:
                continue

        elif escolha == "2":
            if confirmar_acao():
                return escolha
            else:
                continue

        elif escolha == "3":
            if confirmar_acao():
                return escolha
            else:
                continue

        else:
            print("❌ Opção inválida. Tente novamente.")
            time.sleep(2)
            print("------------------------------")
            continue

def menssangem_fim_de_semana():

    mensagem_sorteada = numero_message()

    mensagem_1 = (
        "Bora renovar as forças nesse fim de semana com um Caldão!🌵💪"

    )

    mensagem_2 = (
        "Fim de semana chegando… que tal dar aquele up na energia com um Caldão!? 🌵⚡"

    )

    mensagem_3 = (
        "Hora de recarregar as energias do fim de semana com aquele caldinho gostoso!… 🌵⚡"

    )

    mensagem_4 = (
        "Fim de semana perfeito para renovar o ânimo com um Caldão daqueles!🌵🔥"

    )

    mensagem_5 = (
        "Aquele momento de repor as energias do fim de semana com um caldo quentinho chegou! 🌵😌"

    )

    mensagem_6 = (
        "Hora de preparar bem o corpo para amanhã com um Caldão revigorante! 🌵🚀"

    )

    mensagem_7 = (
        "Finalzinho de dia pedindo uma pausa para um Caldinho… 🌵😌"

    )

    mensagem_8 = (
        "Fim de semana bom é aquele em que a gente repõe as energias com um Caldão daqueles! 🌵😍"

    )

    mensagem_9 = (
        "Que tal dar aquele gás para encerrar o dia bem com um Caldão!? 🌵💪"
    )

    mensagem_10 = (
        "Que tal dar aquele gás para encerrar o dia bem com um Caldo revigorante!? 🌵💪"

    )

    # Dicionário com todas as mensagens
    dict_mensagens = {
        0: mensagem_1,
        1: mensagem_2,
        2: mensagem_3,
        3: mensagem_4,
        4: mensagem_5,
        5: mensagem_6,
        6: mensagem_7,
        7: mensagem_8,
        8: mensagem_9,
        9: mensagem_10
    }

    for chave in dict_mensagens:
        if chave == mensagem_sorteada:
            return dict_mensagens[chave]


def mensagem_simples():

    message = "O tempo esfriou, e o caldão nordestino já está quentinho esperando por você 💛🔥!"

    return message

