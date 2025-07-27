import pandas as pd
import matplotlib.pyplot as plt

#Cargar los archivos CSV
ventas_df = pd.read_csv("RPY3_ventas.txt")       
divisas_df = pd.read_csv("RPY3_divisas.txt")     

#Convertir la columna "Fecha" a tipo datetime
ventas_df["Fecha"] = pd.to_datetime(ventas_df["Fecha"])
divisas_df["Fecha"] = pd.to_datetime(divisas_df["Fecha"])

#Unir las dos tablas por la columna "Fecha"
merged_df = ventas_df.merge(divisas_df, on="Fecha", how="left")

#Convertir todas las ventas a pesos colombianos (COP)
def convertir_a_cop(row):
    if row["Moneda"] == "USD":
        return row["Ventas"] * row["USDCOP"]  # Dólares a COP
    elif row["Moneda"] == "EUR":
        return row["Ventas"] * row["EURCOP"]  # Euros a COP
    else:
        return row["Ventas"]  # Ya está en COP (para Empresa C)

merged_df["Ventas_COP"] = merged_df.apply(convertir_a_cop, axis=1)

#Crear una nueva columna con el mes (año-mes)
merged_df["Mes"] = merged_df["Fecha"].dt.to_period("M")

# ======================================
# ENUNCIADO A:
# Resumir y graficar los valores de venta mensuales por empresa en COP
# ======================================

ventas_mensuales = merged_df.groupby(["Empresa", "Mes"])["Ventas_COP"].sum().unstack("Empresa")

#Graficar las ventas mensuales por empresa
ventas_mensuales.plot(kind="bar", figsize=(14, 6), title="Ventas mensuales por empresa en COP")
plt.ylabel("Ventas en COP")
plt.xlabel("Mes")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# ======================================
# ENUNCIADO B:
# Identificar la empresa con mayores ventas para el año 2020
# ======================================

#Calcular ventas totales anuales por empresa
ventas_totales_2020 = merged_df.groupby("Empresa")["Ventas_COP"].sum()
print("Ventas totales 2020 por empresa (COP):")
print(ventas_totales_2020)

# ======================================
# ENUNCIADO C:
# ¿Cuál fue el mes de mayor crecimiento del mercado total?
# ======================================

#Calcular crecimiento mensual del mercado total
# Sumar ventas de todas las empresas por mes
ventas_totales_mes = ventas_mensuales.sum(axis=1)

# Calcular el porcentaje de crecimiento mes a mes
crecimiento_mensual = ventas_totales_mes.pct_change().dropna()

# Encontrar el mes con mayor crecimiento
mes_max_crecimiento = crecimiento_mensual.idxmax()
max_crecimiento = crecimiento_mensual.max()

print(f"\nMes con mayor crecimiento del mercado: {mes_max_crecimiento} ({max_crecimiento:.2%})")
