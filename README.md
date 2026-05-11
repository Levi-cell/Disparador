# Disparador de Promoções

Aplicação em Python para gerenciar uma lista de clientes e enviar mensagens promocionais pelo WhatsApp Web com apoio de Selenium, Chrome em modo remoto e banco de dados MySQL.

> Projeto criado para uso operacional do Caldão Nordestino, com foco em cadastro de contatos, atualização de base, controle de blacklist e disparos com ou sem mídia.

## O que o projeto faz

O Disparador centraliza quatro rotinas principais:

- Mantém uma base de clientes em MySQL.
- Importa contatos exportados do Google Contacts.
- Permite adicionar, remover, consultar e corrigir clientes.
- Envia mensagens pelo WhatsApp Web para contatos ativos da lista de disparo.

Durante o disparo, o sistema abre o WhatsApp Web em um Chrome iniciado com `remote-debugging-port=9222`, monta a mensagem, opcionalmente anexa uma mídia e marca no banco quem já recebeu a mensagem do dia.

## Funcionalidades

- Menu interativo em terminal.
- Interface visual simples com Tkinter em `terminalApp.py`.
- Envio de mensagens promocionais do dia.
- Envio de mensagem de ausência.
- Envio de mensagem de atualização/mudança.
- Disparo com mídia ou sem mídia.
- Controle para evitar envio duplicado no mesmo ciclo.
- Validação de nomes e telefones brasileiros.
- Importação de contatos via CSV do Google Contacts.
- Limpeza e padronização de nomes importados.
- Remoção de contatos duplicados.
- Blacklist de clientes indesejados.
- Consulta e edição de dados de clientes.
- Build para `.exe` com PyInstaller.

## Estrutura do projeto

```text
Disparador/
├── terminalApp.py                         # Abre a interface Tkinter que simula um terminal
├── menuInterativo.py                      # Menu principal do sistema
├── conexao.py                             # Configuração da conexão MySQL
├── banco.py                               # Criação das tabelas principais
├── tratandoErros.py                       # Validações e tratamentos de entrada
├── requirements.txt                       # Dependências Python
├── OpcaoIndesejados/
│   └── indesejados.py                     # Gerenciamento da blacklist
├── opcoes/
│   ├── adicionar_lead.py                  # Adiciona cliente à base/lista
│   ├── remover_lead.py                    # Remove cliente da lista de disparo
│   ├── consultar_clientes.py              # Consulta e altera clientes
│   └── gerarTabela.py                     # Impressão de tabelas no terminal
├── ProcedimentosInstalacaoDisparador/
│   ├── automatedDownload.py               # Baixa contatos do Google Contacts
│   ├── resetFunction.py                   # Reset/importação da base
│   ├── processFunctions.py                # Insere contatos no banco
│   └── tratando_csv.py                    # Converte e limpa CSV/TXT de contatos
└── processDisparo/
    ├── DisparadorMain.py                  # Fluxo principal de disparo
    ├── Midia/                             # Imagens e vídeos usados nos disparos
    ├── SQLfunctions/                      # Consultas, inserts, updates e deletes
    └── SuportFunctions/                   # Chrome remoto, mensagens, mídia e funções auxiliares
```

## Requisitos

Este projeto foi feito para rodar em Windows.

Requisitos principais:

- Windows 10 ou superior.
- Python 3.12 ou versão compatível.
- Google Chrome instalado.
- MySQL Server rodando localmente.
- WhatsApp Web autenticado no perfil usado pelo sistema.
- Conta Google, caso você queira baixar contatos pelo Google Contacts.

Dependências Python importantes:

- `selenium`
- `mysql-connector-python`
- `pyautogui`
- `pywin32`
- `psutil`
- `requests`
- `pyinstaller`
- `tkinter` disponível na instalação do Python

Todas as dependências do projeto estão listadas em `requirements.txt`.

## Uso responsável

Use este sistema apenas com contatos que aceitaram receber comunicações da sua empresa.

Boas práticas:

- Envie mensagens apenas para clientes com consentimento.
- Respeite pedidos de remoção da lista.
- Use a blacklist para impedir novos envios a contatos indesejados.
- Evite volumes abusivos ou comportamento que viole as regras do WhatsApp.
- Mantenha a mensagem de descadastro/opção de não receber avisos.

## Configuração inicial

### 1. Clonar o repositório

```powershell
git clone https://github.com/Levi-cell/Disparador.git
cd Disparador
```

### 2. Criar ambiente virtual

