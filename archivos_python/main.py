from auth import sesionAdmin
from visitors import menuVisitantes

def salir():
    while True:
        opcion = input("\n\033[32m¿Seguro deseas salir del programa? si / no: \033[0m").strip().lower()
        if opcion == "si":
            print("\033[33mSaliste del programa.\033[0m")
            return True 
        elif opcion == "no":
            print("\033[33mVolviste al menú.\033[0m")
            return False
        else:
            print("\033[31mRespuesta inválida. Escribe si/no.\033[0m")

def main():
    print("\nSistema iniciado correctamente.")
    sesionAdmin()


def menu():
    while True:
        print("\n\033[46m---- MENU PRINCIPAL ----\033[0m")
        print("\n1. Visitantes Intergalácticos")
        print("2. Artefactos Recuperados")
        print("3. salir del sistema")
        
        opcion = input("\nSeleccione una opción: ")
        print()
    # Opciones donde se llaman las funciones
        match opcion:
            case "1":
                menuVisitantes()
                print("mantenimiento")
            case "2":
                #menuArtefactos()
                print("mantenimiento")
            case "3":
                if salir():
                    break
            case _:
                print("\033[31mOpción inválida.\n\033[0m")
    
   
if __name__ == "__main__":
    main()
    menu()
