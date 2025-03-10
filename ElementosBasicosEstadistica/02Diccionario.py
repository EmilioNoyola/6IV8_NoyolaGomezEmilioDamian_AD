import pandas as pd

##Escribir una función que reciba un diccionario con las notas de los estudiantes del curso y devuelve una serie con mínimo, máximo, media y desviación típica.

def estadistica_notas(notas):
    notas = pd.Series(notas)
    estadisticos = pd.Series([notas.min(), notas.max(), notas.mean(), notas.std()], index=['Min', 'Max', 'Media', 'Desviación típica'])
    return estadisticos

def aprobados(notas):
    notas = pd.Series(notas)
    return notas[notas >= 6].sort_values(ascending=False)


notas = {'Juan':9, 'María':6.5, 'Pedro':4, 'Carmen': 8.5, 'Luis': 5}

print(estadistica_notas(notas))
print(aprobados(notas))