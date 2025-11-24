import csv
import json

# Archivos csv
# Archivo JSON donde me guarda todo como copia
archivo = "archivos_CSV/visitantes.csv"
archivo2 = "archivos_JSON/sistemaModerno.json"



# Cargar visitantes del CSV
def cargarVisitantes():
    visitantes = []
    try:
        with open(archivo, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                visitantes.append(row)
    except FileNotFoundError:
        pass
    return visitantes

# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

# Guardar visitantes al CSV
def guardarVisitantes(visitantes):
    with open(archivo, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["ID", "Nombre", "Especie", "Estado"])
        writer.writeheader()
        writer.writerows(visitantes)
# Guarda tambien en el archivo JSON
    guardarJSON(visitantes) 
                
# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

# Guarda visitantes al JSON
def guardarJSON(visitantes):
    with open(archivo2, "w", encoding="utf-8") as abrir:
        json.dump(visitantes, abrir, indent=4, ensure_ascii=False)