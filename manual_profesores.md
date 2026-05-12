# Manual para profesores: analisis de datos, modelos y dashboards

## Proposito del curso

Este manual sirve como guia para un curso express orientado a estudiantes de ingenieria que no necesariamente programan. La meta no es que memoricen sintaxis, sino que aprendan a convertir datos en una historia analitica defendible:

- formular una pregunta clara;
- revisar calidad, sesgos y estructura de los datos;
- describir patrones con estadistica;
- crear variables utiles mediante feature engineering;
- entrenar e interpretar un modelo supervisado;
- agrupar observaciones con clustering;
- comunicar hallazgos en un dashboard.

Los dashboards existentes del directorio funcionan como referencia tecnica: Streamlit, filtros, KPIs, visualizaciones, predicciones, mapas y clustering. El dominio de criminalidad no es el centro del curso; lo importante es el flujo de trabajo analitico.

## Perfil de entrada

Los estudiantes deben poder:

- leer tablas en Excel o CSV;
- interpretar porcentajes, promedios y graficas basicas;
- distinguir entre una pregunta descriptiva y una predictiva;
- seguir instrucciones en una plantilla de codigo comentada.

No se asume experiencia previa en programacion. La plantilla reduce la carga tecnica para que el trabajo se concentre en criterio analitico.

## Resultado esperado por equipo

Cada equipo entrega:

- un dataset propio o asignado;
- una pregunta principal de analisis;
- un mini reporte metodologico;
- un dashboard Streamlit adaptado desde la plantilla;
- una presentacion corta con hallazgos, interpretacion, decisiones visuales y limitaciones.

## Estructura sugerida del curso express

### Bloque 1. De la pregunta al dato

Objetivo: que cada equipo traduzca un tema amplio en una pregunta analizable.

Guia docente:

1. Pedir una pregunta de negocio, social, academica o tecnica.
2. Convertirla en variables observables.
3. Definir unidad de analisis: persona, evento, estacion, producto, municipio, dia, sensor, transaccion.
4. Distinguir variable objetivo de variables explicativas.
5. Revisar si la pregunta es descriptiva, comparativa, predictiva o exploratoria.

Ejemplos de preguntas:

- Descriptiva: que grupos tienen mayor promedio?
- Comparativa: cambia el desempeno entre turnos?
- Predictiva: podemos estimar la probabilidad de aprobacion?
- Exploratoria: existen perfiles naturales de estudiantes, clientes o zonas?

Producto del bloque:

- pregunta principal;
- lista de variables necesarias;
- hipotesis inicial;
- definicion de exito analitico.

### Bloque 2. Carga, limpieza y calidad del dato

Objetivo: que los estudiantes entiendan que un modelo malo muchas veces nace de datos mal revisados.

Revision minima:

- numero de filas y columnas;
- tipos de variables;
- valores faltantes;
- duplicados;
- rangos imposibles;
- categorias escritas de forma inconsistente;
- fechas mal parseadas;
- unidades mezcladas.

Preguntas de interpretacion:

- Que representa una fila?
- Hay columnas que son identificadores y no deberian entrar al modelo?
- Hay variables medidas despues del resultado que causarian fuga de informacion?
- Los valores faltantes son azarosos o significan algo?
- La muestra representa al fenomeno que queremos estudiar?

Decision docente importante:

No conviene "limpiar por limpiar". Cada transformacion debe tener justificacion: imputar, eliminar, agrupar categorias o normalizar unidades cambia la lectura del fenomeno.

### Bloque 3. Estadistica descriptiva e interpretacion

Objetivo: pasar de graficas bonitas a lectura estadistica.

Elementos esenciales:

- conteos y porcentajes para variables categoricas;
- media, mediana, desviacion estandar, minimos, maximos y percentiles para numericas;
- distribuciones e histogramas;
- boxplots para variabilidad y valores extremos;
- correlaciones entre numericas;
- tablas cruzadas para comparar grupos.

Guia de lectura:

- La media resume, pero puede enganarse con valores extremos.
- La mediana ayuda cuando la distribucion esta sesgada.
- La desviacion estandar expresa dispersion, no calidad.
- La correlacion mide asociacion lineal, no causalidad.
- Los porcentajes deben tener denominador claro.

Actividad sugerida:

Cada equipo elige tres hallazgos descriptivos y debe escribirlos con esta estructura:

```text
Observamos que [variable/patron] cambia en [grupo/tiempo/condicion].
La evidencia es [grafica/metrica].
Una interpretacion posible es [explicacion].
Una limitacion es [sesgo/dato faltante/variable no observada].
```

### Bloque 4. Feature engineering

Objetivo: mostrar que los modelos aprenden mejor cuando las variables representan el fenomeno de forma informativa.

Tipos de features utiles:

- fechas: mes, dia de semana, hora, trimestre, temporada;
- proporciones: tareas entregadas / tareas asignadas;
- cambios: diferencia contra periodo anterior;
- indicadores binarios: tiene beca, hubo retraso, es fin de semana;
- agregados: promedio movil, conteo por grupo, acumulado;
- codificacion de categorias: one-hot encoding;
- transformaciones: logaritmo para variables muy sesgadas;
- escalamiento: necesario para clustering y modelos basados en distancia.

