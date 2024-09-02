# Desafio - Sprint 3

Abaixo seguem todos os links dos entregáveis solicitados:

## Etapas

1. Etapa I -

- [Arquivo Python](./etapa1/carguru.py)
- [Dockerfile](./etapa1/dockerfile)

2. Etapa II -

- [Arquivo Markdown](./etapa2/README.md)

3 - Etapa III -

- [Arquivo Python](./etapa3/mascarar_dados.py)
- [Dockerfile](./etapa3/dockerfile)

## Passo a Passo para execução do código

1. Etapa I -

- Primeiramente, é necessário construir a imagem do Docker. Para isso, execute o comando abaixo:

```bash
docker build -t carguru-image .
```

- Em seguida, execute o comando abaixo para rodar o container:

```bash
docker run -it carguru-image
```

2. Etapa III -

- Primeiramente, é necessário construir a imagem do Docker. Para isso, execute o comando abaixo:

```bash
docker build -t mascarar-dados .
```

- Em seguida, execute o comando abaixo para rodar o container:

```bash
docker run -it mascarar-dados
```
