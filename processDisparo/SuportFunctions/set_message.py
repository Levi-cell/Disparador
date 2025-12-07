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


def message_antencede():

    message = "\n\nA partir dás 18 estamos aí! 😊"

    return message


def menssangem_aleatoria_quinta():

    mensagem_sorteada = numero_message()

    mensagem_quinta_1 = (
        "Boa noite Caldolover de plantão! 😊\n\n"
        "Hoje é a nossa tradicional Quinta Nordestina, caldo sabor nordestino está com R$3 de desconto! Peça já o seu 🌵🔥 exclusivo aqui no WhatsApp!\n"
        "(Se quiser pausar o recebimento das promoções, é só informar.)"
    )

    mensagem_quinta_2 = (
        "Atenção querido(a) Caldolover! 😊\n\n"
        "A Quinta Nordestina chegou trazendo caldo sabor nordestino com tamanhos a partir de 6,99! Vem de caldinho 🌵🔥 — somente para pedidos feitos pelo WhatsApp!\n"
        "(Caso não deseje mais receber nossas ofertas, basta avisar.)"
    )

    mensagem_quinta_3 = (
        "Boa noite querido(a) Caldolover! 😊\n\n"
        "Hoje todos os caldos sabor nordestino estão com R$3 OFF! Não perca o seu caldinho 🌵🔥 promoção exclusiva do WhatsApp!\n"
        "(Se preferir parar de receber nossas mensagens, é só pedir.)"
    )

    mensagem_quinta_4 = (
        "Atenção Caldolover! 😊👀\n\n"
        "A Quinta Nordestina tá daquele jeitinho: caldo sabor nordestino com R$3 OFF em qualquer tamanho! Garanta o seu 🌵🔥 exclusivo pelo WhatsApp!\n"
        "(Se não quiser continuar recebendo promoções, é só avisar.)"
    )

    mensagem_quinta_5 = (
        "Boa noite Caldolover! 😊\n\n"
        "Hoje tem caldo sabor nordestino com tamanhos a partir de 6,99! Aproveite e peça o seu 🌵🔥 válido somente no WhatsApp!\n"
        "(Caso não queira mais receber novidades, basta informar.)"
    )

    mensagem_quinta_6 = (
        "Atenção querido(a) Caldolover! 😊\n\n"
        "Na Quinta Nordestina, todos os caldos sabor nordestino estão com R$3 OFF para esquentar a noite do nosso Caldolover! Faça já seu pedido 🌵🔥 — mas somente aqui no WhatsApp!\n"
        "(Se desejar sair da lista, é só nos comunicar.)"
    )

    mensagem_quinta_7 = (
        "Boa noite Caldolover! 😊\n\n"
        "O caldo sabor nordestino está com R$3 OFF em todos os tamanhos! Garanta o seu caldinho 🌵🔥 Promoção exclusiva do WhatsApp!\n"
        "(Se não quiser mais receber nossas promoções, pode avisar sem problema.)"
    )

    mensagem_quinta_8 = (
        "Atenção Caldolover! 😊👀\n\n"
        "Hoje a Quinta Nordestina traz caldo sabor nordestino a partir de 6,99 para nosso Caldolover aproveitar! Chame e peça já 🌵🔥 exclusivo pelo WhatsApp!\n"
        "(Caso queira encerrar o recebimento das ofertas, basta avisar.)"
    )

    mensagem_quinta_9 = (
        "Boa noite Caldolover querido(a)! 😊\n\n"
        "Temos caldo nordestino com R$3 OFF hoje! Não deixe para depois 🌵🔥 oferta exclusiva do WhatsApp!\n"
        "(Se preferir não receber mensagens promocionais, é só informar.)"
    )

    mensagem_quinta_10 = (
        "Atenção querido(a) Caldolover! 😊\n\n"
        "A Quinta Nordestina chegou trazendo caldo nordestino com R$3 de desconto para alegrar sua noite! Peça agora mesmo 🌵🔥 promoção válida somente aqui pelo WhatsApp!\n"
        "(Se quiser parar de receber as promoções, é só mandar mensagem.)"
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
        "Caldolover de plantão, atenção que hoje tá imperdível! 😊👀\n\n"
        "Todos os caldos de sururu estão com R$3 OFF! Peça já o seu 🌵🔥 exclusivamente para pedidos no WhatsApp!\n"
        "(Caso prefira não receber nossas promoções, é só pedir.)"
    )

    mensagem2 = (
        "Boa noite, Caldolover querido(a)! 😊\n\n"
        "Hoje é dia de aproveitar o caldo de sururu com tamanhos a partir de R$8,99! Vem de caldinho 🌵🔥 somente pelo WhatsApp!\n"
        "(Se desejar parar de receber nossas ofertas, é só informar.)"
    )

    mensagem3 = (
        "Atenção, Caldolover! 😊👀\n\n"
        "O sururu tá liberado com R$3 OFF em todos os tamanhos! Não perca seu caldinho 🌵🔥 — promoção exclusiva no WhatsApp!\n"
        "(Se não quiser receber essas mensagens, é só avisar.)"
    )

    mensagem4 = (
        "Boa noite Caldolover! 😊\n\n"
        "A quarta do sururuvis está garantida com R$3 OFF nos caldos de sururu! Garanta o seu 🌵🔥 apenas aqui no WhatsApp!\n"
        "(Caso deseje sair da lista de promoções, é só pedir.)"
    )

    mensagem5 = (
        "Atenção Caldolover! 😊👀\n\n"
        "Hoje tem caldo de sururu com tamanhos a partir de R$8,99! Peça já 🌵🔥 exclusivo para WhatsApp!\n"
        "(Se preferir não receber mais mensagens, é só avisar.)"
    )

    mensagem6 = (
        "Boa noite Caldolover! 😊\n\n"
        "O caldo de sururu está com R$3 OFF em todos os tamanhos! Aproveite agora 🌵🔥 — promoção exclusiva do WhatsApp!\n"
        "(Se quiser parar de receber promoções, só nos sinalizar.)"
    )

    mensagem7 = (
        "Atenção Caldolover! 😊👀\n\n"
        "Caldo de sururu com tamanhos a partir de R$8,99! Garanta o seu 🌵🔥 exclusivo para WhatsApp!\n"
        "(Se não quiser mais receber ofertas, é só informar.)"
    )

    mensagem8 = (
        "Boa noite, Caldolover querido(a)! 😊\n\n"
        "Hoje tem sururu com tamanhos a partir de R$8,99! Não deixe para depois 🌵🔥 só no WhatsApp!\n"
        "(Se desejar sair da lista de promoções, basta avisar.)"
    )

    mensagem9 = (
        "Atenção Caldolover! 😊👀\n\n"
        "O caldo de sururu está com R$3 OFF em todos os tamanhos para esquentar a noite do nosso Caldolover! Peça já o seu 🌵🔥 disponível somente no WhatsApp\n"
        "(Caso não queira mais receber promoções, só avisar.)"
    )

    mensagem10 = (
        "Boa noite Caldolover! 😊\n\n"
        "Hoje tem Caldo de sururu com tamanhos a partir de R$8,99! Vem garantir o seu 🌵🔥 disponível somente no WhatsApp\n"
        "(Se preferir parar de receber nossas mensagens, é só avisar.)"
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

# def menssangem_aleatoria_dias_frios():
#
#     mensagem_sorteada = numero_message()
#
#     mensagem_1 = (
#         "Friozinho no fim de semana…\n\n"
#         "O que falta para nosso CaldoLover fechar a noite com chave de ouro? 🤔🌵 Um caldinho quentinho! 😋🔥\n"
#         "(Caso não queira receber nossos avisos e lembretes, é só avisar.)"
#     )
#
#     mensagem_2 = (
#         "Aquele friozinho no fim de semana chegou…\n\n"
#         "E para o nosso CaldoLover fechar a noite com perfeição só falta um caldinho delicioso! 🤗🔥\n"
#         "(Se preferir não receber nossos lembretes e avisos, basta nos informar.)"
#     )
#
#     mensagem_3 = (
#         "Friozinho gostoso no fim de semana…\n\n"
#         "O que falta para nosso CaldoLover fechar a noite com chave de ouro? 🤔🌵 Um caldinho bem quente! 😍🔥\n"
#         "(Se não quiser mais receber nossos avisos e lembretes, só avisar.)"
#     )
#
#     mensagem_4 = (
#         "Fim de semana geladinho…\n\n"
#         "E nosso CaldoLover já sabe o que falta pra completar, né? 😏🌵 Um caldinho quentinho irresistível! 🔥\n"
#         "(Caso deseje parar de receber nossos lembretes, é só avisar.)"
#     )
#
#     mensagem_5 = (
#         "Friozinho no fim de semana pedindo aquele aconchego…\n\n"
#         "O que falta para nosso CaldoLover fechar a noite com chave de ouro? 🤔🌵 Um caldinho quentinho e delicioso! 🤗🔥\n"
#         "(Se não quiser continuar recebendo nossos avisos, é só nos dizer.)"
#     )
#
#     mensagem_6 = (
#         "Chegou o friozinho no fim de semana…\n\n"
#         "E o que falta para nosso CaldoLover fechar bem a noite? 🤔 Aquele caldinho quentinho que abraça! 🌵🔥\n"
#         "(Caso queira parar de receber nossos lembretes, avise.)"
#     )
#
#     mensagem_7 = (
#         "Friozinho do fim de semana batendo…\n\n"
#         "E só falta uma coisa para nosso CaldoLover fechar a noite com chave de ouro 🌵: um caldinho perfeito pra aquecer! 😌🔥\n"
#         "(Se preferir não receber mais lembretes, basta avisar.)"
#     )
#
#     mensagem_8 = (
#         "Com esse friozinho no fim de semana…\n\n"
#         "O que falta para nosso CaldoLover completar a noite? 🤔🌵 Um caldinho saboroso! 🥰🔥\n"
#         "(Caso não queira mais receber nossos lembretes, apenas nos avise.)"
#     )
#
#     mensagem_9 = (
#         "Fim de semana geladinho chegando…\n\n"
#         "O que falta para nosso CaldoLover fechar a noite com chave de ouro? 🤔🌵 Um caldinho quentinho daqueles! 😋🔥\n"
#         "(Se não quiser receber nossos avisos e lembretes, é só informar.)"
#     )
#
#     mensagem_10 = (
#         "Friozinho no fim de semana… perfeito pra quê? 🤔🌵\n\n"
#         "Para nosso CaldoLover fechar a noite com chave de ouro com um caldinho delicioso! 😋🔥\n"
#         "(Caso não queira mais receber lembretes e avisos, avise por aqui.)"
#     )
#
#     # Dicionário com todas as mensagens
#     dict_mensagens = {
#         0: mensagem_1,
#         1: mensagem_2,
#         2: mensagem_3,
#         3: mensagem_4,
#         4: mensagem_5,
#         5: mensagem_6,
#         6: mensagem_7,
#         7: mensagem_8,
#         8: mensagem_9,
#         9: mensagem_10
#     }
#
#     for chave in dict_mensagens:
#         if chave == mensagem_sorteada:
#             return dict_mensagens[chave]

def mensagem_do_dia():
    # 0 = segunda, 1 = terça, 2 = quarta, 3 = quinta, 4 = sexta...
    dia_semana = datetime.now().weekday()
    horario = datetime.now().hour

    if dia_semana == 2:   # 2 = quarta
        mensagem_quarta = menssangem_aleatoria_quarta()
        if horario < 18:
            ausencia = message_antencede()
            mensagem_quarta = mensagem_quarta + ausencia
        return mensagem_quarta

    elif dia_semana == 3: # 3 = quinta
        mensagem_quinta = menssangem_aleatoria_quinta()
        if horario < 18:
            ausencia = message_antencede()
            mensagem_quinta = mensagem_quinta + ausencia
        return mensagem_quinta

    else:
        mensagem_dia_frio = mensagem_simples()
        if horario < 18:
            ausencia = message_antencede()
            mensagem_dia_frio = mensagem_dia_frio + ausencia
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

def menssangem_aleatoria_dias_frios():

    mensagem_sorteada = numero_message()

    mensagem_1 = (
        "Bora renovar as forças nesse fim de semana… 💪✨\n\n"
        "E nada ajuda mais nessa renovação do que um caldinho acolhedor para completar o dia! 😋🔥\n"
        "(Caso não queira receber nossos avisos e lembretes, é só avisar.)"
    )

    mensagem_2 = (
        "Fim de semana chegando… que tal dar aquele up na energia? 💥😌\n\n"
        "E para acompanhar esse momento, um caldinho aconchegante cai perfeitamente! 🤗🔥\n"
        "(Se preferir não receber nossos lembretes e avisos, basta nos informar.)"
    )

    mensagem_3 = (
        "Hora de recarregar as energias do fim de semana… ✨⚡\n\n"
        "E nada ajuda mais nessa recarga do que um caldinho revigorante pra completar o clima! 😍🔥\n"
        "(Se não quiser mais receber nossos avisos e lembretes, só avisar.)"
    )

    mensagem_4 = (
        "Fim de semana perfeito para renovar o ânimo… ✨🙌\n\n"
        "E para embalar essa renovação, um caldinho acolhedor irresistível é a pedida certa! 😏🌵🔥\n"
        "(Caso deseje parar de receber nossos lembretes, é só avisar.)"
    )

    mensagem_5 = (
        "Aquele momento de repor as energias do fim de semana… 😌💛\n\n"
        "E para deixar tudo ainda melhor, um caldinho aconchegante sempre cai perfeito! 🤗🌵🔥\n"
        "(Se não quiser continuar recebendo nossos avisos, é só nos dizer.)"
    )

    mensagem_6 = (
        "Hora de preparar bem o corpo para amanhã… 🚀✨\n\n"
        "E para acompanhar esse cuidado, um caldinho acolhedor que abraça é ideal! 🌵🔥\n"
        "(Caso queira parar de receber nossos lembretes, avise.)"
    )

    mensagem_7 = (
        "Finalzinho de dia pedindo uma pausa… 😌✨\n\n"
        "E para reforçar essa pausa, um caldinho revigorante dá aquele gás gostoso! 😌🌵🔥\n"
        "(Se preferir não receber mais lembretes, basta avisar.)"
    )

    mensagem_8 = (
        "Fim de semana bom é aquele em que a gente repõe as energias… ✨😍\n\n"
        "E nada combina mais com esse momento do que um caldinho aconchegante para fechar o dia! 🥰🌵🔥\n"
        "(Caso não queira mais receber nossos lembretes, apenas nos avise.)"
    )

    mensagem_9 = (
        "Preparando o corpo e a mente para amanhã… 🌟🙌\n\n"
        "E para ajudar nessa preparação, um caldinho acolhedor faz toda a diferença! 😋🌵🔥\n"
        "(Se não quiser receber nossos avisos e lembretes, é só informar.)"
    )

    mensagem_10 = (
        "Que tal dar aquele gás para encerrar o dia bem? ✨💪\n\n"
        "E para fechar com chave de ouro, um caldinho revigorante é perfeito para o momento! 😋🌵🔥\n"
        "(Caso não queira mais receber lembretes e avisos, avise por aqui.)"
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

    message = ("O tempo esfriou, e o caldão nordestino já está quentinho esperando por você 😊💛🔥!\n\n"
               "Aproveita por que depois de hoje só terça-feira 👀")

    return message

