"""
Seguimiento del peso de pacientes en una clínica de nutrición
Una clínica de nutrición desea analizar el progreso semanal de
uno de sus pacientes, "Carlos", durante 8 semanas. Se tiene 
la siguiente información del peso (en kg) registrado cada lunes:

Usando pandas.Series, responde lo siguiente:
    ¿Cuánto peso perdió en total durante las 8 semanas?
    ¿En qué semana bajó más de peso respecto a la semana anterior?
    ¿Hubo alguna semana en la que subió de peso? Si es así, ¿cuál?
    Muestra una serie nueva que contenga la diferencia de peso semana a semana.
    ¿Cuál fue el peso promedio durante todo el programa?
"""
import pandas as pd

# Datos del paciente Carlos
pesos = [82.5, 81.9, 81.0, 80.8, 80.0, 79.5, 79.2, 78.9]
semanas = [f"Semana {i}" for i in range(1, 9)]

# Crear la Serie
serie_peso = pd.Series(pesos, index=semanas)

# Mostrar serie original
print("📊 Peso por semana:")
print(serie_peso)
print()

# 1. Peso perdido total
perdida_total = serie_peso.iloc[0] - serie_peso.iloc[-1]
print(f"1️⃣ Peso perdido en total: {perdida_total:.2f} kg")

# 2. Semana con mayor bajada
diferencias = serie_peso.diff()
semana_mayor_bajada = diferencias.idxmin()
print(f"2️⃣ Mayor bajada fue en {semana_mayor_bajada}: {diferencias[semana_mayor_bajada]:.2f} kg")

# 3. ¿Subió de peso alguna semana?
subidas = diferencias[diferencias > 0]
if not subidas.empty:
    print("3️⃣ Semanas donde subió de peso:")
    print(subidas)
else:
    print("3️⃣ No hubo semanas con subida de peso.")

# 4. Serie con diferencia semanal
print("\n4️⃣ Diferencia de peso semana a semana:")
print(diferencias)

# 5. Peso promedio
peso_promedio = serie_peso.mean()
print(f"\n5️⃣ Peso promedio: {peso_promedio:.2f} kg")
