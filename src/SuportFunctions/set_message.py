from datetime import datetime
from src.SuportFunctions.FunRandom import numero_message

def menssangem_aleatoria_quinta():

    mensagem_sorteada = numero_message()

    mensagem_quinta_1 = (
        "Boa noite Caldolover de plantão! 😁🔥 "
        "Hoje é a nossa tradicional Quinta Nordestina e o caldo de nordestino está com R$3 de desconto "
        "exclusivo aqui no WhatsApp! 🌵✨ "
        "(Se quiser pausar o recebimento das promoções, é só informar.)"
    )

    mensagem_quinta_2 = (
        "Atenção querido(a)! 🤩🌵 "
        "A Quinta Nordestina chegou trazendo caldo de nordestino a partir de 6,99 para nosso Caldolover aproveitar "
        "— somente para pedidos feitos pelo WhatsApp! 😁🔥 "
        "(Caso não deseje mais receber nossas ofertas, basta avisar.)"
    )

    mensagem_quinta_3 = (
        "Boa noite querido(a)! 🌙🔥 "
        "Hoje todos os caldos de nordestino estão com 30% de desconto para nosso Caldolover ficar feliz, "
        "promoção exclusiva do WhatsApp! 🌵✨ "
        "(Se preferir parar de receber nossas mensagens, é só pedir.)"
    )

    mensagem_quinta_4 = (
        "Atenção! 🤩🔥 "
        "A Quinta Nordestina tá daquele jeitinho: caldo de nordestino com R$3 OFF em qualquer tamanho para nosso Caldolover aproveitar, "
        "exclusivo pelo WhatsApp! 🌵✨ "
        "(Se não quiser continuar recebendo promoções, é só avisar.)"
    )

    mensagem_quinta_5 = (
        "Boa noite! 😄🌵 "
        "Hoje tem caldo nordestino a partir de 6,99 para nosso Caldolover ficar alegre, válido somente no WhatsApp! 🔥 "
        "(Caso não queira mais receber novidades, basta informar.)"
    )

    mensagem_quinta_6 = (
        "Atenção querido(a)! 🔥🌵 "
        "Na Quinta Nordestina, todos os caldos de nordestino estão com 30% de desconto para esquentar a noite do nosso CaldoLover 🔥 "
        "— mas somente aqui no WhatsApp! 😁 "
        "(Se desejar sair da lista, é só nos comunicar.)"
    )

    mensagem_quinta_7 = (
        "Boa noite Caldolover! 🤩🔥 "
        "O caldo nordestino está com R$3 OFF em todos os tamanhos! Promoção exclusiva do WhatsApp! 🌵✨ "
        "(Se não quiser mais receber nossas promoções, pode avisar sem problema.)"
    )

    mensagem_quinta_8 = (
        "Atenção! 🔥🌵 "
        "Hoje a Quinta Nordestina traz caldo de nordestino a partir de 6,99 para nosso Caldolover aproveitar com alegria, "
        "exclusivo pelo WhatsApp! 😁 "
        "(Caso queira encerrar o recebimento das ofertas, basta avisar.)"
    )

    mensagem_quinta_9 = (
        "Boa noite Caldolover querido(a)! 🤩🔥 "
        "Temos 30% OFF no caldo de nordestino hoje, oferta exclusiva do WhatsApp! 🌵✨ "
        "(Se preferir não receber mensagens promocionais, é só informar.)"
    )

    mensagem_quinta_10 = (
        "Atenção querido(a)! 😁🔥 "
        "A Quinta Nordestina chegou trazendo caldo nordestino com R$3 de desconto alegrar a noite do nosso CaldoLover, "
        "promoção válida somente aqui pelo WhatsApp! 🌵✨ "
        "(Se quiser parar de receber as promoções, é só mandar mensagem.)"
    )

    dict_mensagens= {
        1: mensagem_quinta_1,
        2: mensagem_quinta_2,
        3: mensagem_quinta_3,
        4: mensagem_quinta_4,
        5: mensagem_quinta_5,
        6: mensagem_quinta_6,
        7: mensagem_quinta_7,
        8: mensagem_quinta_8,
        9: mensagem_quinta_9,
        10: mensagem_quinta_10
    }

    for chave in dict_mensagens:
        if chave == mensagem_sorteada:
            return dict_mensagens[chave]

