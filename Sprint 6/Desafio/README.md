# Desafio Sprint 6

## Descrição

Nessa parte do desafio consiste em criar um script Python com boto3 que faça a leitura de um arquivo CSV e envie esses dados para um bucket S3 na AWS.

## TUTORIAL PARA A EXECUÇÃO DO DESAFIO

### Pré-requisitos

- dotenv
- Docker

### Passo a passo

1. Clone o repositório e acesse a pasta do projeto

2. Insira os arquivos CSV "movies.csv" e "series.csv" na raiz do projeto

3. Crie um arquivo `.env` na raiz do projeto com as credenciais da AWS

4. Execute o comando abaixo para criar a imagem do Docker e executar o container

```bash
docker build -t nome-da-imagem .
docker run --env-file .env nome-da-imagem
```
