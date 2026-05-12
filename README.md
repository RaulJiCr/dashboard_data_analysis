# Curso express: analisis de datos y dashboards

Esta carpeta contiene materiales para convertir los dashboards existentes en un curso reutilizable:

1. `manual_profesores.md`: guia docente para conducir el curso desde la pregunta analitica hasta el dashboard.
2. `manual_uso_plantilla_estudiantes.md`: manual paso a paso para estudiantes sin experiencia programando.
3. `guia_color_visualizacion_datos.md`: guia de teoria del color aplicada a dashboards y presentacion de datos.
4. `plantilla_dashboard/`: esqueleto Streamlit documentado para que los estudiantes creen su propio dashboard con un CSV.

La plantilla no depende del tema de criminalidad. Usa un dataset academico de ejemplo y acepta cualquier CSV con variables numericas, categoricas y, opcionalmente, fechas.

## Estructura

```text
curso_analisis_datos_dashboard/
├── guia_color_visualizacion_datos.md
├── manual_uso_plantilla_estudiantes.md
├── manual_profesores.md
└── plantilla_dashboard/
    ├── README.md
    ├── app.py
    ├── analytics.py
    ├── config.py
    ├── data_loader.py
    ├── visualizations.py
    ├── requirements.txt
    ├── .streamlit/config.toml
    └── data/ejemplo_estudiantes.csv
```

## Uso rapido de la plantilla

```bash
cd curso_analisis_datos_dashboard/plantilla_dashboard
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Ruta sugerida de lectura

Para profesores:

1. Leer `manual_profesores.md`.
2. Revisar `guia_color_visualizacion_datos.md` antes de la seccion de dashboard.
3. Usar `manual_uso_plantilla_estudiantes.md` como material de apoyo para la sesion practica.

Para estudiantes:

1. Leer `manual_uso_plantilla_estudiantes.md`.
2. Ejecutar `plantilla_dashboard/`.
3. Consultar `guia_color_visualizacion_datos.md` antes de preparar la entrega final.

## Adaptacion recomendada para clase

- Cambiar el archivo `data/ejemplo_estudiantes.csv` por el CSV del equipo.
- Ajustar titulos, colores y texto base en `config.py`.
- Modificar o agregar graficas en `visualizations.py`.
- Mantener la logica analitica en `analytics.py` para que la app no se vuelva dificil de leer.
- Pedir que cada equipo documente sus decisiones en una bitacora: pregunta, variables usadas, limpieza, features creadas, modelo, interpretacion y limitaciones.
- Pedir que justifiquen su paleta de color: que significa cada color y por que ayuda a interpretar.
