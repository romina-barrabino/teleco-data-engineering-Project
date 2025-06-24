import boto3
from datatime import datetime

dynamodb = boto3.resource ('dynamodb')
table = dynamodb.Table('pipeline-config')

table.put_item(
    Item={'id_pipeline':'pipeline_001',
          'status':'Success',
          'timestamp':datetime.utcnow().isoformat()
          }
)