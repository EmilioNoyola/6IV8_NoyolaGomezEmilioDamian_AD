import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Leer el archivo principal
df = pd.read_excel('ElementosBasicosEstadistica/Datos/Datos_Con_Sucursal.xlsx')

# Convertir fechas a formato datetime si es necesario
df["B_mes"] = pd.to_datetime(df["B_mes"])
df["fec_ini_cdto"] = pd.to_datetime(df["fec_ini_cdto"])

# 1. Ventas totales del comercio
ventas_totales = df["ventas_tot"].sum()

# 2. Cantidad de socios con y sin adeudo
socios_con_adeudo = df[df["B_adeudo"] == "Con adeudo"].shape[0]
socios_sin_adeudo = df[df["B_adeudo"] == "Sin adeudo"].shape[0]

# Porcentaje de socios con y sin adeudo
total_socios = socios_con_adeudo + socios_sin_adeudo
porcentaje_con_adeudo = (socios_con_adeudo / total_socios) * 100
porcentaje_sin_adeudo = (socios_sin_adeudo / total_socios) * 100

# 3. Gráfica de ventas totales respecto del tiempo
plt.figure(figsize=(10, 5))
plt.bar(df["B_mes"].astype(str), df["ventas_tot"], color="#17406d")
plt.xticks(rotation=45)
plt.xlabel("Mes")
plt.ylabel("Ventas Totales")
plt.title("Ventas Totales Respecto del Tiempo")
plt.show()

# 4. Gráfica de desviación estándar de los pagos realizados respecto del tiempo
desviacion_pagos = df.groupby("B_mes")["pagos_tot"].std()

plt.figure(figsize=(10, 5))
plt.plot(desviacion_pagos.index.astype(str), desviacion_pagos, marker="o", linestyle="-", color="#17406d")
plt.xticks(rotation=45)
plt.xlabel("Mes")
plt.ylabel("Desviación Estándar de Pagos")
plt.title("Desviación Estándar de Pagos Respecto del Tiempo")
plt.show()

# 5. Deuda total de los clientes
deuda_total = df["adeudo_actual"].sum()

# 6. Porcentaje de utilidad del comercio
porcentaje_utilidad = ((ventas_totales - deuda_total) / ventas_totales) * 100

# 7. Gráfico circular de ventas por sucursal
ventas_por_sucursal = df.groupby("suc")["ventas_tot"].sum()

plt.figure(figsize=(8, 8))
plt.pie(ventas_por_sucursal, labels=ventas_por_sucursal.index, autopct="%1.1f%%", startangle=140)
plt.title("Distribución de Ventas por Sucursal")
plt.show()

# 8. Gráfico de deudas totales por sucursal respecto del margen de utilidad
deudas_por_sucursal = df.groupby("suc")["adeudo_actual"].sum()
margen_utilidad_por_sucursal = (ventas_por_sucursal - deudas_por_sucursal) / ventas_por_sucursal * 100

fig, ax1 = plt.subplots(figsize=(10, 5))

ax1.bar(deudas_por_sucursal.index, deudas_por_sucursal, color="#0f2b48", label="Deuda Total")
ax1.set_xlabel("Sucursal")
ax1.set_ylabel("Deuda Total", color="#0f2b48")
ax1.tick_params(axis="y", labelcolor="#0f2b48")

ax2 = ax1.twinx()
ax2.plot(margen_utilidad_por_sucursal.index, margen_utilidad_por_sucursal, marker="o", linestyle="--", color="#38b6ff", label="Margen de Utilidad")
ax2.set_ylabel("Margen de Utilidad (%)", color="#38b6ff")
ax2.tick_params(axis="y", labelcolor="#38b6ff")

plt.title("Deuda Total por Sucursal vs Margen de Utilidad")
fig.tight_layout()
plt.show()

print("ANÁLISIS")
print(f"Ventas Totales del Comercio: ${ventas_totales:,.2f}")
print(f"Socios con Adeudo: {socios_con_adeudo:,}")
print(f"Socios sin Adeudo: {socios_sin_adeudo:,}")
print(f"Porcentaje de Socios con Adeudo: {porcentaje_con_adeudo:.2f}%")
print(f"Porcentaje de Socios sin Adeudo: {porcentaje_sin_adeudo:.2f}%")
print(f"Deuda Total de los Clientes: ${deuda_total:,.2f}")
print(f"Porcentaje de Utilidad del Comercio: {porcentaje_utilidad:.2f}%")
