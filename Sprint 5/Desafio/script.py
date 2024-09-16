import boto3
import os
from dotenv import load_dotenv

load_dotenv()


AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_SESSION_TOKEN = os.getenv("AWS_SESSION_TOKEN")

Bucketname = "bucket-desafio-sprint5"
Key = 'maquinas.csv'

client = boto3.client('s3', 
                      aws_access_key_id=AWS_ACCESS_KEY_ID,
                      aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                      aws_session_token=AWS_SESSION_TOKEN)


firstQuery = client.select_object_content(
    Bucket=Bucketname,
    Key=Key,
    ExpressionType='SQL',
    Expression="""SELECT SUM(CAST(s.Quantidade AS DECIMAL)) AS total_unidades, MAX(CHARACTER_LENGTH(s.DescrSint)) as mais_caracters FROM s3object s WHERE COALESCE(s.Historico) != 'Fiscal' AND s.Grupo = '05'""",
    InputSerialization={'CSV': {"FileHeaderInfo": "Use", "FieldDelimiter": ";", "AllowQuotedRecordDelimiter": True}},
    OutputSerialization={'CSV': {}},
)

secondQuery = client.select_object_content(
    Bucket=Bucketname,
    Key=Key,
    ExpressionType='SQL',
    Expression="""SELECT s.DtAquisicao FROM s3object s WHERE TO_TIMESTAMP(SUBSTRING(s.DtAquisicao, 7) || 'T') < TO_TIMESTAMP('2012T')""",
    InputSerialization={'CSV': {"FileHeaderInfo": "Use", "FieldDelimiter": ";", "AllowQuotedRecordDelimiter": True}},
    OutputSerialization={'CSV': {}},
)


records = ""

for event in firstQuery['Payload']:
    if 'Records' in event:
        records += event['Records']['Payload'].decode('utf-8')

print(f"o total de unidades e o maior número de caracteres são: {records}")

records = ""

for event in secondQuery['Payload']:
    if 'Records' in event:
        records += event['Records']['Payload'].decode('utf-8')

print(f"as datas de aquisição menores que 2012 são: \n{records}")
