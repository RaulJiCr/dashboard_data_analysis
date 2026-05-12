# Guia de color para visualizacion de datos

## Proposito

El color en un dashboard no debe usarse solo para decorar. Su funcion principal es ayudar a leer, comparar, priorizar y recordar informacion. Una buena paleta hace que el usuario entienda mas rapido; una mala paleta puede confundir, exagerar diferencias o esconder patrones importantes.

Esta guia resume criterios practicos para que los equipos creen dashboards atractivos, claros y defendibles.

## Principios base

### 1. El color debe tener significado

Antes de elegir colores, preguntar:

- Que quiero que el usuario vea primero?
- Que categorias deben distinguirse?
- Que valores representan alerta, exito o neutralidad?
- El color esta codificando datos o solo decorando?

Regla docente: si el color no ayuda a interpretar, probablemente estorba.

### 2. Menos colores suele ser mejor

Una visualizacion con muchos colores parece llamativa, pero suele ser dificil de leer. Para la mayoria de dashboards:

- 1 color principal;
- 1 color secundario;
- 1 color de alerta;
- 1 color neutro;
- 2 a 4 colores adicionales para categorias.

Evitar usar todos los colores disponibles solo porque la libreria los ofrece.

### 3. Mantener consistencia

Un mismo color debe significar lo mismo en todo el dashboard.

Ejemplo:

- Azul: informacion principal.
- Verde: resultado favorable.
- Naranja: atencion.
- Rojo: riesgo o problema.
- Gris: contexto, valores secundarios o datos sin seleccion.

Si en una grafica el rojo significa "bajo" y en otra significa "alto", el usuario se confunde.

## Tipos de paletas

### Paleta categorica

Sirve para comparar grupos sin orden natural: programa academico, turno, region, tipo de producto, canal de venta.

Recomendaciones:

- usar colores claramente distintos;
- evitar mas de 6 a 8 categorias coloreadas;
- si hay muchas categorias, agrupar las menos frecuentes como "Otros";
- no usar degradados para categorias sin orden.

Ejemplo:

| Categoria | Color sugerido |
| --- | --- |
| Grupo A | Azul |
| Grupo B | Verde |
| Grupo C | Morado |
| Grupo D | Naranja |
| Otros | Gris |

### Paleta secuencial

Sirve para valores ordenados de bajo a alto: calificacion, ingreso, volumen, cantidad, probabilidad.

Recomendaciones:

- usar un degradado de claro a oscuro;
- el tono mas oscuro debe representar mayor intensidad;
- evitar colores muy saturados en todos los niveles;
- incluir leyenda clara.

Ejemplo:

```text
Bajo        Medio        Alto
azul claro  azul medio   azul oscuro
```

### Paleta divergente

Sirve cuando hay un punto medio importante: cambio positivo/negativo, arriba/abajo del promedio, diferencia contra meta.

Recomendaciones:

- usar dos colores opuestos alrededor de un color neutro;
- definir explicitamente el punto central;
- no usarla si no existe un "centro" interpretativo.

Ejemplo:

```text
Debajo de meta     En meta        Encima de meta
rojo suave         gris claro     verde
```

## Colores recomendados para dashboards academicos

Una paleta sobria y facil de leer:

| Uso | Color | Hex |
| --- | --- | --- |
| Principal | Azul | `#2563EB` |
| Secundario | Verde | `#16A34A` |
| Atencion | Naranja | `#F59E0B` |
| Problema | Rojo | `#DC2626` |
| Neutro oscuro | Gris pizarra | `#334155` |
| Neutro medio | Gris | `#64748B` |
| Fondo | Blanco suave | `#FFFFFF` |
| Fondo secundario | Gris muy claro | `#F8FAFC` |

Esta es la paleta que usa la plantilla base.

## Accesibilidad

### No depender solo del color

Algunas personas tienen dificultad para distinguir ciertos colores. Por eso, ademas del color, usar:

