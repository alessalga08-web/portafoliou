import json

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium

from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier


# ==========================================
# FASE A:
# RECOLECCIÓN, LIMPIEZA Y ANÁLISIS
# EXPLORATORIO
# ==========================================


# Cargar archivo exportado de Overpass Turbo

with open(
    "export.geojson",
    "r",
    encoding="utf-8"
) as f:

    data = json.load(f)


registros = []


for feature in data["features"]:

    props = feature.get(
        "properties",
        {}
    )

    geom = feature.get(
        "geometry",
        {}
    )

    coords = geom.get(
        "coordinates",
        []
    )


    # Extraer coordenadas

    if (
        geom.get("type") == "Point"
        and len(coords) >= 2
    ):

        lon, lat = (
            coords[0],
            coords[1]
        )

    elif "center" in feature:

        lon = feature["center"]["lon"]
        lat = feature["center"]["lat"]

    else:

        continue


    registros.append({
        "name": props.get(
            "name",
            "Sin nombre registrado"
        ),

        "category": props.get(
            "tourism",
            "hotel"
        ),

        "latitude": float(lat),

        "longitude": float(lon),

        "city_municipality": props.get(
            "addr:city",
            props.get(
                "addr:municipality",
                "La Paz (No especificado)"
            )
        )
    })


df = pd.DataFrame(
    registros
)


# ==========================================
# LIMPIEZA
# ==========================================

total_inicial = len(df)

df = df.dropna(
    subset=[
        "latitude",
        "longitude"
    ]
)

df = df.drop_duplicates(
    subset=[
        "name",
        "latitude",
        "longitude"
    ]
).reset_index(
    drop=True
)


print(
    "--- FASE A: EXPLORACIÓN Y LIMPIEZA ---"
)

print(
    "Registros extraídos inicialmente "
    f"de OSM: {total_inicial}"
)

print(
    "Registros limpios y únicos: "
    f"{len(df)}"
)

print(
    df.head(10)
)

print(
    "\nConteo por categoría:"
)

print(
    df["category"].value_counts()
)


# Exportar dataset limpio

df.to_csv(
    "dataset_hoteles_la_paz_limpio.csv",
    index=False,
    encoding="utf-8"
)


# ==========================================
# FASE B:
# K-MEANS
# ==========================================

X_coords = df[
    [
        "latitude",
        "longitude"
    ]
].values


k_elegido = 3


kmeans = KMeans(
    n_clusters=k_elegido,
    random_state=42,
    n_init=10
)


df["cluster"] = (
    kmeans.fit_predict(
        X_coords
    )
)


centroides = (
    kmeans.cluster_centers_
)


print(
    f"\n--- FASE B: "
    f"K-MEANS (K={k_elegido}) ---"
)


for i, c in enumerate(
    centroides
):

    print(
        f"Cluster {i} -> "
        f"Centroide en Lat: "
        f"{c[0]:.5f}, "
        f"Lon: {c[1]:.5f} | "
        f"Total lugares: "
        f"{(df['cluster'] == i).sum()}"
    )


# Gráfico

plt.figure(
    figsize=(8, 5)
)

sns.scatterplot(
    data=df,
    x="longitude",
    y="latitude",
    hue="cluster",
    palette="Set1",
    s=80
)

plt.scatter(
    centroides[:, 1],
    centroides[:, 0],
    c="black",
    s=200,
    marker="X",
    label="Centroides"
)

plt.title(
    "Distribución de Hoteles en La Paz "
    "(K-Means)"
)

plt.xlabel(
    "Longitud"
)

plt.ylabel(
    "Latitud"
)

plt.legend()

plt.grid(True)

plt.show()


# ==========================================
# FASE C:
# KNN
# ==========================================


df["zona_etiqueta"] = np.where(
    df["latitude"] < 13.40,
    "Zona Costera / Playa",
    "Zona Interior / Urbana"
)


X_rad = np.radians(
    df[
        [
            "latitude",
            "longitude"
        ]
    ].values
)

y_zonas = df[
    "zona_etiqueta"
].values


k_knn = 3


knn = KNeighborsClassifier(
    n_neighbors=k_knn,
    metric="haversine"
)


knn.fit(
    X_rad,
    y_zonas
)


# Coordenadas de referencia

nueva_lat = 13.3210
nueva_lon = -88.9450


nueva_ubicacion_rad = np.radians(
    [
        [
            nueva_lat,
            nueva_lon
        ]
    ]
)