```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

### 3. Instalar dependências

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Conferir caminhos fixos

Alguns arquivos usam caminhos absolutos. O caminho padrão esperado por partes do código é:

```text
C:\Disparo\Projeto\Disparador
```

Se você rodar em outra pasta, ajuste os caminhos nos arquivos:

- `ProcedimentosInstalacaoDisparador/automatedDownload.py`
- `ProcedimentosInstalacaoDisparador/processFunctions.py`
- `ProcedimentosInstalacaoDisparador/resetFunction.py`
- `ProcedimentosInstalacaoDisparador/tratando_csv.py`
- `processDisparo/SuportFunctions/enviar_foto.py`

Também confira o caminho do Chrome em:

```text
processDisparo/SuportFunctions/iniciar_chrome.py
```

Valor padrão:

```text
C:\Program Files\Google\Chrome\Application\chrome.exe
```

### 5. Configurar o banco MySQL

Edite `conexao.py` com os dados do seu MySQL:

```python
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SUA_SENHA",
    database="GerenciamentoCaldao"
)
```

Crie o banco de dados, se ainda não existir:

```sql
CREATE DATABASE GerenciamentoCaldao;
```

As tabelas usadas pelo projeto são:

```sql
CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    telefone VARCHAR(20) NOT NULL,
    disparo_status BOOLEAN NOT NULL,
    enviou_dia BOOLEAN NULL
);

CREATE TABLE clientes_indesejados (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    telefone VARCHAR(20) NOT NULL
);
```

O arquivo `banco.py` também contém funções para criação das tabelas.

### 6. Preparar o Chrome remoto

O sistema usa Chrome com depuração remota na porta `9222`.

Você pode iniciar manualmente com:

```powershell
& "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\SeleniumProfile"
```

Ou deixar o próprio sistema iniciar o Chrome pela função `iniciar_chrome_remoto()`.

No primeiro uso, abra o WhatsApp Web nesse Chrome e faça login pelo QR Code.

## Como executar

### Opção recomendada: interface Tkinter

```powershell
python terminalApp.py
```

Essa opção abre uma janela com visual de terminal e executa o menu principal.

### Opção direta pelo terminal

```powershell
python menuInterativo.py
```

## Manual do menu

Ao iniciar, o sistema mostra o menu:

```text
[1] - Disparar promoções
[2] - Adicionar alguém à lista de disparo
[3] - Remover alguém da lista de disparo
[4] - Consultar todos os clientes e alterar dados
[5] - Baixar nova base de dados para o disparo
[6] - Colocar contato(s) na lista de indesejados
[7] - Sair
```

### 1. Disparar promoções

Fluxo:

1. Escolha se deseja enviar com mídia ou sem mídia.
2. Escolha o tipo de mensagem.
3. O sistema abre o Chrome remoto.
4. O sistema acessa o WhatsApp Web.
5. Para cada cliente ativo, o sistema monta o link `https://web.whatsapp.com/send?phone=...`.
6. O sistema valida se o chat/contato está disponível.
7. A mensagem é colada no campo de texto.
8. Se houver mídia, a imagem ou vídeo é anexado.
9. A mensagem é enviada.
10. O cliente é marcado com `enviou_dia = TRUE`.

Ao final do ciclo, o sistema redefine `enviou_dia` para `FALSE`, liberando a base para um próximo disparo.

### 2. Adicionar alguém à lista

Permite cadastrar um novo cliente ou reativar um cliente que já existe no banco, mas estava fora da lista de disparo.

O telefone é validado no padrão brasileiro:

- DDD válido.
- 11 dígitos.
- Celular com `9` depois do DDD.

### 3. Remover alguém da lista

Remove o cliente apenas da lista de disparo, alterando `disparo_status` para `FALSE`.

O registro continua no banco.

### 4. Consultar clientes e alterar dados

Mostra a base cadastrada e permite alterar dados de um cliente, como nome e telefone.

### 5. Baixar nova base de dados

Fluxo de atualização:

1. Remove CSV/TXT antigos da pasta de instalação.
2. Abre o Google Contacts.
3. Exporta contatos em CSV.
4. Move o CSV para a pasta do projeto.
5. Gera `contatos.txt`.
6. Limpa nomes e telefones.
7. Preserva contatos existentes quando possível.
8. Remove contatos da blacklist.
9. Recria a tabela `clientes`.
10. Insere contatos no banco.
11. Remove duplicados.

Importante: em primeiro acesso, pode ser necessário fazer login na conta Google manualmente.

### 6. Lista de indesejados

Move contatos para a blacklist (`clientes_indesejados`) e remove esses contatos da tabela principal.

Clientes na blacklist são preservados mesmo após atualização da base.

### 7. Sair

Encerra o sistema.

