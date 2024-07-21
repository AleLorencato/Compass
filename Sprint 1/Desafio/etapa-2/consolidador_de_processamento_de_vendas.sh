DIR_BACKUP="/home/alelorencato/ecommerce/vendas/backup"
ARQUIVO_FINAL="$DIR_BACKUP/relatorio_final.txt"

echo "Relatorio Final" > $ARQUIVO_FINAL

for relatorio in $DIR_BACKUP/relatorio*.txt; do
    echo "" >> $ARQUIVO_FINAL
    echo "Conteúdo do $relatorio:" >> $ARQUIVO_FINAL
    cat $relatorio >> $ARQUIVO_FINAL
done

echo "Consolidação completa. Relatório final salvo em $ARQUIVO_FINAL"