- etiquetas;
- iconos discretos;
- ordenamiento;
- texto de apoyo;
- grosor de linea;
- patrones o marcadores.

Ejemplo incorrecto:

```text
Los valores rojos son importantes.
```

Ejemplo mejor:

```text
Los valores marcados como "Atencion" superan el umbral definido.
```

### Cuidar contraste

Texto claro sobre fondo claro o texto oscuro sobre fondo oscuro cansa y dificulta la lectura.

Reglas practicas:

- usar texto oscuro sobre fondos claros;
- evitar texto sobre colores muy saturados;
- si se usa color fuerte como fondo, usar texto blanco y fuente suficientemente grande;
- probar la lectura en pantalla pequena.

### Evitar combinaciones problematicas

Con cuidado:

- rojo/verde como unica senal;
- amarillo claro sobre blanco;
- azul y morado muy parecidos;
- muchos colores pastel juntos;
- fondos oscuros con graficas saturadas si el curso no requiere ese estilo.

## Color segun tipo de grafica

### Barras

Usar un solo color cuando se comparan valores de una misma variable.

Usar varios colores solo si el color agrega una categoria adicional.

### Lineas

Para series temporales:

- 1 linea principal destacada;
- lineas secundarias en gris o con menor opacidad;
- no usar mas de 4 o 5 lineas si se espera lectura rapida.

### Heatmaps

Usar paleta secuencial o divergente segun la pregunta.

- Secuencial: mayor o menor volumen.
- Divergente: arriba o abajo de un promedio/meta.

### Mapas

No usar colores muy intensos para todo el mapa.

Recomendaciones:

- fondo neutro;
- datos importantes con color;
- leyenda clara;
- evitar que limites geograficos compitan visualmente con los datos.

### KPIs

Los KPIs deben usar color con moderacion.

- Numero principal: color neutro oscuro.
- Cambio positivo: verde.
- Cambio negativo: rojo o naranja.
- Texto auxiliar: gris.

Evitar poner todos los KPIs en tarjetas de colores fuertes.

## Como elegir una paleta en clase

### Paso 1. Definir tono del dashboard

| Contexto | Estilo visual recomendado |
| --- | --- |
| Academico | sobrio, claro, con colores moderados |
| Operativo | alto contraste, lectura rapida |
| Ejecutivo | pocos colores, mucho espacio, KPIs claros |
| Exploratorio | mas flexibilidad, pero con leyendas claras |

### Paso 2. Definir color principal

Elegir un color que aparezca en titulos, botones, barras principales o elementos activos.

### Paso 3. Definir color de alerta

No todo debe ser rojo. Usar rojo solo cuando hay problema serio. Para advertencia o atencion, naranja suele ser mejor.

### Paso 4. Definir neutros

Los grises son esenciales. Sirven para ejes, texto secundario, fondos y datos de contexto.

### Paso 5. Probar con una grafica real

No elegir paletas en abstracto. Probar con el dataset del equipo.

## Errores frecuentes

| Error | Problema | Correccion |
| --- | --- | --- |
| Usar arcoiris | Dificulta comparar magnitudes | Usar secuencial o categorica controlada |
| Colorear todo | Nada destaca | Reservar color fuerte para lo importante |
| Cambiar significado del color | Confunde | Crear reglas de color por proyecto |
| Texto sin contraste | No se lee | Subir contraste o cambiar fondo |
| Demasiadas categorias | Leyenda inmanejable | Agrupar categorias pequenas |
| Rojo/verde sin etiquetas | Poco accesible | Agregar texto, simbolos o etiquetas |

## Checklist visual antes de entregar

- La paleta tiene 4 a 8 colores maximo.
- El color principal se usa de forma consistente.
- Rojo, naranja y verde tienen significado claro.
- Las graficas pueden entenderse sin depender solo del color.
- Las leyendas son cortas y legibles.
- Los textos tienen buen contraste.
- El dashboard no parece decorado al azar.
- Cada color responde a una decision de interpretacion.
