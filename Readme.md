# Aplicaciones a instalar: 
SQL Microsoft Server (creo en ella una base de datos que llamo "Empleados")
Visual Studio
Git (desde https://git-scm.com/downloads/win)
Python (descargue en la página la version 3.10.10)
AWS CLI (desde https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

# Instalaciones requeridas:
pandas (pip install pandas)
boto3 (pip install boto3)
#pyodc (pip install pyodbc)

# Conexion entre Visual Studio y AWS:
aws configure

# Conexion entre Visual Studio y S3 (Creacion de bucket,creacion de carpeta, carga de archivos y verificacion de carga):
aws s3 mb s3://telecom-datalake
aws s3api put-object --bucket telecom-datalake --key data/
aws s3 cp clientes.csv s3://telecom-datalake/data/
aws s3 ls s3://telecom-datalake/data/

# Conexion entre Visual Studio y AWS Glue:
# a)Verificar la creacion y estado del crawler desde Visual Studio: 
aws glue get-crawler --name crawler_rol_romi_IAM
# b)Cargar un archivo .py a S3:
aws s3 cp C:\Users\PC\Desktop\Proyecto_5_2025\Scripts\ETL_en_Glue.py s3://telecom-datalake/scripts/

# Conexion entre Visual Studio y un repositorio en GitHub:
git init
git add .
git commit -m "Iniciando proyecto en GitHub"