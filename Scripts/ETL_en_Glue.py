# Extracción de datos:
import boto3
import pandas as pd
import io
import numpy as np
import os

#Determino los parámetros
bucket = 'telecom-datalake-1'
key = 'data/clientes.csv'
print ("Parametros definidos")

#Inicializacion de S3
print ("Iniciando conexion")
s3 = boto3.client('s3')
print ("Inicializacion con S3 exitosa")

#Descargar de la tabla csv
response = s3.get_object(Bucket=bucket, Key=key)
print ("Descarga completa")

#Leer el CSV en un DataFrame
df = pd.read_csv(io.BytesIO(response['Body'].read()))
print ("Se leyo la tabla correctamente")

#Mostrar los primeros registros (a modo de verificacion):
print ("Los primeros registros de la tabla son:")
print(df.head())

# Transformacion de datos:

#Reemplazo las celdas vacías o con espacios por NaN
print ("Iniciando procesos de transformacion")
df.replace(r'^\s*$', np.nan, regex=True, inplace=True)
print ("Se modificacion las celdas vacias o con espacios vacios")

#Elimino los espacios al principio y final de strings
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
print ("Se eliminaron espacios vacios en los strigs")

#Reemplazo el nombre del primer cliente
df.at[0, 'nombre_cliente'] = 'Carla Rodriguez'
print ("Se cambio el nombre del cliente correctamente")

print("Transformacion completada. Resultado:")
print(df)

# Carga de datos transformados a S3:

#Ruta del archivo a cargar
print ("Subiendo los datos transformados a S3")
local_file_path = r'C:\Users\PC\Desktop\Proyecto_5_2025\Scripts\ETL_en_Glue.py'
output_key = 'scripts/ETL_en_Glue.py'

#Subir el archivo
s3.upload_file(local_file_path, bucket, output_key)
print(f" Script subido correctamente a s3://{bucket}/{output_key}")
