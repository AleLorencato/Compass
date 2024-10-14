# Desafio

1. [Pasta do Desafio](./Desafio/)

# Sobre o Desafio Final

## Desafio de Construção de Data Lake no tema de Animação e Comédia

### Objetivo

O desafio consiste na construção de um Data Lake para armazenar, processar e consumir dados de filmes e séries relacionados aos gêneros de **animação** e **comédia**. O processo é dividido em múltiplas camadas que incluem ingestão, armazenamento, processamento e consumo dos dados.

### Etapas do Desafio

1. **Ingestão dos Dados**: Serão realizados dois tipos de ingestão de dados:

   - Arquivos CSV contendo informações sobre filmes e séries (fornecidos no início do desafio).
   - Dados obtidos através da API do **TMDB** (The Movie Database).

2. **Armazenamento em Data Lake**: Os dados serão organizados e armazenados no Data Lake, utilizando a camada **RAW Zone** do **AWS S3**. Após a ingestão, os dados serão processados e movidos para camadas posteriores onde serão padronizados e catalogados.

3. **Processamento e Transformação**: Com o uso de **Apache Spark**, os dados serão processados, transformados e organizados em um formato dimensional para análise.

4. **Consumo de Dados e Análises**: As informações processadas serão consumidas utilizando dashboards analíticos para responder perguntas específicas sobre filmes e séries de animação e comédia.

### Motivo da Análise

O Data Lake será utilizado para responder questões relacionadas ao desempenho de filmes e séries de animação e comédia, a fim de identificar padrões de sucesso e discrepâncias entre diferentes plataformas de avaliação (TMDB e IMDB).

### Perguntas que serão respondidas

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

# Exercícios

1. [Exercício 1](./Exercicios/ex1/)
2. [Exercício 2](./Exercicios/ex2/)
3. [Exercício 3](./Exercicios/ex3/)

# Evidências

Evidência 1: Exercício 1 - S3 Bucket
![Evidência 1](./Evidencias/ex1-S3.png)
Evidência 2: Exercício 1 - Site Estático
![Evidência 2](./Evidencias/ex1-site-estatico.png)
Evidência 3: Exercício 2 - AWS Athena
![Evidência 3](./Evidencias/ex2-athena.png)
Evidência 4: Exercício 3 - Layer Pandas
![Evidência 4](./Evidencias/ex3-camada-pandas.png)
Evidência 5: Exercício 3 - AWS lambda
![Evidência 5](./Evidencias/ex3-lambda.png)
Evidência 6: limpeza de arquivos
![Evidência 6](./Evidencias/limpeza.png)
Evidência 7: Desafio - Execução
![Evidência 7](./Evidencias/desafio-execucao.png)
Evidência 8: Desafio - S3
![Evidência 8](./Evidencias/desafio-S3.png)

# Certificados

- Certificado do Curso Noções básicas de Analytics na AWS – Parte 1
  ![Certificado](./Certificados/analytics1.pdf)

- Certificado do Curso Noções básicas de Analytics na AWS – Parte 2
  ![Certificado](./Certificados/analytics2.pdf)

- Certificado do Curso Introduction to Amazon Athena
  ![Certificado](./Certificados/intro-athena.pdf)

- Certificado do Curso Amazon Redshift Getting Started
  ![Certificado](./Certificados/intro-redshift.pdf)

- Certificado do Curso AWS Glue Getting Started
  ![Certificado](./Certificados/intro-glue.pdf)

- Certificado do Curso Amazon EMR Getting Started
  ![Certificado](./Certificados/intro-emr.pdf)

- Certificado do Curso Serverless Analytics
  ![Certificado](./Certificados/serverless.pdf)

- Certificado do Curso Best Practices for Data Warehousing with Amazon Redshift
  ![Certificado](./Certificados/best-practices-redshift.pdf)

- Certificado do Curso QuickSight Getting Started
  ![Certificado](./Certificados/intro-quicksight.pdf)
