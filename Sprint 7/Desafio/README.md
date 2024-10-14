# Desafio Sprint 7

## Descrição

Este desafio tem como objetivo consumir dados da API do TMDB e armazenar no bucket do S3 da AWS. A função Lambda irá buscar filmes e séries por gênero e salvar os resultados em arquivos JSON no S3.

## Motivação de cada API

Pensei em utilizar a API do TMDB para buscar dados que sejam diferentes dos dados fornecidos nos arquivos CSV. Para assim complementar os dados e enriquecer a análise. Neste momento, optei por fazer somente uma execução com 100 filmes e 100 séries por cada arquivo JSON como foi solicitado.

### Questões a serem respondidas

1. Existe uma correlação entre o orçamento de um filme de comédia e sua nota média? Filmes com orçamentos mais altos tendem a receber melhores avaliações?
   Comparar o orçamento médio de filmes de comédia com alta e baixa avaliação.

2. Existe alguma diferença significativa nas avaliações de filmes de comédia produzidos em diferentes países?
   Analisar a distribuição de gêneros de comédia por país de origem.

3. Existe uma relação entre a receita de um filme de comédia e sua nota média? Filmes mais lucrativos tendem a ser melhor avaliados?
   Comparar a receita média de filmes de comédia com alta e baixa avaliação.

4. O número de votos de filmes de comédia no CSV está correlacionado com o número de votos no TMDB?
   Analisar a correlação entre o número de votos do CSV e os dados do IMDB, verificando se há uma correspondência direta ou se existem diferenças na popularidade das produções em cada plataforma.

5. Filmes de comédia lançados em diferentes décadas têm variação significativa nas notas médias?
   Analisar se Filmes de comédia de décadas passadas são avaliados de forma diferente em comparação com as lançadas recentemente.

6. Filmes de comédia com maior número de votos ou presença de grandes nomes (atores ou diretores renomados) tendem a ter uma nota média mais alta?
   Relação entre popularidade (número de votos e presença de grandes nomes) e notas médias.

7. Qual a duração média dos filmes de comédia mais bem avaliados?
   Explorar se filmes de comédia mais curtos ou mais longos tendem a ser melhor avaliados pelo público.

8. Qual o percentual de séries de comédia dirigidas por mulheres e homens e como essas séries são avaliadas em comparação?
   Comparar a distribuição de diretores e diretoras de séries de comédia, analisando se há uma diferença significativa nas avaliações de acordo com o gênero do diretor.

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
