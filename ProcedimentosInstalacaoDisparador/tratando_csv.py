import re
import csv
import time
from pathlib import Path
from processDisparo.SQLfunctions.ConsultFunctions import consulta_todos_cliente_sql, consulta_todos_clientes_indesejados_sql

def gerar_contatos_em_txt():
    results = []

    # Exporte o arquivo csv com os contatos em https://contacts.google.com/ e coloque na pasta
    # ProcedimentoInstalacaoDisparador
    caminho_csv = r'C:\Disparo\Projeto\Disparador\ProcedimentosInstalacaoDisparador\contacts.csv'
    caminho_saida = r'C:\Disparo\Projeto\Disparador\ProcedimentosInstalacaoDisparador\contatos.txt'

    # Abrir o arquivo CSV
    with open(caminho_csv, "r", encoding="utf-8") as f:
        reader = csv.reader(f)

        for row in reader:
            # Ignorar linha de cabeçalho
            if row and row[0] == "First Name":
                continue

            # Nome está SEMPRE na coluna 0
            name = row[0].strip() if row[0].strip() else "Null"

            # Converter a linha inteira em string para facilitar regex
            full_line = ",".join(row)

            # Capturar todos os números da linha
            nums = re.findall(r"\+?\d[\d\-\s]{6,}\d", full_line)

            # Se tiver números → pegar o último
            num = nums[-1] if nums else "Null"

            # Limpar
            num = num.replace("+55", "").replace("-", "").replace(" ", "")

            # Garantir número no padrão: DDD + 9 + número (11 dígitos)
            if re.fullmatch(r"\d{10}", num):
                num = num[:2] + "9" + num[2:]

            results.append((name, num))

    # Criar arquivo contatos.txt
    table = "Nome ||| Numero\n\n"

    for n, v in results:
        table += f"- {n} ||| {v}\n\n"

    # Salvar no caminho solicitado
    with open(caminho_saida, "w", encoding="utf-8") as f:
        f.write(table)

    print("✔ Arquivo contatos.txt gerado com sucesso!")
    print(f"📁 Caminho salvo: {caminho_saida}")

def processar_contatos_txt():
    caminho = r'C:\Disparo\Projeto\Disparador\ProcedimentosInstalacaoDisparador\contatos.txt'
    p = Path(caminho)

    if not p.exists():
        print("Arquivo não encontrado.")
        return

    linhas = p.read_text(encoding='utf-8').splitlines()

    # Encontrar onde começam os contatos (linha que inicia com "-")
    inicio = 0
    for i, ln in enumerate(linhas):
        if ln.strip().startswith("-"):
            inicio = i
            break

    cabecalho = linhas[:inicio]
    dados = linhas[inicio:]

    def limpar_nome(nome):
        # remove tudo que não for letra, número ou espaço (inclui emojis)
        nome_limpo = re.sub(r'[^A-Za-z0-9À-ÖØ-öø-ÿ\s]', '', nome)

        # normalizar espaços
        nome_limpo = re.sub(r'\s+', ' ', nome_limpo).strip()

        # se esvaziou → Saudação
        if nome_limpo == "":
            return "Saudação"

        # manter apenas o primeiro nome
        primeiro_nome = nome_limpo.split()[0]

        return primeiro_nome

    saida = cabecalho.copy()

    for ln in dados:
        if "|||" not in ln:
            continue

        nome_raw, numero = ln.split("|||", 1)
        nome_raw = nome_raw.lstrip("-").strip()
        numero = numero.strip()

        nome_final = limpar_nome(nome_raw)

        saida.append(f"- {nome_final} ||| {numero}")
        saida.append("")

    p.write_text("\n".join(saida), encoding="utf-8")
    print("✔ Contatos processados com sucesso!")

def verifica_numeros_iguais():
    # Consulta todos os clientes no banco
    dados_banco = consulta_todos_cliente_sql()
    # dados_banco deve retornar algo como:
    # [ {"nome": "João", "telefone": "75988444037"}, ... ]

    if not dados_banco:

        return

    # Criar dicionário telefone → nome
    mapa_banco = {}
    for cliente in dados_banco:
        telefone = str(cliente[2]).strip()
        nome = cliente[1].strip()
        mapa_banco[telefone] = nome

    caminho = r"C:\Disparo\Projeto\Disparador\ProcedimentosInstalacaoDisparador\contatos.txt"
    p = Path(caminho)

    if not p.exists():
        print(f"Arquivo não encontrado: {caminho}")
        return

    linhas = p.read_text(encoding="utf-8").splitlines()

    # Encontrar onde começam os contatos
    inicio = 0
    for i, ln in enumerate(linhas):
        if ln.strip().startswith("-"):
            inicio = i
            break

    cabecalho = linhas[:inicio]
    dados = linhas[inicio:]

    saida = cabecalho.copy()

    for ln in dados:
        if "|||" not in ln:
            saida.append(ln)
            continue

        esquerda, direita = ln.split("|||", 1)
        nome_raw = esquerda.lstrip("-").strip()
        telefone_raw = direita.strip()

        # Se esse telefone existir no banco → substitui nome
        if telefone_raw in mapa_banco:
            nome_final = mapa_banco[telefone_raw]
        else:
            nome_final = nome_raw  # mantém o nome atual

        saida.append(f"- {nome_final} ||| {telefone_raw}")
        saida.append("")

    # Salvar o arquivo novamente
    p.write_text("\n".join(saida), encoding="utf-8")

    print("✔ Arquivo atualizado com nomes do banco de dados!")
    print(f"📁 {caminho}")

from pathlib import Path

def remove_clientes_indesejados():
    # Busca lista no banco [(id, nome, telefone), ...]
    lista_indesejados = consulta_todos_clientes_indesejados_sql()

    # Monta set com os telefones (cliente[2])
    numeros_indesejados = set()
    for cliente in lista_indesejados:
        telefone = cliente[2]   # telefone é o índice 2
        telefone = telefone.strip()
        numeros_indesejados.add(telefone)

    # Caminho do arquivo
    caminho = r"C:\Disparo\Projeto\Disparador\ProcedimentosInstalacaoDisparador\contatos.txt"
    p = Path(caminho)

    if not p.exists():
        return

    # Lê o arquivo
    linhas = p.read_text(encoding="utf-8").splitlines()

    novas_linhas = []

    for linha in linhas:

        # Linha que não tem número, apenas copiar
        if "|||" not in linha:
            novas_linhas.append(linha)
            continue

        # separa nome e número
        partes = linha.split("|||", 1)
        numero_raw = partes[1]

        numero = numero_raw.strip()

        # mantém SOMENTE se o número NÃO estiver em indesejados
        if numero not in numeros_indesejados:
            novas_linhas.append(linha)

    # Regrava o arquivo filtrado
    p.write_text("\n".join(novas_linhas), encoding="utf-8")

def molda_txt_completo():
    gerar_contatos_em_txt()
    processar_contatos_txt()
    verifica_numeros_iguais()
    remove_clientes_indesejados()

