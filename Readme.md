# Aplicaciones a instalar: 
Visual Studio
Git (desde https://git-scm.com/downloads/win)
Python (descargue en la página la version 3.10.10)
AWS CLI (desde https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

# Instalaciones requeridas:
pandas (pip install pandas)
boto3 (pip install boto3)

# Conexion entre Visual Studio y AWS:
aws configure

# Conexion entre Visual Studio y S3:
# a) Creacion de bucket:
aws s3 mb s3://telecom-datalake-1
# b) Creacion de carpeta dentro del bucket:
aws s3api put-object --bucket telecom-datalake-1 --key data/
# c) Carga de archivos a S3:
aws s3 cp clientes.csv s3://telecom-datalake-1/data/
# d) Verificaciones de carga en S3:
aws s3 ls s3://telecom-datalake-1/data/ #Creacion de carpeta
#aws s3 ls s3://telecom-datalake-1/scripts/ #Cargo los datos transformados

# Conexion entre Visual Studio y AWS Glue:
# a)Verificar la creacion y estado del crawler desde Visual Studio: 
aws glue get-crawler --name crawler_rol_romi_glue
# b)Cargar un archivo .py a S3:
aws s3 cp C:\Users\PC\Desktop\Proyecto_5_2025\Scripts\ETL_en_Glue.py s3://telecom-datalake-1/scripts/

# Conexion entre Visual Studio y un repositorio en GitHub:
git init
git add .
git commit -m "Iniciando proyecto en GitHub"

# Nota:
Cuando se intente crear el crawler, primero se tienen que cambiar las politicas del bucket y despues se selecciona la ruta del archivo csv pero al final no se pone nada (ningun . ni /, es decir termina en csv) 