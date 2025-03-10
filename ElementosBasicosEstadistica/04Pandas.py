import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv('ElementosBasicosEstadistica/Datos/housing.csv')

#Mostrar las primeras 5 filas 
print(df.head())

#Mostrar las ultimas 5 filas
print('\n',df.tail())

#Mostrar una fila en específico
print('\n',df.iloc[7])

#Mostrar la columna ocean_proximity
print(df["ocean_proximity"])

#Obtener la media de la columna rooms
mediaCuartos = df["total_rooms"].mean()
print('La media del numero de cuartos es:', mediaCuartos)

#Obtenemos la mediana de la columna rooms
mediaCuartos = df["total_rooms"].median()
print('La mediana del numero de cuartos es:', mediaCuartos)

#Obtenemos la moda de la columna rooms
mediaCuartos = df["total_rooms"].mode()
print('La moda del numero de cuartos es:', mediaCuartos)

#La suma de popular
salarioTotal = df["population"].sum()
print('El salario total es:', salarioTotal)

#Para poder filtrar
filtro = df[df['ocean_proximity'] == 'ISLAND']
print(filtro)

plt.scatter(df['ocean_proximity'][:10], df['median_house_value'][:10])

plt.xlabel('Proximidad')
plt.ylabel('Precio')

plt.title('Grafica de disperción de proximidad al oceano vs precio')

plt.show()

