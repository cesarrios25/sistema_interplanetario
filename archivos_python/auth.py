import csv



# Carga al administrador desde el CSV.
def cargarAdmin():
    with open("archivos_CSV/admin_access.csv", "r", encoding="utf-8") as archivo:
        reader = csv.DictReader(archivo)
        for row in reader:
            return row 
        
# Inicio de sesion validando credenciales con el csv
def sesionAdmin(intentos = 3):
    # Llamo la funcion cargar admin que es la del csv
    admin = cargarAdmin()
    # Intentos de inicio de sesion
    if intentos <= 0:
        print("Has agotado tus intentos")
        exit()
    
    
    print("\n--- PANEL DE INICIO DE SESION ---")
    usuario = input("Ingrese su usuario: ").lower()
    contrasena = input("Ingrese su contraseña: ")
    # Valido credenciales
    if usuario == admin["usuario"] and contrasena == admin["contrasena"]:
        print("\nSUPERADMIN, Bienvenido al sistema")
        return True
    
    print(f"\nCredenciales incorrectas. Te quedan {intentos - 1} intentos.")
    return sesionAdmin(intentos - 1)

