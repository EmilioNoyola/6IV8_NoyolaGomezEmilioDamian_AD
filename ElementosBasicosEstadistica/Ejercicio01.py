import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
df = pd.read_csv('ElementosBasicosEstadistica/Datos/housing.csv')

# Calcular medidas estadísticas
rango = df["median_house_value"].max() - df["median_house_value"].min()
media = df["median_house_value"].mean()
mediana = df["median_house_value"].median()
moda = df["median_house_value"].mode()[0]
desviacion = df["median_house_value"].std()
varianza = df["median_house_value"].var()

# DataFrame con los resultados
tabla_estadistica = pd.DataFrame({
    "Medida": ["Rango", "Media", "Mediana", "Moda", "Desviación Estándar", "Varianza"],
    "Valor": [rango, media, mediana, moda, desviacion, varianza]
})

pd.options.display.float_format = '{:,.2f}'.format 

print(tabla_estadistica)

plt.figure(figsize=(10, 6))
plt.hist(df["median_house_value"], bins=30, alpha=0.5, label="Median House Value", color='blue')
plt.hist(df["total_bedrooms"], bins=30, alpha=0.5, label="Total Bedrooms", color='red')
plt.hist(df["population"], bins=30, alpha=0.5, label="Population", color='green')

# Línea de la media de median_house_value
plt.axvline(df["median_house_value"].mean(), color='black', linestyle='dashed', linewidth=2, label="Media Median House Value")

plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.title("Histograma Comparativo de Median House Value, Total Bedrooms y Population")
plt.legend()
plt.show()
