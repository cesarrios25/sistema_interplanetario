from storage import cargarVisitantes, guardarVisitantes

def menuVisitantes():
    while True:
        print("\n\033[46m---- MENU PRINCIPAL ----\033[0m")
        print("\n1. Registrar Visitantes")
        print("2. Listar visitantes")
        print("3. Buscar visitante por ID")
        print("4. Actualizar estado")
        print("5. Eliminar visitante")
        print("6. Estadísticas")
        print("7. Regresar al Menu Principal")
        
        opcion = input("\nSeleccione una opción: ")
        print()
    # Opciones donde se llaman las funciones
        match opcion:
            case "1":
                registrarVisitante()
            case "2":
                listarVisitantes()
            case "3":
                buscarVisitante()
                print("mantenimiento")
            case "4":
                actualizarEstado()
            case "5":
                eliminarVisitante()
            case "6":
                estadisticas()
            case "7":
                regresarMenu()
            case _:
                print("\033[31mOpción inválida.\n\033[0m")

# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

# # funcion para generar id unicos y asi evitar repetir o duplicar ids
def generarID(visitantes):
    if not visitantes:
        return 1
    ids = {int(v["ID"]) for v in visitantes}
    return max(ids) + 1

# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

# crear nuevos registro  
def registrarVisitante():
    while True:
        visitantes = cargarVisitantes()

        print("\n--- REGISTRO DE VISITANTE ---")
        nombre = input("\n\033[32mIngrese Nombre: \033[0m")
        especie = input("\033[32mIngrese Especie: \033[0m")
        estado = input("\033[32mIngrese Estado Activo / Retirado: \033[0m")

# Genero automaticamente el id
        nuevoID = generarID(visitantes)

        visitante = {
            "ID": str(nuevoID),
            "Nombre": nombre,
            "Especie": especie,
            "Estado": estado
        }

        visitantes.append(visitante)
        guardarVisitantes(visitantes)

        print("\n\033[33mVisitante guardado exitosamente.\033[0m")

        opcion = input("\033[32m¿Deseas registrar otro visitante? si / no: \033[0m").lower()
        if opcion != "si":
            print("\033[33mRegresando al menú...\033[0m")
            break


# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

# Leer registros guardados
def listarVisitantes():
    visitantes = cargarVisitantes()
# Validar si hay o no visitantes registrados
    if not visitantes:
        print("\nNo hay visitantes registrados.")
        return

    print("\n\033[42m---- LISTA DE VISITANTES ----\033[0m")
    print()
    for visitante in visitantes:
# Mostrar cada visitante como tupla (ID, Nombre, Especie, Estado)
        print(tuple(visitante.values()))
        
# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

# Buscar visitante por ID
def buscarVisitante():
    while True:
        visitantes = cargarVisitantes()

        if not visitantes:
            print("\033[31mNo hay visitantes guardados.\033[0m\n")
            return None

        visitanteID = input("\n\033[32mIngrese el ID del visitante a buscar: \033[0m").strip()

        # Buscamos en la lista
        encontrado = False
        for visitante in visitantes:
            if visitante["ID"] == visitanteID:
                print("\nVisitante encontrado:")
                print(f"ID: {visitante['ID']}")
                print(f"Nombre: {visitante['Nombre']}")
                print(f"Especie: {visitante['Especie']}")
                print(f"Estado: {visitante['Estado']}\n")
                encontrado = True
                break

        if not encontrado:
            print("\033[31mVisitante no encontrado.\033[0m\n")

        opcion = input("\033[32m¿Deseas hacer una nueva búsqueda? si / no: \033[0m").strip().lower()
        if opcion != "si":
            print("Saliste al menú.\n")
            break

# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

# Actualizar estado
def actualizarEstado():
    while True:
        visitantes = cargarVisitantes()
        
        if not visitantes:
            print("\033[31mNo hay datos para actualizar.\033[0m\n")
            return None
        
        actualizarVisitante = input("\n\033[32mIngrese el ID del visitante a actualizar: \033[0m").strip()
        
        # Obtenemos la informacion de los visitantes y los mostramos
        encontrado = False
        for visitante in visitantes:
            if visitante["ID"] == actualizarVisitante:
                print("\n\033[33mVisitante encontrado: \033[0m")
                print(f"ID: {visitante['ID']}")
                print(f"Nombre actual: {visitante['Nombre']}")
                print(f"Especie actual: {visitante['Especie']}")
                print(f"Estado actual: {visitante['Estado']}")
                
                # Pedimos el nuevo estado y validamos que sea Activo o Retirado
                while True:
                    nuevoEstado = input("\n\033[32mIngrese el nuevo estado activo / retirado: \033[0m").strip().lower()
                    if nuevoEstado in ["activo", "retirado"]:
                        visitante["Estado"] = nuevoEstado
                        print("\033[32mEstado actualizado correctamente.\033[0m\n")
                        break
                    else:
                        print("\033[31mEstado inválido. Debe ser 'activo' o 'retirado'.\033[0m")

                encontrado = True
                break

        if not encontrado:
            print("\033[31mVisitante no encontrado.\033[0m\n")

        # Guardamos los cambios en el CSV
        guardarVisitantes(visitantes)

        # Preguntamos si desea actualizar otro visitante
        opcion = input("\033[32m¿Deseas actualizar otro visitante? si / no: \033[0m").strip().lower()
        if opcion != "si":
            print("Saliste al menú.\n")
            break

# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

