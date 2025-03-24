import numpy as np
import matplotlib.pyplot as plt

#Vamos a crear una semilla random para reproductibilidad
np.random.seed(0)

#Vamos a buscar los parametros para una distribución

#Media
media = 0

#Desviación Estandar
sigma1 = 1
sigma2 = 2
sigma3 = 3

#El número de muestras para el análisis 
n_muestras = 1000

#Vamos a generar los datos de las distribuciones normales
data1 = np.random.normal(media, sigma1, n_muestras)
data2 = np.random.normal(media, sigma2, n_muestras)
data3 = np.random.normal(media, sigma3, n_muestras)

#Vamos a configurar la 
plt.figure(figsize=(10, 6))

#Vamos a cargar las frecuencias a partir de un histograma 
plt.hist(data1, bins=30, alpha=0.5, label='Desviación Estandar 1', color='blue', density=True )
plt.hist(data2, bins=30, alpha=0.5, label='Desviación Estandar 2', color='red', density=True )
plt.hist(data3, bins=30, alpha=0.5, label='Desviación Estandar 3', color='green', density=True )

#Vamos a mostrar
plt.title('Comparación de Distribuciones Normales con una semilla random')
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.legend()
plt.grid()

plt.show()