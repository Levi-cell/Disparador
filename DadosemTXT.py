import re
# Quando o cliente exportar os para converter em uma tabela txt basica com nome e número
# Assim irá ficar mais fácil de fazer o comando INSERT
raw = """rosahelena,,,,,,,,,,,,,,,,* myContacts,Mobile,+55 75 88025-541,,
Rosângella,,,,,,,,,,,,,,,,* myContacts,Mobile,+55 75 83322-645,,
Rosângella,,Conrado❤,,,,,,,,,,,,,,* myContacts,Mobile,+55 75 83322-645,,
Sandro,,,,,,,,,,,,,,,,* myContacts,Versão antiga,+55 75 9844-8294,Mobile,+55 75 99844-8294
Sara,,,,,,,,,,,,,,,,* myContacts,Versão antiga,+55 75 9958-2233,Mobile,+55 75 99958-2233
Sara,,Barreto,,,,,,,,,,,,,,* myContacts,Mobile,+55 75 88277-711,,
Simara,,,,,,,,,,,,,,,,* myContacts,Mobile,+55 75 82581-691,,
Simaria,,,,,,,,,,,,,,,,* myContacts,Mobile,+55 75 82581-691,,
Sther ✨,,,,,,,,,,,,,,,,* myContacts,Versão antiga,+557581316796,Mobile,+55 75 98131-6796
Suellen💘,,,,,,,,,,,,,,,,* myContacts,Versão antiga,+557583137195,Mobile,+55 75 98313-7195
Tailane,,Santana,,,,,,,,,,,,,,* myContacts,Mobile,+55 75 88574-879,,
Tâmara Oliveira,,,,,,,,,,,,,,,,* myContacts,Mobile,+5511963244894,,
Tamires Reis,,,,,,,,,,,,,,,,* myContacts,Versão antiga,+557583542652,Mobile,+55 75 98354-2652
Tânia Silva,,,,,,,,,,,,,,,,* myContacts,Versão antiga,+557591624924,Mobile,+55 75 99162-4924
Tássia Reis,,,,,,,,,,,,,,,,* myContacts,Versão antiga,+557598605027,Mobile,+55 75 99860-5027
Tatiane,,,,,,,,,,,,,,,,* myContacts,Mobile,+55 75 81667-465,,
TAYNA Quero,,,,,,,,,,,,,,,,* myContacts,Versão antiga,+557588221521,Mobile,+55 75 98822-1521
Thai,,,,,,,,,,,,,,,,* myContacts,Versão antiga,+557588963716,Mobile,+55 75 98896-3716
Thiago,,,,,,,,,,,,,,,,* myContacts,Versão antiga,+557182616626,Mobile,+55 71 98261-6626
Thialla 💙,,,,,,,,,,,,,,,,* myContacts,Mobile,+557581288875,,
Tonny,Cerqueira,🎸🎼,,,,,,,,,,,,,,* myContacts,Mobile,+55 75 88624-476,,
Torlone Castro,,,,,,,,,,,,,,,,* myContacts,Versão antiga,+557591252888,Mobile,+55 75 99125-2888
Udemberg,,,,,,,,,,,,,,,,* myContacts,Versão antiga,+55 75 9922-1986,Mobile,+55 75 99922-1986
Val,,Juracy,,,,,,,,,,,,,,* myContacts,Mobile,+55 75 88126-471,,
valnei,,pires,,,,,,,,,,,,,,* myContacts,Mobile,+55 75 91177-707,,
Vanessa,,,,,,,,,,,,,,,,* myContacts,Versão antiga,+55 75 9991-3314,Mobile,+55 75 99991-3314
Vanessa,,Passos,,,,,,,,,,,,,,* myContacts,Mobile,+55 75 88924-184,,
Yan,,Lage,,,,,,,,,,,,,,* myContacts,Versão antiga,+55 75 9245-4636,Mobile,+55 75 99245-4636
Yasmin,,,,,,,,,,,,,,,,* myContacts,Mobile,+55 75 99436-204,,
Yasmin Menezes,,,,,,,,,,,,,,,,* myContacts,Versão antiga,+557588271805,Mobile,+55 75 98827-1805
Yasmin,,MMA,,,,,,,,,,,,,,* myContacts,Mobile,+55 75 99943-6204,,
Yasmin,,Moura,,,,,,,,,,,,,,* myContacts,Mobile,+55 71 91729-213,,
"""

lines = raw.strip().split("\n")
results = []

for line in lines:
    name = line.split(",")[0].strip()
    if not name:
        name = "Null"

    nums = re.findall(r"\+?\d[\d\-\s]{6,}\d", line)
    num = nums[-1] if nums else "Null"

    num = num.replace("+55", "").replace("-", "").replace(" ", "")

    if re.fullmatch(r"\d{10}", num):
        num = num[:2] + "9" + num[2:]

    results.append((name, num))

table = "Nome ||| Numero\n\n"
for n, v in results:
    table += f"- {n} ||| {v}\n\n"

# 🔥 AQUI GERAMOS O ARQUIVO TXT
with open("contatos.txt", "w", encoding="utf-8") as f:
    f.write(table)

print("Arquivo contatos.txt gerado com sucesso!")
