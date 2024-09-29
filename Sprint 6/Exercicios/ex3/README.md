## Descrição do Exercício 3 - Lab AWS Lambda

Neste exercício, foi criada uma função lambda que lê um arquivo CSV do S3 e retorna quantas linhas tem.
Utilizei o docker para criar a layer com o pandas para o exercício. Foi necessário utilizar o python 3.8 ao invés do 3.7, pois na AWS, a versão 3.7 não está mais disponível e a 3.8 é a mais próxima.
Também tive que modificar o código para adicionar o numpy, tanto no dockerfile quanto no código da lambda function.

Etapas:

- Criar uma função Lambda do zero
- Criar uma layer com as dependências necessárias
- Executar o código
