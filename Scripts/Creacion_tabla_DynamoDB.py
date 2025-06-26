import boto3
from datetime import datetime

# Inicializar el recurso de DynamoDB
dynamodb = boto3.resource('dynamodb')

# Referencia a la tabla
table = dynamodb.Table('pipeline-config')

# Insertar un ítem en la tabla con manejo de errores
try:
    response = table.put_item(
        Item={
            'id_pipeline': 'pipeline_001',
            'status': 'Success',
            'timestamp': datetime.utcnow().isoformat()
        }
    )
    print("Log registrado con éxito:", response)
except Exception as e:
    print("Error al registrar el log:", str(e))