Riesgos:

- fuga de informacion: usar una variable que en la realidad no estaria disponible al momento de predecir;
- sobreingenieria: crear muchas variables sin hipotesis;
- variables proxy sensibles: columnas que indirectamente codifican informacion delicada;
- features no explicables para usuarios finales.

Actividad sugerida:

Pedir que cada equipo proponga cinco features y las clasifique:

| Feature | Fuente | Hipotesis | Riesgo | Se usara? |
| --- | --- | --- | --- | --- |
| mes_fecha | fecha | hay estacionalidad | bajo | si |
| promedio_ultimas_4_sem | historico | tendencia reciente | fuga si usa futuro | depende |

### Bloque 5. Modelos supervisados

Objetivo: entrenar un modelo simple y entender sus resultados sin convertir la clase en un curso profundo de algoritmos.

Flujo minimo:

1. Elegir variable objetivo.
2. Elegir variables predictoras.
3. Separar entrenamiento y prueba.
4. Preprocesar datos: imputacion, escalamiento, codificacion.
5. Entrenar un modelo base.
6. Evaluar con metricas apropiadas.
7. Interpretar importancia de variables y errores.

Tipos de problema:

- Clasificacion: la variable objetivo es una categoria, por ejemplo "aprobo" o "no aprobo".
- Regresion: la variable objetivo es numerica continua, por ejemplo calificacion, demanda o ingreso.

Metricas recomendadas:

Clasificacion:

- accuracy: porcentaje de aciertos;
- precision: de los predichos positivos, cuantos eran positivos;
- recall: de los positivos reales, cuantos encontramos;
- F1: balance entre precision y recall;
- matriz de confusion: donde se equivoca el modelo.

Regresion:

- MAE: error absoluto promedio, facil de explicar;
- RMSE: penaliza errores grandes;
- R2: proporcion de variabilidad explicada, con cuidado al interpretarlo.

Preguntas de interpretacion:

- El modelo supera una regla simple?
- En que casos se equivoca mas?
- Que variables parecen mas influyentes?
- La metrica elegida corresponde al costo real del error?
- El modelo generaliza o solo memoriza?

### Bloque 6. Clustering

Objetivo: usar aprendizaje no supervisado para descubrir perfiles, no para afirmar verdades absolutas.

Ideas clave:

- En clustering no hay etiqueta correcta conocida.
- Los clusters dependen de las variables seleccionadas y del escalamiento.
- K-means agrupa por distancia; por eso las variables numericas deben escalarse.
- El numero de clusters debe justificarse con metrica y lectura sustantiva.

Proceso:

1. Elegir variables relevantes.
2. Escalar variables numericas.
3. Probar varios valores de k.
4. Revisar silueta y tamanos de clusters.
5. Perfilar cada cluster con medias, modas y distribuciones.
6. Nombrar clusters con lenguaje descriptivo, no estigmatizante.

Ejemplo de interpretacion:

```text
Cluster 2 concentra estudiantes con alta asistencia, muchas tareas entregadas y calificaciones altas.
Lo llamamos "avance consistente".
No significa que todos los estudiantes del grupo sean iguales; solo comparten un patron promedio en las variables usadas.
```

### Bloque 7. Dashboard

Objetivo: construir una herramienta de comunicacion, no un deposito de graficas.

Estructura recomendada:

- encabezado con pregunta y alcance;
- filtros globales;
- KPIs principales;
- visualizaciones descriptivas;
- seccion de modelo supervisado;
- seccion de clusters;
- tabla descargable o vista de datos;
- notas de interpretacion y limitaciones.

Principios de diseno:

- cada grafica debe responder una pregunta;
- los filtros deben cambiar la lectura, no solo decorar;
- los KPIs deben tener denominador claro;
- evitar saturacion visual;
- usar nombres comprensibles para variables;
- separar resultados descriptivos de predicciones.
- usar color con significado constante, no como decoracion.

Preguntas para revisar dashboards:

- Que decision podria tomar alguien con esto?
- Cual es el hallazgo mas importante en los primeros 30 segundos?
- Se entiende que datos se filtraron?
- Hay alguna grafica redundante?
- El usuario puede distinguir dato observado, prediccion y cluster?
- El significado de los colores es consistente?

### Bloque 8. Color y presentacion visual

Objetivo: que los estudiantes usen color para comunicar datos con claridad y no solo para hacer la pantalla mas llamativa.

Material de apoyo:

```text
guia_color_visualizacion_datos.md
```

Ideas clave para explicar:

- El color debe tener significado: categoria, intensidad, alerta, exito o contexto.
- Una paleta corta suele comunicar mejor que una paleta con muchos colores.
- El mismo color debe significar lo mismo en todo el dashboard.
- Los colores fuertes se reservan para lo importante.
- Rojo, verde y naranja deben usarse con cuidado porque sugieren juicio o alerta.
- No se debe depender solo del color: tambien usar etiquetas, ordenamiento y texto.

