# Plantilla Streamlit para estudiantes

Esta plantilla permite construir un dashboard de analisis de datos sin partir de cero. Esta organizada por modulos para que cada equipo pueda modificar una parte concreta sin perderse en todo el codigo.

## Archivos principales

- `app.py`: interfaz principal de Streamlit.
- `config.py`: titulos, colores y ruta del dataset de ejemplo.
- `data_loader.py`: carga CSV, limpia nombres de columnas y detecta tipos de datos.
- `analytics.py`: estadistica descriptiva, feature engineering, modelo supervisado y clustering.
- `visualizations.py`: graficas reutilizables.
- `data/ejemplo_estudiantes.csv`: dataset pequeno para practicar.

## Como correr la app

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Como adaptar la plantilla

1. Colocar el CSV del equipo en la carpeta `data/`.
2. Cambiar `DEFAULT_DATA_PATH` en `config.py`.
3. Ejecutar la app y revisar la pestana `Datos`.
4. Elegir variables numericas y categoricas en `Estadistica`.
5. Crear features de fecha en `Feature engineering` si el dataset tiene fechas.
6. Entrenar un modelo en `Modelo`.
7. Crear perfiles en `Clustering`.
8. Ajustar la vista `Dashboard` para contar la historia final.

## Reglas de trabajo recomendadas

- No borrar funciones que no se entienden; comentarlas o preguntar primero.
- Cambiar una cosa a la vez y volver a ejecutar la app.
- Guardar una bitacora con decisiones de limpieza, variables usadas y limitaciones.
- No afirmar causalidad si el analisis solo muestra asociacion.
