# Desafio Sprint 8

## Descrição

Este desafio tem como objetivo processar dados da camada RAW para a camada TRUSTED no S3 utilizando o AWS Glue. O processamento envolve a transformação de arquivos CSV e JSON em arquivos Parquet, aplicando as devidas conversões de tipos e limpeza de dados.

Observação: Modifiquei o script da sprint 7 também para melhorar a aleatoriadade dos dados gerados.

## Motivação

A motivação para este desafio é garantir que os dados armazenados na camada TRUSTED estejam limpos, estruturados e prontos para análise. A transformação de dados em formato Parquet melhora a eficiência de armazenamento e consulta, facilitando análises futuras.

### Questões a serem respondidas

1. Existe uma correlação entre o orçamento de um filme de comédia e sua nota média? Filmes com orçamentos mais altos tendem a receber melhores avaliações?
   Comparar o orçamento médio de filmes de comédia com alta e baixa avaliação.

2. Existe alguma diferença significativa nas avaliações de filmes de comédia produzidos em diferentes países?
   Analisar a distribuição de gêneros de comédia por país de origem.

3. Existe uma relação entre a receita de um filme de comédia e sua nota média? Filmes mais lucrativos tendem a ser melhor avaliados?
   Comparar a receita média de filmes de comédia com alta e baixa avaliação.

4. O número de votos de filmes de comédia no CSV está correlacionado com o número de votos no TMDB?
   Analisar a correlação entre o número de votos do CSV e os dados do TMDB, verificando se há uma correspondência direta ou se existem diferenças na popularidade das produções em cada plataforma.

5. Filmes de comédia com maior número de votos ou presença de grandes nomes (atores ou diretores renomados) tendem a ter uma nota média mais alta?
   Relação entre popularidade (número de votos e presença de grandes nomes) e notas médias.

6. Séries de comédia lançados em diferentes décadas têm variação significativa nas notas médias?
   Analisar se séries de comédia de décadas passadas são avaliados de forma diferente em comparação com os lançados recentemente.

7. Qual a duração média das séries de comédia mais bem avaliados?
   Explorar se séries de comédia mais curtos ou mais longos tendem a ser melhor avaliados pelo público.

8. Qual o percentual de séries de comédia dirigidas por mulheres e homens e como essas séries são avaliadas em comparação?
   Comparar a distribuição de diretores e diretoras de séries de comédia, analisando se há uma diferença significativa nas avaliações de acordo com o gênero do diretor.

## Pré-requisitos

- Python
- Apache Spark
- AWS Glue

## Estrutura do Projeto

O projeto está estruturado da seguinte forma:

- `local-csv.py`: Script para processar arquivos CSV localmente e transformá-los em arquivos Parquet.
- `local-json.py`: Script para processar arquivos JSON localmente e transformá-los em arquivos Parquet.
- `csvaws.py`: Script para processar arquivos CSV no AWS Glue e transformá-los em arquivos Parquet na camada TRUSTED.
- `jsonaws.py`: Script para processar arquivos JSON no AWS Glue e transformá-los em arquivos Parquet na camada TRUSTED.

## Instruções de Uso

Certifique-se de que os arquivos presentes da camada RAW estão formatados no padrão :

- /RAW/Local/CSV/Movies/2024/01/01/xxxx.csv
- /RAW/TMDB/JSON/Movies/2024/01/01/xxxx.json

### Processamento Local

Fiz o processamento local para demonstrar o funcionamento do script para o vídeo.

1. **Processar CSV Localmente**:

   - Execute o script `local-csv.py` para transformar arquivos CSV em Parquet.
   - Caminhos de entrada e saída são definidos no script.

2. **Processar JSON Localmente**:
   - Execute o script `local-json.py` para transformar arquivos JSON em Parquet.
   - Caminhos de entrada e saída são definidos no script.

### Processamento no AWS Glue

1. **Processar CSV no AWS Glue**:

   - Execute o script `csvaws.py` como um job em Apache Spark no AWS Glue para transformar arquivos CSV em Parquet passando para a camada TRUSTED.
   - Path de entrada e saída são definidos nos detalhes do job na parte dos parâmetros.

2. **Processar JSON no AWS Glue**:
   - Execute o script `jsonaws.py` como um job em Apache Spark no AWS Glue para transformar arquivos JSON em Parquet passando para a camada TRUSTED.
   - Parâmetros de entrada e saída são definidos nos detalhes do job na parte dos parâmetros.