Actividad sugerida:

Pedir a cada equipo que documente su paleta:

| Elemento | Color | Significado |
| --- | --- | --- |
| Principal | Azul | metrica central |
| Alerta | Naranja | valor que requiere atencion |
| Problema | Rojo | resultado debajo del umbral |
| Contexto | Gris | informacion secundaria |

Antes de presentar, cada equipo debe responder:

- Que color guia la lectura principal?
- Que color indica alerta?
- Hay algun color que se use con significados distintos?
- La grafica se entiende si se imprime en blanco y negro?
- El texto se lee bien sobre el fondo?

## Rubrica sugerida

| Criterio | Excelente | Suficiente | Debe mejorar |
| --- | --- | --- | --- |
| Pregunta analitica | Clara, medible y conectada con decision | Clara pero amplia | Ambigua o no medible |
| Limpieza de datos | Decisiones justificadas | Limpieza basica | Sin revision de calidad |
| Estadistica | Interpreta patrones y limitaciones | Describe graficas | Solo muestra graficas |
| Feature engineering | Variables utiles y defendibles | Algunas variables nuevas | Sin justificacion |
| Modelo | Evalua e interpreta errores | Entrena y reporta metrica | Sin evaluacion clara |
| Clustering | Perfiles interpretados con cautela | Clusters mostrados | Clusters sin explicacion |
| Dashboard | Claro, funcional y enfocado | Funcional con exceso de elementos | Dificil de entender |
| Diseno visual | Paleta consistente y legible | Colores aceptables pero poco justificados | Colores confusos o decorativos |
| Comunicacion | Hallazgos con evidencia y limites | Resumen general | Conclusiones no sustentadas |

## Guion para los profesores

### Antes de clase

- Elegir 1 o 2 datasets de respaldo por si algun equipo no trae datos.
- Verificar que la plantilla Streamlit corra localmente.
- Preparar una demostracion con `data/ejemplo_estudiantes.csv`.
- Definir si los equipos trabajaran con clasificacion, regresion o ambos.

### Durante clase

1. Abrir con el mapa del proceso analitico completo.
2. Mostrar un dashboard existente y preguntar: que decisiones permite tomar?
3. Separar el dashboard en modulos: carga, filtros, KPIs, graficas, modelo, clusters.
4. Trabajar primero en interpretacion; despues en codigo.
5. Pedir entregables pequenos por bloque para evitar que todo se acumule al final.

### Cierre

Cada equipo presenta:

- pregunta;
- dataset y unidad de analisis;
- tres hallazgos descriptivos;
- dos features importantes;
- metrica del modelo y principal error;
- significado de los clusters;
- justificacion de la paleta de color;
- una limitacion seria;
- una mejora futura.

## Errores frecuentes y como corregirlos

| Error | Senal | Intervencion docente |
| --- | --- | --- |
| Quieren predecir sin entender los datos | Saltan directo al modelo | Pedir 3 graficas descriptivas antes de modelar |
| Usan demasiadas variables | No pueden explicar el modelo | Limitar a 5-12 variables iniciales |
| Interpretan correlacion como causalidad | "X causa Y" | Cambiar a "X se asocia con Y" |
| Ignoran faltantes | Metricas sospechosamente altas | Revisar columna por columna |
| Clusters sin sentido | Nombres inventados sin evidencia | Exigir perfil estadistico de cada cluster |
| Dashboard saturado | Muchas graficas sin narrativa | Pedir una pregunta por grafica |

## Relacion con los dashboards existentes

Los proyectos revisados aportan patrones reutilizables:

- `mapa_alcaldias_v1`: estructura multipagina, autenticacion, filtros, KPIs, visualizaciones temporales y mapas.
- `Streamlit_final-main`: organizacion modular, datos cacheados, vistas por rol, clustering, predicciones y series de tiempo.
- `dashboard_metro_final`: narrativa de dashboard, modelos guardados, predicciones, componentes de mapa y analisis temporal.

Para el curso conviene abstraer esos patrones:

- de "alcaldia/estacion/delito" a "grupo/lugar/categoria";
- de "incidencia" a "evento, resultado o desempeno";
- de "riesgo" a "probabilidad, volumen, segmento o prediccion";
- de "perfil delictivo" a "perfil de comportamiento".

## Checklist final para evaluar proyectos

- La pregunta principal esta escrita al inicio.
- Se sabe que representa cada fila del dataset.
- Las columnas objetivo y predictoras estan identificadas.
- Hay revision de faltantes y tipos de datos.
- Las graficas descriptivas tienen interpretacion.
- Las features nuevas tienen razon de existir.
- El modelo usa separacion entrenamiento/prueba.
- Las metricas corresponden al tipo de problema.
- Los clusters estan perfilados y nombrados con evidencia.
- El dashboard permite filtrar, comparar e interpretar.
- Las limitaciones estan explicitas.