# Eliminar Visitante
def eliminarVisitante():
    while True:
        visitantes = cargarVisitantes()

        if not visitantes:
            print("\033[31mNo hay datos para eliminar.\033[0m\n")
            return None

        eliminarRegistro = input("\n\033[32mIngrese el ID del visitante a eliminar: \033[0m").strip()

        # Buscamos el visitante
        visitante = None
        for visitante in visitantes:
            if visitante["ID"] == eliminarRegistro:
                visitante = visitante
                break


        if visitante:
            print("\n\033[33mVisitante encontrado: \033[0m")
            print(f"ID: {visitante['ID']}")
            print(f"Nombre: {visitante['Nombre']}")
            print(f"Especie: {visitante['Especie']}")
            print(f"Estado: {visitante['Estado']}")

            # Elegir opción de eliminación
            opcion = input("\033[32mOpción A: eliminar fila / Opción B: marcar 'Eliminado'. Ingrese a / b: \033[0m").strip().lower()

            if opcion == "a":
                visitantes.remove(visitante)
                print("\033[33mVisitante eliminado completamente.\033[0m\n")
            elif opcion == "b":
                visitante["Estado"] = "Eliminado"
                print("\033[33mVisitante marcado como 'Eliminado'.\033[0m\n")
            else:
                print("\033[31mOpción inválida.\033[0m\n")
                continue

            # Guardamos los cambios en el CSV
            guardarVisitantes(visitantes)

        else:
            print("\033[31mVisitante no encontrado.\033[0m\n")

        # Preguntar si desea eliminar otro visitante
        opcion_continuar = input("\033[32m¿Deseas eliminar otro visitante? si / no: \033[0m").strip().lower()
        if opcion_continuar != "si":
            print("Saliste al menú.\n")
            break

# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

# Estadísticas de los visitantes
def estadisticas():
    visitantes = cargarVisitantes()

    if not visitantes:
        print("\033[31mNo hay datos para mostrar.\033[0m\n")
        return None

    print("\n---- ESTADÍSTICAS DE LOS VISITANTES ----\n")

# Total de visitantes
    totalVisitantes = len(visitantes)

# Visitantes por especie (diccionario + set)
    especies = {}     
    especiesSet = set() 

    for visitante in visitantes:
        especie = visitante["Especie"]

        especiesSet.add(especie)

        if especie not in especies:
            especies[especie] = 1
        else:
            especies[especie] += 1

# Activos vs Retirados
    estadoCantidad = {
        "activo": 0,
        "retirado": 0,
        "Eliminado": 0  
    }

    for visitante in visitantes:
        estado = visitante["Estado"]
        if estado in estadoCantidad:
            estadoCantidad[estado] += 1

    # PRESENTACIÓN DE RESULTADOS
    print(f"Total de visitantes registrados: {totalVisitantes}\n")

    print("Visitantes por especie:")
    for especie, cantidad in especies.items():
        print(f" - {especie}: {cantidad}")

    print("\nEstados:")
    print(f" - Activos: {estadoCantidad['activo']}")
    print(f" - Retirados: {estadoCantidad['retirado']}")
    print(f" - Eliminados: {estadoCantidad['Eliminado']}")

    print("\nListado de especies detectadas (SET):")
    print(especiesSet)

    print("\n----------------------------------------\n")
    




    







        



































































# # ==========================
# # Listar Visitantes
# # ==========================
# def listar_visitantes():
#     visitantes, _ = cargar_visitantes()

#     if not visitantes:
#         print("No hay visitantes registrados.")
#         return

#     print("\n===== LISTA DE VISITANTES =====")
#     for v in visitantes:
#         print(tuple(v.values()))


# # ==========================
# # Buscar por ID
# # ==========================
# def buscar_por_id():
#     visitantes, _ = cargar_visitantes()
#     buscar = input("Ingrese el ID del visitante: ").strip()

#     for v in visitantes:
#         if v["ID"] == buscar:
#             print("Visitante encontrado:")
#             print(v)
#             return

#     print("❌ No existe un visitante con ese ID.")


# # ==========================
# # Actualizar Estado
# # ==========================
# def actualizar_estado():
#     visitantes, _ = cargar_visitantes()
#     buscar = input("ID del visitante a actualizar: ").strip()

#     for v in visitantes:
#         if v["ID"] == buscar:
#             v["Estado"] = "Retirado" if v["Estado"] == "Activo" else "Activo"
#             guardar_visitantes(visitantes)
#             print("✔ Estado actualizado.")
#             return

#     print("❌ No se encontró el ID.")


# # ==========================
# # Eliminar visitante
# # ==========================
# def eliminar_visitante(modo="marcar"):
#     visitantes, _ = cargar_visitantes()
#     buscar = input("ID del visitante a eliminar: ").strip()

#     for v in visitantes:
#         if v["ID"] == buscar:

#             if modo == "eliminar":
#                 visitantes.remove(v)
#             else:
#                 v["Estado"] = "Eliminado"

#             guardar_visitantes(visitantes)
#             print("✔ Visitante eliminado según el modo elegido.")
#             return

#     print("❌ No se encontró el visitante.")


# # ==========================
# # Estadísticas
# # ==========================
# def estadisticas():
#     visitantes, _ = cargar_visitantes()

#     total = len(visitantes)
#     especies = {}
#     estados = {"Activo": 0, "Retirado": 0, "Eliminado": 0}

#     for v in visitantes:
#         # contar especies
#         especies[v["Especie"]] = especies.get(v["Especie"], 0) + 1
#         # contar estados
#         if v["Estado"] in estados:
#             estados[v["Estado"]] += 1

#     print("\n===== ESTADÍSTICAS =====")
#     print(f"Total visitantes: {total}")
#     print(f"Visitantes por especie: {especies}")
#     print(f"Estados: {estados}")