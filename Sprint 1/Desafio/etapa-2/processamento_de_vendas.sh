DATA=$(date +"%Y%m%d")
DIR_ECOMMERCE="/home/alelorencato/ecommerce"
cd $DIR_ECOMMERCE
DIR_VENDAS="$DIR_ECOMMERCE/vendas"
DIR_BACKUP="$DIR_VENDAS/backup"
DADOS="$DIR_ECOMMERCE/dados_de_vendas.csv"
DADOS_VENDAS="$DIR_VENDAS/dados_de_vendas.csv"
DADOS_BACKUP="$DIR_BACKUP/dados-$DATA.csv"
ARQUIVO_RELATORIO="$DIR_BACKUP/relatorio-$DATA.txt"
ARQUIVO_ZIP="$DIR_BACKUP/backup-dados-$DATA.zip"

mkdir -p $DIR_VENDAS
cp $DADOS $DADOS_VENDAS

mkdir -p $DIR_BACKUP
cp $DADOS_VENDAS $DADOS_BACKUP

DATA_SISTEMA=$(date +"%Y/%m/%d %H:%M")
DATA_PRIMEIRO=$(awk -F, 'NR==2 {print $5}' $DADOS_BACKUP)
DATA_ULTIMO=$(awk -F, 'END {print $5}' $DADOS_BACKUP)
QTDE_ITENS=$(awk -F, 'NR>1 {print $2}' $DADOS_BACKUP | sort | uniq | wc -l)


echo "Data do sistema operacional: $DATA_SISTEMA" > $ARQUIVO_RELATORIO
echo "Data do primeiro registro de venda: $DATA_PRIMEIRO" >> $ARQUIVO_RELATORIO
echo "Data do ultimo registro de venda: $DATA_ULTIMO" >> $ARQUIVO_RELATORIO
echo "Quantidade total de itens diferentes vendidos: $QTDE_ITENS" >> $ARQUIVO_RELATORIO

echo "" >> $ARQUIVO_RELATORIO
echo "Primeiras 10 linhas do arquivo de backup:" >> $ARQUIVO_RELATORIO
head -n 10 $DADOS_BACKUP >> $ARQUIVO_RELATORIO

zip $ARQUIVO_ZIP $DADOS_BACKUP

rm $DADOS_BACKUP
rm $DADOS_VENDAS
