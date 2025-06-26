#No se pudo ejecutar por falta de permisos del usuario
{
  "Comment": "Pipeline: ejecutar Glue Job ETL → cargar a Redshift → consultar Athena → log DynamoDB",
  "StartAt": "Ejecutar Glue Job ETL",
  "States": {
    "Ejecutar Glue Job ETL": {
      "Type": "Task",
      "Resource": "arn:aws:states:::glue:startJobRun.sync",
      "Parameters": {
        "JobName": "glue_etl_clientes"
      },
      "Next": "Cargar datos a Redshift"
    },
    "Cargar datos a Redshift": {
      "Type": "Task",
      "Resource": "arn:aws:states:::lambda:invoke",
      "Parameters": {
        "FunctionName": "lambda-cargar-redshift",
        "Payload": {
          "s3_path": "s3://telecom-datalake-1/output/clientes_transformados.csv"
        }
      },
      "Next": "Ejecutar consulta en Athena"
    },
    "Ejecutar consulta en Athena": {
      "Type": "Task",
      "Resource": "arn:aws:states:::lambda:invoke",
      "Parameters": {
        "FunctionName": "lambda-consulta-athena",
        "Payload": {
          "query": "SELECT * FROM glue_data.clientes LIMIT 10"
        }
      },
      "Next": "Registrar Log en DynamoDB"
    },
    "Registrar Log en DynamoDB": {
      "Type": "Task",
      "Resource": "arn:aws:states:::lambda:invoke",
      "Parameters": {
        "FunctionName": "lambda-registrar-log",
        "Payload": {
          "status": "SUCCESS",
          "etapa": "Pipeline completo ejecutado",
          "archivo": "s3://telecom-datalake-1/scripts/ETL_en_Glue.py",
          "timestamp.$": "$$.State.EnteredTime"
        }
      },
      "End": true
    }
  }
}