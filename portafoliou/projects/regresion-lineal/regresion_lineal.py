import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


# ==========================================
# REGRESIÓN LINEAL
# ==========================================

data = {
    "HORAS_ESTUDIO": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "SCORE": [2, 3, 4, 5, 6, 7, 7, 8, 9, 10]
}

df = pd.DataFrame(data)

print(df)


# Variables independientes y dependientes
X = df[["HORAS_ESTUDIO"]]
y = df["SCORE"]


# Crear y entrenar el modelo
modelo = LinearRegression()
modelo.fit(X, y)


# Realizar predicciones
y_pred = modelo.predict(X)


# Mostrar resultados
print("Pendiente:", modelo.coef_[0])
print("Intercepto:", modelo.intercept_)
print("R²:", r2_score(y, y_pred))
print("MSE:", mean_squared_error(y, y_pred))


# Solicitar horas de estudio al usuario
horas = float(input("Ingrese las horas de estudio: "))


# Realizar predicción
prediccion = modelo.predict([[horas]])

print("Score predicho:", prediccion[0])


# Gráfica
plt.scatter(X, y)
plt.plot(X, y_pred)

plt.xlabel("Horas de estudio")
plt.ylabel("Score")
plt.title("Regresión Lineal")

plt.show()