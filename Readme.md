# Aplicaciones a instalar: 
Visual Studio
Git (desde https://git-scm.com/downloads/win)
Python (descargue en la página la version 3.10.10)
AWS CLI (desde https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

# Instalaciones requeridas:
pandas (pip install pandas)
boto3 (pip install boto3)

# Permisos para rol IAM
AmazonRedshiftAllCommandsFullAccess
AWSGlueConsoleFullAccess
AWSGlueServiceRole
CloudWatchLogsFullAccess

# Configuracion de politica del bucket (necesario para que se cree la tabla despues del crawler)
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::992382691114:role/rol_romi_glue" #tener en cuenta que esto cambia por el rol y usuario utilizado
      },
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::telecom-datalake-1/data/*" #le agregue el "-1" debido a que me figuraba que el bucket "telecom-datalake" ya estaba creado
    }
  ]
}

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

# Notas:
# 1)
Antes de ejecutar el crawler, se deben agregar al bucket las politicas y, despues seleccionar la ruta del archivo csv sin ningun signo al final(es decir termina en "csv") 
# 2)
Debido a las limitaciones de los usuarios brindados por la academia, permite crear e el cruster, pero no se puede continuar trabajando con Redshift. 
A su vez, el ultimo usuario no tenia acceso a Glue, por lo que no me permite trabajar en Redsfhit y Athena. Por ende, no puedo verificar la automatizacion (usando Step Funcions), pero se realizo un trabajo aproximado de la ejecucion. 