## Mensagens e mídias

As mensagens ficam em:

```text
processDisparo/SuportFunctions/set_message.py
```

As mídias ficam em:

```text
processDisparo/Midia/
```

O arquivo `enviar_foto.py` escolhe a mídia de acordo com o tipo de mensagem e, em alguns casos, com o dia da semana.

Exemplos:

- Quarta-feira: `quarta.png`
- Quinta-feira: `Quinta.jpg`
- Ausência: `ausencia.png`
- Atualização: `aviso.jpg`

## Deploy local

### Deploy como script Python

Use este modo quando você quer rodar com código fonte:

```powershell
cd C:\Disparo\Projeto\Disparador
.\.venv\Scripts\activate
python terminalApp.py
```

Checklist antes de rodar:

- MySQL ativo.
- `conexao.py` configurado.
- Chrome instalado no caminho esperado.
- WhatsApp Web logado no perfil `C:\SeleniumProfile`.
- Mídias presentes em `processDisparo/Midia`.
- Tabelas criadas no banco.

### Deploy como executável Windows

O projeto já possui `terminalApp.spec`, então o build pode ser feito com PyInstaller:

```powershell
.\.venv\Scripts\activate
pyinstaller terminalApp.spec
```

Ao final, o executável será gerado em:

```text
dist\terminalApp.exe
```

Para distribuir em outra máquina, leve junto:

- `dist\terminalApp.exe`
- Pasta `processDisparo/Midia`
- Acesso ao MySQL configurado
- Google Chrome instalado
- Perfil `C:\SeleniumProfile` configurado ou pronto para login

Se preferir gerar um build novo sem usar o `.spec`:

```powershell
pyinstaller --onefile --windowed terminalApp.py
```

Depois teste o executável em uma máquina limpa antes de usar em produção.

## Dicas de operação

- Não minimize o navegador durante o disparo.
- Não use o Chrome do disparo enquanto o robô está enviando mensagens.
- No primeiro login do WhatsApp Web, pare o sistema, leia o QR Code e execute novamente.
- Mantenha os contatos de teste no início da base para validar a mensagem antes de disparar para todos.
- Confira os clientes inválidos apresentados ao final do disparo.
- Atualize também o telefone no celular quando corrigir manualmente um número no sistema.

## Solução de problemas

### Chrome não conecta

Verifique se a porta `9222` está livre e se o Chrome foi aberto com:

```powershell
--remote-debugging-port=9222 --user-data-dir="C:\SeleniumProfile"
```

### WhatsApp pede QR Code

Faça login manualmente no Chrome aberto com o perfil `C:\SeleniumProfile` e execute o sistema novamente.

### Foto não encontrada

Confirme se a mídia existe no caminho usado em `processDisparo/SuportFunctions/enviar_foto.py`.

### Erro de banco de dados

Confira:

- MySQL está rodando.
- Banco `GerenciamentoCaldao` existe.
- Usuário e senha em `conexao.py` estão corretos.
- Tabelas `clientes` e `clientes_indesejados` existem.

### Google Contacts não exporta

Faça login manual na conta Google, aguarde a página carregar e tente novamente.

Como a automação usa XPaths do Google Contacts, mudanças na interface do Google podem exigir atualização dos seletores em `automatedDownload.py`.

### WhatsApp mudou a tela

O projeto usa XPaths do WhatsApp Web. Se o WhatsApp alterar a interface, pode ser necessário ajustar seletores em:

- `processDisparo/DisparadorMain.py`
- `processDisparo/SuportFunctions/enviar_foto.py`
- `processDisparo/SuportFunctions/PoupTxtfield.py`

## Observações técnicas

- O sistema usa `enviou_dia` para evitar duplicidade durante o disparo.
- O sistema usa `disparo_status` para definir quem está ativo na lista.
- A blacklist fica em `clientes_indesejados`.
- O envio depende de interação visual com Chrome/Windows, então a automação deve rodar em uma sessão gráfica ativa.
- Existem caminhos absolutos no código; para um deploy mais portável, recomenda-se migrar esses caminhos para variáveis de ambiente ou arquivo `.env`.

## Melhorias recomendadas

- Remover credenciais fixas do código e usar `.env`.
- Trocar caminhos absolutos por configuração centralizada.
- Ignorar `__pycache__`, `build`, `dist` e arquivos gerados no Git.
- Adicionar logs estruturados.
- Criar testes automatizados para validações de nome/telefone.
- Adicionar tela de configuração inicial.
- Criar instalador Windows com dependências e checagens de ambiente.

## Licença

Este repositório ainda não possui arquivo de licença definido.