clase_predicha = knn.predict(
    nueva_ubicacion_rad
)[0]


distancias_rad, indices_vecinos = (
    knn.kneighbors(
        nueva_ubicacion_rad
    )
)


distancias_km = (
    distancias_rad[0] * 6371.0
)


print(
    f"\n--- FASE C: RESULTADO DE KNN "
    f"PARA LAS HOJAS RESORT "
    f"(k={k_knn}) ---"
)

print(
    "Ubicación de Referencia "
    f"(Tierra Firme): "
    f"Lat {nueva_lat}, "
    f"Lon {nueva_lon}"
)

print(
    f"Clasificación asignada: "
    f"{clase_predicha}"
)


print(
    "Hoteles vecinos reales más cercanos "
    "extraídos de OpenStreetMap:"
)


vecinos_df = df.iloc[
    indices_vecinos[0]
].copy()


vecinos_df[
    "distancia_km"
] = distancias_km


print(
    vecinos_df[
        [
            "name",
            "category",
            "zona_etiqueta",
            "distancia_km"
        ]
    ]
)


# ==========================================
# FASE D:
# MAPA INTERACTIVO
# ==========================================


mapa = folium.Map(
    location=[
        nueva_lat,
        nueva_lon
    ],
    zoom_start=13,
    tiles="Esri.WorldStreetMap"
)


colores_cluster = [
    "red",
    "blue",
    "green",
    "purple",
    "orange"
]


# Marcadores de hoteles

for _, row in df.iterrows():

    color_punto = (
        colores_cluster[
            row["cluster"]
            % len(colores_cluster)
        ]
    )


    popup_texto = (
        f"<b>{row['name']}</b><br>"
        f"Categoría: {row['category']}<br>"
        f"Cluster: {row['cluster']}<br>"
        f"Zona: {row['zona_etiqueta']}"
    )


    folium.CircleMarker(
        location=[
            row["latitude"],
            row["longitude"]
        ],

        radius=6,

        color=color_punto,

        fill=True,

        fill_color=color_punto,

        fill_opacity=0.8,

        popup=folium.Popup(
            popup_texto,
            max_width=250
        )
    ).add_to(mapa)


# Marcadores de centroides

for i, c in enumerate(
    centroides
):

    folium.Marker(
        location=[
            c[0],
            c[1]
        ],

        popup=(
            f"<b>Centroide "
            f"Cluster {i}</b>"
        ),

        icon=folium.Icon(
            color="black",
            icon="star"
        )
    ).add_to(mapa)


# Marcador principal

folium.Marker(
    location=[
        nueva_lat,
        nueva_lon
    ],

    popup=(
        "<b>LAS HOJAS RESORT "
        "(Referencia Principal)</b><br>"
        f"Clasificación KNN: "
        f"{clase_predicha}"
    ),

    icon=folium.Icon(
        color="orange",
        icon="star"
    )
).add_to(mapa)


# Líneas hacia vecinos

for _, vecino in (
    vecinos_df.iterrows()
):

    folium.PolyLine(
        locations=[
            [
                nueva_lat,
                nueva_lon
            ],
            [
                vecino["latitude"],
                vecino["longitude"]
            ]
        ],

        color="orange",

        weight=2.5,

        dash_array="5, 5",

        tooltip=(
            f"Vecino real: "
            f"{vecino['name']} "
            f"({vecino['distancia_km']:.2f} km)"
        )
    ).add_to(mapa)


# ==========================================
# LEYENDA
# ==========================================

leyenda_html = """
<div style="
position: fixed;
bottom: 30px;
left: 30px;
width: 310px;
z-index: 9999;
background-color: white;
border: 2px solid grey;
border-radius: 8px;
padding: 10px;
font-size: 13px;
">

<b>
Hotspots Hoteleros - Las Hojas
</b>

<br>

• Puntos de color:
Hoteles por Cluster K-Means

<br>

★ Marcador naranja:
Las Hojas Resort

<br>

--- Líneas naranjas:
Hoteles vecinos reales (KNN)

<br>

<small>
Fuente: OpenStreetMap / Esri
</small>

</div>
"""


mapa.get_root().html.add_child(
    folium.Element(
        leyenda_html
    )
)


# ==========================================
# GUARDAR MAPA
# ==========================================

mapa.save(
    "mapa_hotspots_la_paz.html"
)


print(
    "Mapa guardado con éxito como "
    "'mapa_hotspots_la_paz.html'."
)


mapa
