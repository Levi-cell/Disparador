import time
import re
import unicodedata

def confirmar_acao():
    print("Confirmar a ação?")
    print("[1]  → Sim")
    print("[2]  → Não")
    print("⚠️ Qualquer tecla também serve como não.")

    opc = input("Digite sua opção: ").strip()
    time.sleep(2)
    print("---------")

    if opc == "1":
        return True
    return False


def trata_entrada_de_opcao(numero):
    """
    Função de tratamento para caso o usuário digite uma letra ao em vez de número quando for interagir com o Menu.
    :param numero: Essa variável sempre receberá um número do tipo string.
    :return: Sempre retorna um número do tipo string.
    """

    while not numero.isdigit():
        numero = input("Opção inválida, apenas números, por favor digite novamente: ")

    return numero

def trata_entrada_de_id(id_cliente):
    """
    Função de tratamento para caso o usuário digite uma letra ao em vez de número quando for interagir com o Menu.
    :param : Essa variável sempre receberá um número do tipo string.
    :return: Sempre retorna um número do tipo string.
    """

    while not id_cliente.isdigit():
        id_cliente = input("Digite apenas números, digite o ID novamente: ")

    return id_cliente


def tratamento_de_retorno(parou):
    """
    Permite ao usuário voltar ao menu principal ou encerrar o programa.
    :param parou: Variável booleana de controle.
    :return: Retorna True ou False.
    """
    print("✔️ Ação encerrada...")
    print('\n------------------------------')
    print('O que deseja fazer agora?')
    print('[1]  → Voltar ao menu principal')
    print('[2]  → Encerrar o programa')
    print('⚠️ Qualquer tecla também irá encerrar o programa.')

    escolha = input("Digite sua opção: ").strip()

    # 1 → voltar ao menu
    if escolha == "1":
        print("Retornando ao menu principal...")
        time.sleep(2)
        return parou

    # 2 → encerrar (comportamento original)
    if escolha == "2":
        return not parou

    # fallback para segurança (qualquer outra tecla encerra)
    return not parou

def trata_nome_cliente(nome: str) -> str:
    """
    Valida o nome do cliente com regras:
      - Não pode ser vazio.
      - Não pode conter números.
      - Não pode conter caracteres especiais (ç, acentos, ., , etc).
      - Não pode conter palavras pejorativas.
      - Não pode ter exagero de letras repetidas (ex: xxxxxxx).
      - Aceita apenas letras A-Z e espaços.
      - Retorna com capitalização correta.
    """

    # Lista ampliada de palavras proibidas
    palavras_proibidas = {
        "porra", "merda", "bosta", "caralho", "cacete",
        "desgraça", "vagabundo", "vagabunda", "fdp",
        "foda", "foder", "fudido", "fudida", "arrombado",
        "arrombada", "pau", "rola", "piroca", "pica",
        "buceta", "xoxota", "xereca", "cu", "cuzão",
        "cuzona", "otário", "otária", "idiota", "imbecil",
        "burro", "burra", "corno", "corna", "desgraçado",
        "desgraçada", "canalha", "cretino", "cretina",
        "babaca", "energúmeno", "nojento", "nojenta",
        "trapaceiro", "enganador", "pilantra", "safado",
        "safada", "sem-vergonha", "sem vergonha",
        "puta", "puto", "putinha", "prostituta",
        "prostituto", "escroto", "escrota", "miserável", "macaco", "Macaco", "Gay", "gay"
    }

    # Função para checar repetição exagerada
    def repeticao_exagerada(texto):
        # Rejeita nomes com apenas 1 caractere
        if len(texto) == 1:
            return True

        count = 1
        for i in range(1, len(texto)):
            if texto[i] == texto[i - 1]:
                count += 1
                if count >= 3:  # rejeita repetição de 2 letras
                    return True
            else:
                count = 1

        return False

    while True:
        nome = nome.strip()

        if not nome:
            nome = input("❌ Nome vazio é inválido. Digite novamente: ")
            continue

        if any(ch.isdigit() for ch in nome):
            nome = input("❌ Nome não pode conter números. Digite novamente: ")
            continue

        # Apenas letras A-Z e espaços (sem acentos, sem cedilha)
        if not all(ch.isalpha() or ch == " " for ch in nome):
            nome = input("❌ Nome contém caracteres inválidos. Digite novamente (A-Z apenas): ")
            continue

        # Checagem de palavrões
        nome_minusculo = nome.lower()
        if any(p in nome_minusculo.split() for p in palavras_proibidas):
            nome = input("❌ Nome não permitido. Digite novamente: ")
            continue

        # Checagem de repetição exagerada
        if repeticao_exagerada(nome_minusculo):
            nome = input("❌ Nome não pode ter menos de 2 letras ou repetição exagerada de uma única letra."
                         " Digite novamente: ")
            continue

        return nome.title()


