# Desafio Sprint 9

## Descrição

Este desafio tem como objetivo processar dados da camada TRUSTED para a camada REFINED no S3 utilizando o AWS Glue. O processamento envolve o refinamento dos dados armazenados em formato .PARQUET, selecionando somente os dados que serão utilizados na análise da sprint 10.

Observação: Modifiquei e retirei algumas perguntas do desafio para melhor se adaptar aos dados coletados e para não ficar muito extenso.

## Motivação

A motivação para este desafio é garantir que os dados armazenados na camada REFINED estejam prontos para serem utilizados na análise de dados da sprint 10. O processamento dos dados é necessário para garantir que as informações estejam no formato correto e que somente os dados relevantes sejam selecionados para a análise.

### Questões a serem respondidas

Como diversos Fatores influenciam aa avaliação de um filme/série.

- 1. Filmes de comédia com orçamentos mais altos tendem a ser mais populares?
     Analisar a correlação entre o orçamento e a nota média para identificar se filmes com maior investimento são mais populares.
- 2. As avaliações de filmes de comédia variam significativamente entre diferentes países?
     Comparar as notas médias de filmes de comédia de acordo com o país de origem para identificar possíveis diferenças culturais na recepção.
- 3. Filmes de comédia mais lucrativos tendem a ser melhor avaliados?
     Examinar a relação entre a receita e a nota média para entender se o sucesso financeiro impacta a percepção crítica.
- 4. Séries de comédia com mais votos tendem a ter notas médias mais altas?
     Avaliar se a popularidade de uma série, medida pelo número de votos, está associada a uma melhor avaliação média.
- 5. Existe uma diferença nas avaliações de séries de comédia dirigidas por homens e mulheres?
     Comparar as notas médias de séries de comédia dirigidas por homens e por mulheres para identificar diferenças de avaliação.
- 6. Séries de comédia de países fora dos EUA tendem a ser melhor avaliadas?
     Analisar as notas médias de séries de comédia de acordo com o país de origem para identificar possíveis diferenças culturais na recepção.

## Pré-requisitos

- Python
- Apache Spark
- AWS Glue

## Estrutura do Projeto

O projeto contém o arquivo python para rodar o job no AWS Glue.

- `refined-aws.py`: Script para refinar os dados dos arquivos .PARQUET na AWS.

## Instruções de Uso

Certifique-se de que os arquivos presentes da camada TRUSTED estão formatados no padrão :

- /RAW/Local/CSV/Movies/2024/01/01/xxxx.csv
- /RAW/TMDB/JSON/Movies/2024/01/01/xxxx.json

### Processamento no AWS Glue

1. **Processar JSON no AWS Glue**:
   - Execute o script `refined-aws.py` como um job em Apache Spark no AWS Glue para refinar os arquivos .PARQUET e armazenar na camada REFINED no S3.
   - Parâmetros de entrada e saída são definidos nos detalhes do job na parte dos parâmetros.
