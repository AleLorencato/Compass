# Desafio Sprint 7

## Descrição

Este desafio tem como objetivo consumir dados da API do TMDB e armazenar no bucket do S3 da AWS. A função Lambda irá buscar filmes e séries por gênero e salvar os resultados em arquivos JSON no S3.

## Pré-requisitos

Python 3.10
Docker
tmdbv3api
Requests

## Passo a Passo

- Passo 1: Clonar o Repositório
  Clone o repositório para sua máquina local

- Passo 2: Criar a Camada Lambda
  Execute o docker para criar a camada lambda:

```bash
docker build -t [nome da imagem] .
docker run -it [nome da imagem] bash
```

Crie e Navegue até o Diretório python

```bash
cd ~
mkdir -p layer_dir/python
cd layer_dir/python
```

Instalar as Bibliotecas na Pasta python

```bash
python3.10 -m pip install requests -t .
python3.10 -m pip install tmdbv3api -t .
```

Compactar o Diretório python

```bash
cd /root/layer_dir
tar -czvf [nome-camada] python
```

Fazer Upload da Camada para o AWS Lambda

Na aba Layers, crie uma nova camada e selecione a versão do python 3.10 adicionando o arquivo compactado.(Formato .zip)

- Passo 3: Configurar a Função Lambda
  No console do AWS Lambda, crie uma função lambda com python 3.10 e adicione a camada criada.

- Passo 4: Configurar a o arquivo lambda_function.py e as dependências
  Coloque o Arquivo requests-layer.zip na pasta da função lambda conforme na imagem abaixo:
  ![Função Lambda](../Evidencias/image.png)

- Passo 5: Configurar as Credenciais AWS
  Salvar as chaves da API do TMDB como variáveis de ambiente no AWS lambda

### Agora a função lambda está pronta para ser executada.

### Observações

É necessário colocar a pasta requests-layer.zip na pasta da função lambda para que a função lambda consiga executar, pois a biblioteca requests teve que ser instalada manualmente devido a problemas de compatibilidade com o AWS Lambda.

- Os arquivos JSON serão salvos no bucket do S3 com o caminho :
  Filmes: Raw/Local/TMDB/JSON/Movies/[data atual]/tmdb_comedy_movies.json
  Séries: Raw/Local/TMDB/JSON/Series/[data atual]/tmdb_comedy_series.json
