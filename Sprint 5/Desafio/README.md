# TUTORIAL PARA A EXECUÇÃO DO PROJETO

### Pré-requisitos
- Python 3.xx
- Boto3
- dotenv

### Passo 1: Clonar o Repositório

### Passo 2: Instalar as Dependências

### Passo 3: Fazer o upload do arquivo CSV para o S3

### Passo 4: Configurar as Credenciais AWS
Crie um arquivo .env na raiz do projeto e adicione suas credenciais AWS

### Passo 5: Executar o Script
Execute o script script.py para realizar as consultas no arquivo CSV armazenado no S3

O script script.py realiza duas consultas no arquivo CSV armazenado no S3:

Primeira Consulta:

Soma a quantidade (Quantidade) de itens que não têm o histórico 'Fiscal' e pertencem ao grupo '05'.
Encontra o comprimento máximo da descrição sintética (DescrSint).

Segunda Consulta:

Seleciona as datas de aquisição (DtAquisicao) que são anteriores a 2012.