def menssangem_aleatoria_quarta():

    mensagem_sorteada = numero_message()

    mensagem1 = (
        "Caldolover de plantão, atenção que hoje tá imperdível! 🤩🔥 "
        "Todos os caldos de sururu estão com 25% de desconto exclusivamente para pedidos no WhatsApp! 🌵✨ "
        "(Caso prefira não receber nossas promoções, é só pedir.)"
    )

    mensagem2 = (
        "Boa noite, Caldolover querido(a)! 😁 Hoje é dia de aproveitar: caldo de sururu "
        "a partir de R$8,99 somente pelo WhatsApp! 🌵✨ "
        "(Se desejar parar de receber nossas ofertas, é só informar.)"
    )

    mensagem3 = (
        "Atenção, Caldolover! 👀 O sururu tá liberado com R$3 de desconto em todos os tamanhos — promoção exclusiva no WhatsApp! 🤩🔥 "
        "(Se não quiser receber essas mensagens, é só avisar.)"
    )

    mensagem4 = (
        "Boa noite! 🤩🔥 A quarta do sururuvis está garantida com 25% OFF nos caldos de sururu, apenas aqui no WhatsApp! 🌵✨ "
        "(Caso deseje sair da lista de promoções, é só pedir.)"
    )

    mensagem5 = (
        "Atenção! 👀 Hoje tem caldo de sururu a partir de R$8,99 exclusivamente no WhatsApp para o nosso Caldolover ficar feliz! 🤩🔥 "
        "(Se preferir não receber mais mensagens, é só avisar.)"
    )

    mensagem6 = (
        "Boa noite, Caldolover! 😁 O caldo de sururu está com R$3 de desconto em todos os tamanhos — promoção exclusiva do WhatsApp! 🌵✨ "
        "(Se quiser parar de receber promoções, só nos sinalizar.)"
    )

    mensagem7 = (
        "Atenção! 🤩🔥 Caldo de sururu com 25% de desconto exclusivamente aqui no WhatsApp para o nosso Caldolover ficar feliz! 🌵✨ "
        "(Se não quiser mais receber ofertas, é só informar.)"
    )

    mensagem8 = (
        "Boa noite, Caldolover querido(a)! 👀 Hoje tem sururu a partir de R$8,99 só no WhatsApp! Promoção quentinha chegando! 🤩🔥 "
        "(Se desejar sair da lista de promoções, basta avisar.)"
    )

    mensagem9 = (
        "Atenção! 🤩🔥 O caldo de sururu está com R$3 OFF em todos os tamanhos — e essa delícia é exclusiva para pedidos via WhatsApp para o nosso Caldolover ficar feliz! 🌵✨ "
        "(Caso não queira mais receber promoções, só pedir.)"
    )

    mensagem10 = (
        "Boa noite! 😁 Caldo de sururu com 25% de desconto disponível somente no WhatsApp para o nosso Caldolover ficar feliz! 🤩🔥 "
        "(Se preferir parar de receber nossas mensagens, é só avisar.)"
    )

    dict_mensagens = {
        "msg1": mensagem1,
        "msg2": mensagem2,
        "msg3": mensagem3,
        "msg4": mensagem4,
        "msg5": mensagem5,
        "msg6": mensagem6,
        "msg7": mensagem7,
        "msg8": mensagem8,
        "msg9": mensagem9,
        "msg10": mensagem10
    }

    for chave in dict_mensagens:
        if chave == mensagem_sorteada:
            return dict_mensagens[chave]

