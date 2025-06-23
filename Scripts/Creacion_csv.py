import csv

clientes = [
    ["id_cliente", "nombre_cliente", "plan", "fecha_inicio", "fecha_fin", "monto"],
    [1, "Cliente A", "Plan Básico", "2024-01-01", "2024-12-31", 25],
    [2, "Cliente B", "Plan Premium", "2024-02-01", "2024-12-31", 50]
]

#Creo un archivo CSV llamado clientes.csv
with open("clientes.csv", "w", newline="", encoding="utf-8") as archivo:
    writer = csv.writer(archivo)
    writer.writerows(clientes)

print("Archivo 'clientes.csv' creado con éxito.")