def trata_telefone(telefone: str) -> str:
    """
    Valida e formata o telefone.
    Aceita entrada com +55, (), -, espaços.
    Rejeita letras.
    Exige 11 dígitos: DDD + 9 + número.
    Verifica se o DDD é válido no Brasil.
    Exige obrigatoriamente o 9 após o DDD.
    """

    # Lista de DDDs válidos no Brasil
    ddds_validos = {
        "11","12","13","14","15","16","17","18","19",
        "21","22","24",
        "27","28",
        "31","32","33","34","35","37","38",
        "41","42","43","44","45","46",
        "47","48","49",
        "51","53","54","55",
        "61","62","64","65","66","67","68","69",
        "71","73","74","75","77",
        "79",
        "81","82","83","84","85","86","87","88","89",
        "91","92","93","94","95","96","97","98","99"
    }

    while True:
        if not isinstance(telefone, str):
            telefone = input("❌ Telefone inválido. Digite novamente: ")
            continue

        telefone = telefone.strip()

        # 🚫 Verifica letras
        if re.search(r"[a-zA-Z]", telefone):
            telefone = input("❌ Telefone não pode conter letras. Digite novamente: ")
            continue

        # 🔢 Remove tudo que não for número
        numeros = re.sub(r"\D", "", telefone)

        # 🌍 Remove DDI +55 se vier
        if numeros.startswith("55") and len(numeros) > 11:
            numeros = numeros[2:]

        # 📌 Exigir exatamente 11 dígitos (DDD + 9 + número)
        if len(numeros) != 11:
            telefone = input("❌ Telefone deve ter 11 dígitos (DDD + 9 + número). Digite novamente: ")
            continue

        # 📌 Validar DDD
        ddd = numeros[:2]
        if ddd not in ddds_validos:
            telefone = input(f"❌ DDD '{ddd}' não é válido no Brasil. Digite novamente: ")
            continue

        # 📌 Checar se tem o 9 obrigatório após o DDD
        if numeros[2] != "9":
            telefone = input("❌ O número de celular deve começar com o dígito 9 após o DDD. Digite novamente: ")
            continue

        return numeros


def trata_nome_pejorativo_txt(nome: str) -> str:
    """
    Limpa e valida um nome:
    - Aceita somente letras, acentos e espaço.
    - Remove emojis e caracteres inválidos.
    - Bloqueia palavras pejorativas.
    - Bloqueia repetições exageradas (aaaaaa, kkkkkk, xxxxxx).
    - Bloqueia nomes muito curtos ou vazios.
    - Sempre retorna apenas o primeiro nome.
    """


    # Remove emojis e caracteres não alfabéticos
    nome = re.sub(r"[^A-Za-zÀ-ÖØ-öø-ÿ\s]", "", nome)

    # Normaliza espaços
    nome = re.sub(r"\s+", " ", nome).strip()

    # Se estiver vazio → Saudação
    if not nome:
        return "Saudação"

    # Sempre manter apenas o primeiro nome
    primeiro = nome.split()[0]

    # Lista de palavras proibidas
    palavras_proibidas = {
        "porra", "merda", "bosta", "caralho", "cacete",
        "desgraça", "vagabundo", "vagabunda", "fdp",
        "foda", "foder", "fudido", "fudida", "arrombado",
        "arrombada", "pau", "rola", "piroca", "pica",
        "buceta", "xoxota", "xereca", "cu", "cuzão",
        "cuzona", "otário", "otária", "idiota", "imbecil",
        "burro", "burra", "corno", "corna", "desgraçado",
        "desgraçada", "canalha", "cretino", "cretina",
        "babaca", "energúmeno", "nojento", "nojenta",
        "trapaceiro", "enganador", "pilantra", "safado",
        "safada", "sem-vergonha", "sem vergonha",
        "puta", "puto", "putinha", "prostituta",
        "prostituto", "escroto", "escrota", "miserável",
        "macaco", "gay"
    }

    # Se o primeiro nome for pejorativo → Saudação
    if primeiro.lower() in palavras_proibidas:
        return "Saudação"

    # ❗ Bloqueia nomes com letras repetidas exageradas (ex: aaaaa, kkkkkk, xxxxx)
    if re.fullmatch(r"(.)\1{3,}", primeiro.lower()):
        return "Saudação"

    # ❗ Bloqueia nomes muito curtos (1 letra)
    if len(primeiro) <= 1:
        return "Saudação"

    # ❗ Bloqueia nomes tipo "aaa", "bbb", "ccc"
    if len(set(primeiro.lower())) == 1:
        return "Saudação"

    # Capitaliza corretamente (Carlos, João, José)
    return primeiro
