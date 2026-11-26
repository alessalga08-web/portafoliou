# ==========================================
# ACTIVIDAD: AI Challenge — K-Means y KNN
# ==========================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score,
    classification_report
)


# ==========================================
# 1. PREPARACIÓN DE DATOS
# ==========================================

np.random.seed(42)

n_estudiantes = 500

horas_estudio = np.random.uniform(
    2,
    10,
    n_estudiantes
)

asistencia = np.random.uniform(
    50,
    100,
    n_estudiantes
)

tareas_entregadas = np.random.uniform(
    40,
    100,
    n_estudiantes
)


nota_final = (
    (horas_estudio * 3.5)
    + (asistencia * 0.35)
    + (tareas_entregadas * 0.35)
    + np.random.normal(0, 4, n_estudiantes)
)

nota_final = np.clip(
    nota_final,
    0,
    100
)


# Aprobado = 1
# Reprobado = 0

aprobado = (
    nota_final >= 60
).astype(int)


# Crear DataFrame

df = pd.DataFrame({
    "horas_estudio": horas_estudio,
    "asistencia": asistencia,
    "tareas_entregadas": tareas_entregadas,
    "nota_final": nota_final,
    "aprobado": aprobado
})


print(
    f"Estudiantes aprobados en total: "
    f"{df['aprobado'].sum()} de {n_estudiantes}"
)

print(
    "--- Primeras 5 filas del Dataset ---"
)

print(df.head())

print("\n")


# ==========================================
# 2. K-MEANS
# ==========================================

X_cluster = df[
    [
        "horas_estudio",
        "asistencia",
        "tareas_entregadas"
    ]
]


# K-Means con 3 grupos

kmeans_3 = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

df["grupo_3"] = kmeans_3.fit_predict(
    X_cluster
)


# K-Means con 4 grupos

kmeans_4 = KMeans(
    n_clusters=4,
    random_state=42,
    n_init=10
)

df["grupo_4"] = kmeans_4.fit_predict(
    X_cluster
)


# Visualización

plt.figure(figsize=(10, 5))

sns.scatterplot(
    data=df,
    x="horas_estudio",
    y="asistencia",
    hue="grupo_3",
    palette="viridis",
    s=60
)

plt.title(
    "K-Means Clustering "
    "(3 Grupos de Estudiantes)"
)

plt.xlabel(
    "Horas de Estudio Semanales"
)

plt.ylabel(
    "Asistencia (%)"
)

plt.show()


# ==========================================
# 3. KNN
# ==========================================

X = df[
    [
        "horas_estudio",
        "asistencia",
        "tareas_entregadas"
    ]
]

y = df["aprobado"]


# División de datos

X_train, X_test, y_train, y_test = (
    train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=42
    )
)


# Normalización

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(
    X_train
)

X_test_scaled = scaler.transform(
    X_test
)


# Modelo KNN

knn = KNeighborsClassifier(
    n_neighbors=5
)

knn.fit(
    X_train_scaled,
    y_train
)


y_pred = knn.predict(
    X_test_scaled
)


print(
    "--- Resultados de KNN (K=5) ---"
)

print(
    f"Exactitud (Accuracy): "
    f"{accuracy_score(y_test, y_pred) * 100:.2f}%"
)

print(
    "\nReporte de Clasificación:"
)

print(
    classification_report(
        y_test,
        y_pred
    )
)


# ==========================================
# 4. EXPERIMENTACIÓN CON K
# ==========================================

valores_k = [
    1,
    3,
    5,
    7,
    11,
    15,
    21
]

resultados_normalizados = []
resultados_sin_normalizar = []


for k in valores_k:

    # Datos normalizados

    knn_norm = KNeighborsClassifier(
        n_neighbors=k
    )

    knn_norm.fit(
        X_train_scaled,
        y_train
    )

    pred_norm = knn_norm.predict(
        X_test_scaled
    )

    resultados_normalizados.append(
        accuracy_score(
            y_test,
            pred_norm
        )
    )


    # Datos sin normalizar

    knn_sin = KNeighborsClassifier(
        n_neighbors=k
    )

    knn_sin.fit(
        X_train,
        y_train
    )

    pred_sin = knn_sin.predict(
        X_test
    )

    resultados_sin_normalizar.append(
        accuracy_score(
            y_test,
            pred_sin
        )
    )


# Tabla comparativa

df_experimento = pd.DataFrame({
    "Valor de K": valores_k,
    "Accuracy (Con Normalización)":
        resultados_normalizados,
    "Accuracy (Sin Normalización)":
        resultados_sin_normalizar
})


print(
    "\n--- Tabla Comparativa "
    "de Experimentación con K ---"
)

print(
    df_experimento
)


# ==========================================
# 5. DESAFÍO FINAL
# ==========================================

estudiante_nuevo = np.array([
    [4.0, 55.0, 50.0]
])


# Escalar nuevo dato

estudiante_nuevo_scaled = (
    scaler.transform(
        estudiante_nuevo
    )
)


# Predicción

prediccion_desafio = knn.predict(
    estudiante_nuevo_scaled
)

probabilidad_desafio = (
    knn.predict_proba(
        estudiante_nuevo_scaled
    )
)


print(
    "\n--- Resultado del Desafío Final ---"
)


resultado_texto = (
    "Aprobará"
    if prediccion_desafio[0] == 1
    else "Reprobará"
)


print(
    "El estudiante con 4 hrs de estudio, "
    "55% asistencia y 50% tareas: "
    f"{resultado_texto}"
)


print(
    "Probabilidades "
    "[Reprobar, Aprobar]: "
    f"{probabilidad_desafio[0]}"
)
