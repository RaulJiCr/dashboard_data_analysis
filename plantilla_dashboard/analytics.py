"""Funciones analiticas: estadistica, features, modelo y clustering.

Las funciones estan pensadas para uso didactico. Prefieren claridad sobre
optimizaciones avanzadas, y devuelven tablas que se pueden mostrar directo en
Streamlit.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    mean_absolute_error,
    mean_squared_error,
    r2_score,
    silhouette_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from config import RANDOM_STATE


ProblemType = Literal["classification", "regression"]


@dataclass
class ModelResult:
    """Paquete con todo lo necesario para interpretar el modelo."""

    problem_type: ProblemType
    metrics: pd.DataFrame
    feature_importance: pd.DataFrame
    predictions: pd.DataFrame
    confusion: pd.DataFrame | None


@dataclass
class ClusterResult:
    """Paquete con resultados de clustering."""

    data_with_clusters: pd.DataFrame
    profile: pd.DataFrame
    silhouette: float | None


def add_date_features(df: pd.DataFrame, date_columns: list[str]) -> pd.DataFrame:
    """Agrega columnas derivadas de fechas.

    Para una columna "fecha", crea: fecha_anio, fecha_mes, fecha_dia_semana.
    """

    featured = df.copy()

    for column in date_columns:
        if column not in featured.columns:
            continue

        dates = pd.to_datetime(featured[column], errors="coerce")
        featured[f"{column}_anio"] = dates.dt.year
        featured[f"{column}_mes"] = dates.dt.month
        featured[f"{column}_dia_semana"] = dates.dt.dayofweek

    return featured


def infer_problem_type(target: pd.Series) -> ProblemType:
    """Decide si el problema parece clasificacion o regresion."""

    unique_values = target.dropna().nunique()
    is_numeric = pd.api.types.is_numeric_dtype(target)

    if is_numeric and unique_values > 10:
        return "regression"

    return "classification"


def _split_columns_by_type(df: pd.DataFrame) -> tuple[list[str], list[str]]:
    """Separa columnas numericas y categoricas para el preprocesamiento."""

    numeric_features = df.select_dtypes(include=["number", "bool"]).columns.tolist()
    categorical_features = [
        column for column in df.columns if column not in numeric_features
    ]
    return numeric_features, categorical_features


def build_preprocessor(X: pd.DataFrame) -> ColumnTransformer:
    """Crea el preprocesador compartido por modelos y clustering."""

    numeric_features, categorical_features = _split_columns_by_type(X)

    numeric_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ]
    )

    categorical_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
        ]
    )

    return ColumnTransformer(
        transformers=[
            ("num", numeric_pipeline, numeric_features),
            ("cat", categorical_pipeline, categorical_features),
        ],
        remainder="drop",
    )


def _get_feature_names(preprocessor: ColumnTransformer) -> list[str]:
    """Recupera nombres de features despues del one-hot encoding."""

    try:
        return preprocessor.get_feature_names_out().tolist()
    except Exception:
        return [f"feature_{idx}" for idx in range(len(preprocessor.transformers_))]


def train_supervised_model(
    df: pd.DataFrame,
    target_column: str,
    feature_columns: list[str],
) -> ModelResult:
    """Entrena un modelo supervisado y devuelve metricas interpretables."""

    modeling_df = df[feature_columns + [target_column]].dropna(subset=[target_column])
    X = modeling_df[feature_columns]
    y = modeling_df[target_column]

    problem_type = infer_problem_type(y)

    stratify = y if problem_type == "classification" and y.nunique() > 1 else None
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=RANDOM_STATE,
        stratify=stratify,
    )

    preprocessor = build_preprocessor(X_train)

    if problem_type == "classification":
        model = RandomForestClassifier(
            n_estimators=200,
            min_samples_leaf=2,
            random_state=RANDOM_STATE,
        )
    else:
        model = RandomForestRegressor(
            n_estimators=200,
            min_samples_leaf=2,
            random_state=RANDOM_STATE,
        )

    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", model),
        ]
    )

    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)

    if problem_type == "classification":
        metrics = pd.DataFrame(
            {
                "metrica": ["accuracy", "f1_macro"],
                "valor": [
                    accuracy_score(y_test, y_pred),
                    f1_score(y_test, y_pred, average="macro", zero_division=0),
                ],
            }
        )
        labels = sorted(pd.Series(y_test).astype(str).unique().tolist())
        confusion = pd.DataFrame(
            confusion_matrix(y_test.astype(str), pd.Series(y_pred).astype(str), labels=labels),
            index=[f"real_{label}" for label in labels],
            columns=[f"pred_{label}" for label in labels],
        )
    else:
        rmse = mean_squared_error(y_test, y_pred) ** 0.5
        metrics = pd.DataFrame(
            {
                "metrica": ["mae", "rmse", "r2"],
                "valor": [
                    mean_absolute_error(y_test, y_pred),
                    rmse,
                    r2_score(y_test, y_pred),
                ],
            }
        )
        confusion = None

    feature_names = _get_feature_names(pipeline.named_steps["preprocessor"])
    importances = pipeline.named_steps["model"].feature_importances_

    feature_importance = (
        pd.DataFrame({"feature": feature_names, "importancia": importances})
        .sort_values("importancia", ascending=False)
        .head(15)
        .reset_index(drop=True)
    )

    predictions = pd.DataFrame(
        {
            "valor_real": y_test.reset_index(drop=True),
            "prediccion": pd.Series(y_pred),
        }
    )

    return ModelResult(
        problem_type=problem_type,
        metrics=metrics.round(4),
        feature_importance=feature_importance,
        predictions=predictions,
        confusion=confusion,
    )


def run_clustering(
    df: pd.DataFrame,
    feature_columns: list[str],
    n_clusters: int,
) -> ClusterResult:
    """Ejecuta K-means y perfila los clusters resultantes."""

    cluster_df = df[feature_columns].copy()
    preprocessor = build_preprocessor(cluster_df)
    X_processed = preprocessor.fit_transform(cluster_df)

    kmeans = KMeans(
        n_clusters=n_clusters,
        random_state=RANDOM_STATE,
        n_init=10,
    )
    labels = kmeans.fit_predict(X_processed)

    data_with_clusters = df.copy()
    data_with_clusters["cluster"] = labels

    silhouette = None
    if n_clusters > 1 and len(set(labels)) > 1 and len(labels) > n_clusters:
        silhouette = float(silhouette_score(X_processed, labels))

    profile_rows = []
    for cluster_id in sorted(data_with_clusters["cluster"].unique()):
        subset = data_with_clusters[data_with_clusters["cluster"] == cluster_id]
        row = {
            "cluster": cluster_id,
            "registros": len(subset),
            "porcentaje": round(len(subset) / len(data_with_clusters) * 100, 2),
        }

        for column in feature_columns:
            if pd.api.types.is_numeric_dtype(subset[column]):
                row[f"{column}_promedio"] = round(subset[column].mean(), 3)
            else:
                mode = subset[column].mode(dropna=True)
                row[f"{column}_moda"] = mode.iloc[0] if not mode.empty else None

        profile_rows.append(row)

    profile = pd.DataFrame(profile_rows)

    return ClusterResult(
        data_with_clusters=data_with_clusters,
        profile=profile,
        silhouette=silhouette,
    )


def describe_numeric_columns(df: pd.DataFrame, numeric_columns: list[str]) -> pd.DataFrame:
    """Tabla compacta con estadisticos descriptivos."""

    if not numeric_columns:
        return pd.DataFrame()

    return (
        df[numeric_columns]
        .describe()
        .T[["count", "mean", "std", "min", "25%", "50%", "75%", "max"]]
        .round(3)
        .reset_index()
        .rename(columns={"index": "columna"})
    )
