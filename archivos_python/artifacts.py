from storage import cargarArtefactos, guardarArtefactos

def menuArtefactos():
    while True:
        print("\n\033[46m---- MENU ARTEFACTOS ----\033[0m")
        print("\n1. Registrar artefacto")
        print("2. Listar artefactos")
        print("3. Buscar artefacto")
        print("4. Clasificar artefactos por rareza")
        print("5. Eliminar artefacto")
        print("6. Mostrar estadísticas")
        print("7. Regresar al Menú Principal")
        
        opcion = input("\n\033[32mSeleccione una opción: \033[0m")
        print()

        match opcion:
            case "1":
                registrarArtefactos()
            case "2":
                listarArtefactos()
            case "3":
                buscarArtefactos()
            case "4":
                clasificarArtefactos()
            case "5":
                eliminarArtefacto()
            case "6":
                estadisticas()
            case "7":
                return
            case _:
                print("\033[31mOpción inválida.\033[0m")
                
# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

# Generar ID único
def generarID(artefactos):
    if not artefactos:
        return 1
    ids = {int(a["ID"]) for a in artefactos}
    return max(ids) + 1

# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

# Registrar artefacto
def registrarArtefactos():
    while True:
        artefactos = cargarArtefactos()

        print("\n--- REGISTRO DE ARTEFACTOS ---")
        descripcion = input("\n\033[32mDescripción: \033[0m").lower()
        nivelRareza = input("\033[32mRareza bajo / medio / alto / prohibido: \033[0m").lower()
        estatus = input("\033[32mEstatus almacenado / en estudio / destruido: \033[0m").lower()

        nuevoID = generarID(artefactos)

        artefacto = {
            "ID": str(nuevoID),
            "Descripcion": descripcion,
            "Rareza": nivelRareza,
            "Estatus": estatus
        }

        artefactos.append(artefacto)
        guardarArtefactos(artefactos)

        print("\n\033[33mArtefacto guardado exitosamente.\033[0m")

        if input("\n\033[32m¿Registrar otro? si / no: \033[0m").lower() != "si":
            break

# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

# Listar artefactos
def listarArtefactos():
    artefactos = cargarArtefactos()

    if not artefactos:
        print("\n\033[31mNo hay artefactos registrados.\033[0m")
        return

    print("\n\033[42m---- LISTA DE ARTEFACTOS ----\033[0m")
    print()
    for art in artefactos:
        print(tuple(art.values()))


# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

# Buscar artefactos
def buscarArtefactos():
    while True:
        artefactos = cargarArtefactos()

        if not artefactos:
            print("\n\033[31mNo hay artefactos registrados.\033[0m")
            return

        artefactoID = input("\n\033[32mIngrese el ID del artefacto: \033[0m").strip()

        encontrado = next((a for a in artefactos if a["ID"] == artefactoID), None)

        if encontrado:
            print("\n\033[33mArtefacto encontrado:\033[0m")
            print(f"ID: {encontrado['ID']}")
            print(f"Descripción: {encontrado['Descripcion']}")
            print(f"Rareza: {encontrado['Rareza']}")
            print(f"Estatus: {encontrado['Estatus']}\n")
        else:
            print("\033[31mArtefacto no encontrado.\033[0m\n")

        if input("\n\033[32m¿Buscar otro? si / no: \033[0m").lower() != "si":
            break

# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

# Clasificar artefactos por rareza (usa kwargs)
def clasificarArtefactos(**kwargs):
    artefactos = cargarArtefactos()

    if not artefactos:
        print("\033[31mNo hay artefactos registrados.\033[0m")
        return

    # Tomar rareza y estatus enviados por kwargs (si los hay)
    rarezaBuscada = kwargs.get("rareza", "").lower().strip()
    estatusBuscado = kwargs.get("estatus", "").lower().strip()

    # Si no llegaron valores por kwargs, pedirlos al usuario
    if not rarezaBuscada and not estatusBuscado:
        rarezaBuscada = input("\n\033[32mFiltrar rareza bajo/medio / alto / prohibido o Enter para todos: \033[0m").lower().strip()
        estatusBuscado = input("\033[32mFiltrar estatus almacenado / en estudio / destruido o Enter para todos: \033[0m").lower().strip()

    nivelesValidos = ["bajo", "medio", "alto", "prohibido"]

    # Validación de rareza si se ingresó
    if rarezaBuscada and rarezaBuscada not in nivelesValidos:
        print("\033[31mRareza inválida.\033[0m")
        return

    print("\n\033[33m--- ARTEFACTOS CLASIFICADOS ---\033[0m\n")
    print()
    filtrados = [
        art for art in artefactos
        if (not rarezaBuscada or art["Rareza"].lower() == rarezaBuscada)
        and (not estatusBuscado or art["Estatus"].lower() == estatusBuscado)
    ]

    if not filtrados:
        print("\033[31mNo se encontraron artefactos con esos criterios.\033[0m")
        return

    for art in filtrados:
        print(f"ID: {art['ID']}")
        print(f"Descripción: {art['Descripcion']}")
        print(f"Rareza: {art['Rareza']}")
        print(f"Estatus: {art['Estatus']}")
        print("-" * 40)

    print("\n\033[32mClasificación completa.\033[0m")
    
    
# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

# Elimnar artefactos
def eliminarArtefacto():
    while True:
        artefactos = cargarArtefactos()

        if not artefactos:
            print("\033[31mNo hay artefactos registrados.\033[0m")
            return

        eliminarArtefacto = input("\n\033[32mIngrese el ID del artefacto a eliminar: \033[0m").strip()

        # Buscamos el artefacto
        artefacto = None
        for artefacto in artefactos:
            if artefacto["ID"] == eliminarArtefacto:
                artefacto = artefacto
                break


        if artefacto:
            print("\n\033[33martefacto encontrado: \033[0m")
            print(f"ID: {artefacto['ID']}")
            print(f"Descripcion: {artefacto['Descripcion']}")
            print(f"Rareza: {artefacto['Rareza']}")
            print(f"Estatus: {artefacto['Estatus']}")

            # Elegir opción de eliminación
            opcion = input("\n\033[32mOpción A: eliminar fila / Opción B: marcar 'Eliminado'. Ingrese a / b: \033[0m").strip().lower()

            if opcion == "a":
                artefactos.remove(artefacto)
                print("\033[33mArtefacto eliminado completamente.\033[0m\n")
            elif opcion == "b":
                artefacto["Estado"] = "Eliminado"
                print("\033[33mArtefacto marcado como 'Eliminado'.\033[0m\n")
            else:
                print("\033[31mOpción inválida.\033[0m\n")
                continue

            # Guardamos los cambios en el CSV
            guardarArtefactos(artefactos)

        else:
            print("\033[31mVisitante no encontrado.\033[0m\n")

        # Preguntar si desea eliminar otro visitante
        opcion_continuar = input("\033[32m¿Deseas eliminar otro artefacto? si / no: \033[0m").strip().lower()
        if opcion_continuar != "si":
            print("Saliste al menú.\n")
            break

# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

# Estadísticas de los visitantes
def estadisticas():
    artefactos = cargarArtefactos()

    if not artefactos:
        print("\033[31mNo hay artefactos registrados.\033[0m")
        return

    print("\n\033[46m---- ESTADÍSTICAS DE LOS ARTEFACTOS ----\033[0m\n")

    # Total de artefactos
    totalArtefactos = len(artefactos)

    # Contar artefactos por Rareza
    rarezaCantidad = {}     
    estatusSet = set() 

    for artefacto in artefactos:
        rareza = artefacto["Rareza"]
        estatus = artefacto["Estatus"]

        # Contar rareza
        if rareza not in rarezaCantidad:
            rarezaCantidad[rareza] = 1
        else:
            rarezaCantidad[rareza] += 1

        # Guardar estatus únicos
        estatusSet.add(estatus)

    # Contar cantidad por estatus
    estatusCantidad = {}
    for artefacto in artefactos:
        estatus = artefacto["Estatus"].capitalize()
        if estatus not in estatusCantidad:
            estatusCantidad[estatus] = 1
        else:
            estatusCantidad[estatus] += 1

    # ----------------------------------------
    # PRESENTACIÓN DE RESULTADOS
    print(f"Total de artefactos registrados: {totalArtefactos}\n")

    print("Artefactos por nivel de rareza:")
    for rareza, cantidad in rarezaCantidad.items():
        print(f" - {rareza}: {cantidad}")

    print("\nArtefactos por estatus:")
    for estatus, cantidad in estatusCantidad.items():
        print(f" - {estatus}: {cantidad}")

    print("\nListado de estatus detectados (SET):")
    print(estatusSet)

    print("\n----------------------------------------\n")
