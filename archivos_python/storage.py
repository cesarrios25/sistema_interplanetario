import csv
import json

# Archivos csv
# Archivo JSON donde me guarda todo como copia
archivo = "archivos_CSV/visitantes.csv"
archivo3 = "archivos_CSV/artefactos.csv"
archivo2 = "archivos_JSON/sistemaModerno.json"
archivo4 = "archivos_JSON/sistemaModerno2.json"

# -----------------------------------------------------------------------------------------------
# SISTEMA VISITANTES INTERGALACTICOS
# -----------------------------------------------------------------------------------------------

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
        

# -----------------------------------------------------------------------------------------------
# SISTEMA ARTEFACTOS RECUPERADOS
# -----------------------------------------------------------------------------------------------

# Cargar artefactos del CSV
def cargarArtefactos():
    artefactos = []
    try:
        with open(archivo3, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                artefactos.append(row)
    except FileNotFoundError:
        pass
    return artefactos

# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

# # Guardar visitantes al CSV
def guardarArtefactos(artefactos):
    with open(archivo3, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["ID", "Descripcion", "Rareza", "Estatus"])
        writer.writeheader()
        writer.writerows(artefactos)
# Guarda tambien en el archivo JSON
    guardarJSON(artefactos) 
                
# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

# # Guarda visitantes al JSON
def guardarJSON(artefactos):
    with open(archivo4, "w", encoding="utf-8") as abrir:
        json.dump(artefactos, abrir, indent=4, ensure_ascii=False)
        