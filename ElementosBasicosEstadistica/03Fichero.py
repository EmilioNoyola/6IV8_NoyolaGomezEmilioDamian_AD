import pandas as pd

def resumen_cotizacion(fichero):
    df = pd.read_csv(fichero, sep=';', decimal=',', thousands='.', index_col=0)
    return pd.DataFrame([df.min(), df.max(), df.mean(), df.std()], index=['Mínimo', 'Máximo', 'Media', 'Desviación Estandar'])

print(resumen_cotizacion('./ElementosBasicosEstadistica/Datos/cotizacion.csv'))