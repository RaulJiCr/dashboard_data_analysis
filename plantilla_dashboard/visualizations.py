"""Visualizaciones reutilizables para la plantilla.

Mantener las graficas aqui permite que los estudiantes cambien una figura sin
romper la logica de carga, filtros o modelado.
"""

from __future__ import annotations

import pandas as pd
import plotly.express as px

from config import COLOR_PRIMARY, COLOR_SECONDARY


def numeric_histogram(df: pd.DataFrame, column: str):
    """Histograma para revisar la distribucion de una variable numerica."""

    return px.histogram(
        df,
        x=column,
        nbins=24,
        color_discrete_sequence=[COLOR_PRIMARY],
        title=f"Distribucion de {column}",
    )


def numeric_boxplot(df: pd.DataFrame, column: str):
    """Boxplot para detectar dispersion y posibles valores atipicos."""

    return px.box(
        df,
        y=column,
        points="outliers",
        color_discrete_sequence=[COLOR_SECONDARY],
        title=f"Variabilidad de {column}",
    )


def category_bar_chart(df: pd.DataFrame, column: str, top_n: int = 15):
    """Grafica de barras para las categorias mas frecuentes."""

    counts = (
        df[column]
        .astype(str)
        .value_counts(dropna=False)
        .head(top_n)
        .rename_axis(column)
        .reset_index(name="conteo")
    )

    return px.bar(
        counts,
        x="conteo",
        y=column,
        orientation="h",
        color_discrete_sequence=[COLOR_PRIMARY],
        title=f"Frecuencia de {column}",
    )


def correlation_heatmap(df: pd.DataFrame, numeric_columns: list[str]):
    """Mapa de calor de correlaciones entre variables numericas."""

    corr = df[numeric_columns].corr(numeric_only=True)

    return px.imshow(
        corr,
        text_auto=".2f",
        color_continuous_scale="RdBu_r",
        zmin=-1,
        zmax=1,
        title="Correlacion entre variables numericas",
    )


def feature_importance_bar(feature_importance: pd.DataFrame):
    """Grafica de importancia de variables del modelo supervisado."""

    return px.bar(
        feature_importance.sort_values("importancia"),
        x="importancia",
        y="feature",
        orientation="h",
        color_discrete_sequence=[COLOR_PRIMARY],
        title="Variables mas influyentes del modelo",
    )


def prediction_scatter(predictions: pd.DataFrame):
    """Comparacion entre valor real y prediccion para problemas de regresion."""

    return px.scatter(
        predictions,
        x="valor_real",
        y="prediccion",
        color_discrete_sequence=[COLOR_PRIMARY],
        title="Valor real vs. prediccion",
    )


def cluster_scatter(df: pd.DataFrame, x_column: str, y_column: str):
    """Dispersion 2D coloreada por cluster."""

    return px.scatter(
        df,
        x=x_column,
        y=y_column,
        color=df["cluster"].astype(str),
        title=f"Clusters segun {x_column} y {y_column}",
        color_discrete_sequence=px.colors.qualitative.Set2,
    )
