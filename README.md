-- MENÚ PRINCIPAL
Al iniciar el sistema, se solicita inicio de sesión con usuario y contraseña.
Después de iniciar sesión correctamente, se muestra el menú principal con tres opciones:

1 - Visitantes Intergalácticos → abre el menú de visitantes
2 - Artefactos Recuperados → abre el menú de artefactos
3 - Salir del sistema → confirma antes de cerrar la aplicación

--- MÓDULO DE VISITANTES INTERGALÁCTICOS
Este módulo permite administrar los visitantes que llegan de otros planetas. Funcionalidades:

1 - Registrar visitante
    * Solicita nombre, especie y estado (Activo / Retirado)
    * Genera automáticamente un ID único
    * Guarda el registro en CSV y JSON
2 - Listar visitantes
    * Muestra todos los visitantes como tuplas (ID, Nombre, Especie, Estado)
3 - Buscar visitante por ID
    * Permite buscar un visitante específico por su ID
    * Muestra todos los datos del visitante
4 - Actualizar estado
    * Actualiza el estado del visitante (Activo o Retirado)
    * Guarda los cambios en CSV y JSON
5 - Eliminar visitante
    * Dos opciones: eliminar fila o marcar como "Eliminado"
    * Permite eliminar varios visitantes de forma consecutiva
6 - Estadísticas
    * Total de visitantes registrados
    * Distribución por especie
    * Cantidad de activos, retirados y eliminados
    * Listado de especies únicas (set)
7 - Regresar al menú principal

--- MÓDULO DE ARTEFACTOS RECUPERADOS
Este módulo gestiona artefactos encontrados en misiones espaciales. Funcionalidades:

1 - Registrar artefacto
    * Solicita descripción, nivel de rareza (bajo/medio/alto/prohibido) y estatus (almacenado/en estudio/destruido)
    * Genera ID único automáticamente
    * Guarda en CSV y JSON
2 - Listar artefactos
    * Muestra todos los artefactos como tuplas (ID, Descripción, Rareza, Estatus)
3 - Buscar artefacto por ID
    * Permite buscar artefactos específicos por su ID
    * Muestra toda la información del artefacto
4 - Clasificar artefactos por rareza y estatus
    * Filtra artefactos según rareza o estatus
    * Permite valores por defecto o entrada del usuario
5 - Eliminar artefacto
    * Dos opciones: eliminar fila o marcar como "Eliminado"
6 - Estadísticas
    * Total de artefactos registrados
    * Distribución por rareza
    * Distribución por estatus
    * Listado de estatus únicos (set)
7 - Regresar al menú principal

ESTRUCTURA DE ARCHIVOS
sistema_interplanetario/
│
├─ main.py                     # Archivo principal
├─ auth.py                     # Gestión de sesión de administrador
├─ visitors.py                 # Menú y CRUD de visitantes
├─ artifacts.py                # Menú y CRUD de artefactos
├─ storage.py                  # Funciones para cargar y guardar CSV/JSON
│
├─ archivos_CSV/
│   ├─ admin_access.csv        # Credenciales de administrador
│   ├─ visitantes.csv          # Registro de visitantes
│   └─ artefactos.csv          # Registro de artefactos
│
└─ archivos_JSON/
    ├─ sistemaModerno.json     # Respaldo de visitantes
    └─ sistemaModerno2.json    # Respaldo de artefactos