def menssangem_aleatoria_dias_frios():

    mensagem_sorteada = numero_message()

    # Mensagens personalizadas
    mensagem_1 = ("friozinho no fim de semana… o que falta para nosso CaldoLover fechar a noite "
                  "com chave de ouro? 🤔🔥 Um caldinho quentinho! 😋🌵 Hoje trazendo nossos lembretes e promoções pra você! "
                  "(Caso não queira receber nossos avisos e lembretes, é só avisar.)")

    mensagem_2 = ("aquele friozinho no fim de semana chegou… e para o nosso CaldoLover fechar a noite "
                  "com perfeição só falta um caldinho delicioso! 🤗🔥 Aproveite também nossos avisos e promoções deste fim de semana! "
                  "(Se preferir não receber nossos lembretes e avisos, basta nos informar.)")

    mensagem_3 = ("friozinho gostoso no fim de semana… o que falta para nosso CaldoLover fechar a noite "
                  "com chave de ouro? 😍🔥 Um caldinho bem quente! 🌵 E claro, passando com nossos lembretes e promoções! "
                  "(Se não quiser mais receber nossos avisos e lembretes, só avisar.)")

    mensagem_4 = ("fim de semana geladinho… e nosso CaldoLover já sabe o que falta pra completar, né? 😏🔥 "
                  "Um caldinho quentinho irresistível! Aproveitando para deixar nossos avisos e promoções aqui! "
                  "(Caso deseje parar de receber nossos lembretes, é só avisar.)")

    mensagem_5 = ("friozinho no fim de semana pedindo aquele aconchego… o que falta para nosso CaldoLover "
                  "fechar a noite com chave de ouro? 🤗🔥 Um caldinho quentinho e delicioso! 🌵 Ah, e aqui vão nossos lembretes e promoções! "
                  "(Se não quiser continuar recebendo nossos avisos, é só nos dizer.)")

    mensagem_6 = ("chegou o friozinho no fim de semana… e o que falta para nosso CaldoLover fechar bem a noite? "
                  "🤔🔥 Aquele caldinho quentinho que abraça! 🌵 Deixando também nossos avisos e promoções para você não perder nada. "
                  "(Caso queira parar de receber nossos lembretes, avise.)")

    mensagem_7 = ("friozinho do fim de semana batendo… e só falta uma coisa para nosso CaldoLover fechar a noite "
                  "com chave de ouro: um caldinho perfeito pra aquecer! 😌🔥 Junto disso, seguem nossos lembretes e promoções do dia! "
                  "(Se preferir não receber mais lembretes, basta avisar.)")

    mensagem_8 = ("com esse friozinho no fim de semana… o que falta para nosso CaldoLover completar a noite? "
                  "🥰🔥 Um caldinho saboroso! 🌵 Também aproveitamos para trazer nossos avisos e promoções. "
                  "(Caso não queira mais receber nossos lembretes, apenas nos avise.)")

    mensagem_9 = ("fim de semana geladinho chegando… e o que falta para nosso CaldoLover fechar a noite "
                  "com chave de ouro? 😋🔥 Um caldinho quentinho daqueles! 🌵 E claro, passando com nossos lembretes e promoções! "
                  "(Se não quiser receber nossos avisos e lembretes, é só informar.)")

    mensagem_10 = ("friozinho no fim de semana… perfeito pra quê? 🤔🔥 Para nosso CaldoLover fechar a noite "
                   "com chave de ouro com um caldinho delicioso! 😋 Aproveite também nossos avisos e promoções especiais. "
                   "(Caso não queira mais receber lembretes e avisos, avise por aqui.)")

    # Dicionário com todas as mensagens
    dict_mensagens = {
        1: mensagem_1,
        2: mensagem_2,
        3: mensagem_3,
        4: mensagem_4,
        5: mensagem_5,
        6: mensagem_6,
        7: mensagem_7,
        8: mensagem_8,
        9: mensagem_9,
        10: mensagem_10
    }

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

