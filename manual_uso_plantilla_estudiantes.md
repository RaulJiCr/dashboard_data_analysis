# Manual para estudiantes: uso basico de la plantilla

## Para quien es este manual

Este manual esta pensado para estudiantes que no programan o que apenas estan empezando. La meta es que puedan usar la plantilla del dashboard sin entender todo el codigo desde el primer dia.

La regla principal es: no tienen que modificar todo. Solo deben cambiar las partes necesarias para adaptar el dashboard a sus datos.

## Que van a construir

Van a construir un dashboard con:

- carga de un archivo CSV;
- filtros basicos;
- indicadores principales;
- graficas descriptivas;
- creacion simple de variables de fecha;
- un modelo supervisado;
- clustering;
- una vista final tipo dashboard.

## Antes de empezar

Necesitan:

- una computadora con Python instalado;
- la carpeta `plantilla_dashboard`;
- un archivo CSV;
- una idea clara de que quieren analizar.

Si todavia no tienen datos, pueden usar el archivo:

```text
plantilla_dashboard/data/ejemplo_estudiantes.csv
```

## Como abrir la plantilla

### Paso 1. Abrir terminal

La terminal es una ventana donde escribimos instrucciones para la computadora.

En Mac:

```text
Aplicaciones > Utilidades > Terminal
```

En Windows:

```text
Buscar > PowerShell
```

### Paso 2. Entrar a la carpeta

Usar `cd` para entrar a la carpeta de la plantilla.

Ejemplo:

```bash
cd plantilla_dashboard
```

Si la carpeta esta dentro de otra, pueden arrastrar la carpeta a la terminal despues de escribir `cd `.

### Paso 3. Crear ambiente virtual

Un ambiente virtual guarda las librerias del proyecto sin mezclar todo con la computadora.

```bash
python -m venv .venv
```

### Paso 4. Activar el ambiente

En Mac:

```bash
source .venv/bin/activate
```

En Windows:

```powershell
.venv\Scripts\activate
```

Si funciono, normalmente aparece `(.venv)` al inicio de la linea.

### Paso 5. Instalar librerias

```bash
pip install -r requirements.txt
```

Esto instala Streamlit, pandas, scikit-learn y Plotly.

### Paso 6. Ejecutar la app

```bash
streamlit run app.py
```

Se abrira una pagina en el navegador. Si no se abre sola, copiar la liga que aparece, normalmente:

```text
http://localhost:8501
```

## Como usar la app sin tocar codigo

La app tiene una barra lateral y varias pestanas.

### Barra lateral

Sirve para:

- subir un CSV;
- aplicar un filtro global.

Si no suben CSV, la app usa el dataset de ejemplo.

### Pestana Datos

Sirve para revisar:

- numero de registros;
- numero de columnas;
- porcentaje de datos faltantes;
- primeras filas del dataset;
- tipos de columnas detectadas;
- columnas con valores faltantes.

Antes de hacer modelos, siempre revisar esta pestana.

### Pestana Estadistica

Sirve para explorar datos.

Pueden elegir:

- una variable numerica para ver histograma y boxplot;
- una variable categorica para ver conteos;
- correlaciones entre variables numericas.

Preguntas utiles:

- Que variable tiene valores muy altos o muy bajos?
- Hay grupos que aparecen mucho mas que otros?
- Hay variables numericas que se mueven juntas?

### Pestana Feature engineering

Sirve para crear variables nuevas a partir de fechas.

Si el dataset tiene una columna de fecha, la app puede crear:

- anio;
- mes;
- dia de semana.

Ejemplo:

```text
fecha_registro -> fecha_registro_anio, fecha_registro_mes, fecha_registro_dia_semana
```

Estas variables pueden ayudar a detectar patrones por temporada o dia.

### Pestana Modelo

Sirve para entrenar un modelo supervisado.

Pasos:

1. Elegir la variable objetivo.
2. Elegir variables predictoras.
3. Presionar `Entrenar modelo`.
4. Revisar metricas y variables importantes.

La variable objetivo es lo que quieren predecir.

Ejemplos:

- `aprobo`: si el estudiante aprobo o no;
- `calificacion_final`: estimar una calificacion;
- `ventas`: estimar ventas;
- `riesgo`: clasificar un nivel de riesgo.

