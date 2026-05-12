"""Configuracion central de la plantilla.

Los estudiantes pueden empezar modificando este archivo. Mantener nombres,
colores y rutas aqui evita buscar valores sueltos dentro de toda la app.
"""

# Titulo principal que se muestra en Streamlit.
APP_TITLE = "Plantilla de dashboard para analisis de datos"

# Texto corto de contexto. Cambiarlo por el tema del proyecto del equipo.
APP_SUBTITLE = "Exploracion, modelo supervisado, clustering y visualizacion ejecutiva"

# Dataset de demostracion. La app tambien permite cargar un CSV desde la barra lateral.
DEFAULT_DATA_PATH = "data/ejemplo_estudiantes.csv"

# Colores base usados por las graficas.
COLOR_PRIMARY = "#2563eb"
COLOR_SECONDARY = "#16a34a"
COLOR_WARNING = "#f59e0b"
COLOR_DANGER = "#dc2626"
COLOR_NEUTRAL = "#64748b"

# Numero maximo de filas que se muestran en la vista previa para no saturar la pantalla.
PREVIEW_ROWS = 20

# Semilla fija: ayuda a que los modelos den resultados reproducibles en clase.
RANDOM_STATE = 42
