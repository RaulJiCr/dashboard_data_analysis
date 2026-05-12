"""Carga y preparacion ligera de datos.

Este modulo separa la lectura del CSV de la interfaz visual. Asi la app queda
mas facil de entender: app.py decide que mostrar, data_loader.py decide como
leer y ordenar los datos.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import BinaryIO

import pandas as pd
import streamlit as st


@dataclass
class ColumnProfile:
    """Resumen de tipos de columnas detectadas en el dataset."""

    numeric: list[str]
    categorical: list[str]
    datetime: list[str]
    boolean: list[str]


@st.cache_data(show_spinner=False)
def load_csv_from_path(path: str) -> pd.DataFrame:
    """Lee un CSV local y devuelve un DataFrame."""

    return pd.read_csv(path)


def load_csv_from_upload(uploaded_file: BinaryIO) -> pd.DataFrame:
    """Lee un CSV cargado desde la interfaz de Streamlit."""

    return pd.read_csv(uploaded_file)


def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Crea una copia con nombres de columnas mas uniformes.

    Ejemplo: "Calificacion Final" se vuelve "calificacion_final".
    Esto reduce errores al seleccionar columnas desde el codigo.
    """

    cleaned = df.copy()
    cleaned.columns = [
        str(col).strip().lower().replace(" ", "_").replace("-", "_")
        for col in cleaned.columns
    ]
    return cleaned


def parse_possible_dates(df: pd.DataFrame) -> pd.DataFrame:
    """Intenta convertir a fecha columnas cuyo nombre sugiere tiempo.

    La funcion evita convertir cualquier texto arbitrario. Solo revisa columnas
    con nombres como fecha, date, dia o mes.
    """

    parsed = df.copy()
    date_tokens = ("fecha", "date", "dia", "day", "mes", "month")

    for column in parsed.columns:
        lower_name = str(column).lower()
        looks_like_date = any(token in lower_name for token in date_tokens)

        if looks_like_date and not pd.api.types.is_numeric_dtype(parsed[column]):
            converted = pd.to_datetime(parsed[column], errors="coerce")
            success_rate = converted.notna().mean()

            if success_rate >= 0.7:
                parsed[column] = converted

    return parsed


def profile_columns(df: pd.DataFrame) -> ColumnProfile:
    """Clasifica columnas por tipo para poblar selectores y graficas."""

    numeric = df.select_dtypes(include=["number"]).columns.tolist()
    datetime = df.select_dtypes(include=["datetime64[ns]", "datetimetz"]).columns.tolist()
    boolean = df.select_dtypes(include=["bool"]).columns.tolist()

    categorical = [
        column
        for column in df.columns
        if column not in numeric and column not in datetime and column not in boolean
    ]

    return ColumnProfile(
        numeric=numeric,
        categorical=categorical,
        datetime=datetime,
        boolean=boolean,
    )


def missing_values_table(df: pd.DataFrame) -> pd.DataFrame:
    """Devuelve conteo y porcentaje de valores faltantes por columna."""

    total_missing = df.isna().sum()
    percent_missing = (total_missing / len(df)).fillna(0) * 100

    summary = pd.DataFrame(
        {
            "columna": total_missing.index,
            "faltantes": total_missing.values,
            "porcentaje_faltante": percent_missing.round(2).values,
        }
    )

    return summary.sort_values("porcentaje_faltante", ascending=False)


def prepare_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """Aplica preparacion inicial compartida por toda la app."""

    prepared = clean_column_names(df)
    prepared = parse_possible_dates(prepared)
    return prepared