Importante: no elegir como predictora una variable que ya contiene la respuesta.

Ejemplo incorrecto:

```text
Objetivo: aprobo
Predictora: calificacion_final
```

Puede ser incorrecto si `aprobo` se calcula directamente desde `calificacion_final`.

### Pestana Clustering

Sirve para encontrar grupos parecidos entre registros.

Pasos:

1. Elegir variables para agrupar.
2. Elegir numero de clusters.
3. Presionar `Calcular clusters`.
4. Revisar la tabla de perfil de clusters.

Interpretacion:

Un cluster no es una verdad absoluta. Es un grupo de registros que se parecen segun las variables elegidas.

Ejemplo:

```text
Cluster 0: alta asistencia, muchas tareas, alta calificacion.
Cluster 1: baja asistencia, pocas tareas, calificacion baja.
```

Despues deben poner nombres interpretables:

```text
Cluster 0 = avance consistente
Cluster 1 = requiere apoyo
```

### Pestana Dashboard

Es la vista final para presentar.

Debe responder:

- cual es el patron principal;
- que datos se estan mostrando;
- que grupo o variable destaca;
- que decision podria tomarse.

## Que archivos pueden modificar

### `config.py`

Modificar aqui:

- titulo;
- subtitulo;
- ruta del CSV;
- colores principales.

Ejemplo:

```python
APP_TITLE = "Dashboard de rendimiento academico"
APP_SUBTITLE = "Analisis de asistencia, tareas y calificacion final"
```

### `data/`

Aqui pueden guardar su CSV.

Ejemplo:

```text
data/mi_dataset.csv
```

Luego en `config.py` cambiar:

```python
DEFAULT_DATA_PATH = "data/mi_dataset.csv"
```

### `visualizations.py`

Aqui viven las graficas. Si no saben programar, no es obligatorio modificarlo.

### `analytics.py`

Aqui viven los modelos y clustering. No modificar al inicio.

### `app.py`

Es la app principal. No modificar hasta que entiendan la estructura general.

## Como preparar el CSV

Recomendaciones:

- usar una fila por observacion;
- poner nombres de columnas claros;
- evitar celdas combinadas;
- guardar como `.csv`;
- no dejar titulos arriba de la tabla;
- no mezclar texto y numero en la misma columna;
- revisar fechas.

Ejemplo de estructura correcta:

| fecha | grupo | horas_estudio | asistencia | aprobo |
| --- | --- | --- | --- | --- |
| 2026-01-01 | A | 5 | 90 | Si |
| 2026-01-02 | B | 2 | 70 | No |

## Como escribir interpretaciones

Cada grafica debe tener una interpretacion corta.

Formato recomendado:

```text
Observamos que [variable] tiene [patron].
Esto sugiere que [interpretacion].
Sin embargo, [limitacion].
```

Ejemplo:

```text
Observamos que los estudiantes con mayor asistencia tienden a tener mayor calificacion final.
Esto sugiere que la asistencia podria estar asociada con el desempeno.
Sin embargo, no podemos afirmar causalidad solo con esta grafica.
```

## Errores comunes

| Error | Como resolverlo |
| --- | --- |
| La app no abre | Revisar que el ambiente este activado y correr `streamlit run app.py` |
| No encuentra el CSV | Revisar la ruta en `DEFAULT_DATA_PATH` |
| El CSV se ve raro | Abrirlo en Excel y exportarlo otra vez como CSV |
| El modelo falla | Revisar que la variable objetivo tenga datos |
| Hay demasiadas categorias | Agrupar categorias pequenas como `Otros` |
| No se entiende la grafica | Cambiar titulo, ordenar datos o reducir categorias |

## Entregable sugerido

Cada equipo debe entregar:

- dashboard funcionando;
- pregunta principal;
- descripcion del dataset;
- tres hallazgos descriptivos;
- variables usadas en el modelo;
- metrica principal;
- interpretacion de clusters;
- limitaciones;
- captura o enlace del dashboard.

## Checklist antes de presentar

- La app abre sin errores.
- El titulo corresponde al tema.
- El CSV correcto esta cargado.
- Los filtros funcionan.
- Las graficas tienen sentido.
- Los colores no confunden.
- El modelo tiene una metrica explicada.
- Los clusters tienen nombres interpretables.
- Las conclusiones no afirman causalidad sin evidencia.
