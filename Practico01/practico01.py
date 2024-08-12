import random
import pandas as pd

alturas = []
pesos = []

for _ in range(100):
    altura = round(random.uniform(1.4, 2.0), 2)  # Genera alturas entre 1.40 y 2.00 metros
    if altura < 1.5:
        peso = round(random.uniform(45, 60), 1)  # Peso para alturas bajas
    elif altura < 1.8:
        peso = round(random.uniform(55, 80), 1)  # Peso para alturas medias
    else:
        peso = round(random.uniform(70, 100), 1)  # Peso para alturas altas

    alturas.append(altura)
    pesos.append(peso)

datos = pd.DataFrame({
    'Estatura': alturas,
    'Peso': pesos
})

datos.to_csv('datos_peso_estatura.csv', index=False)

print(datos.head())
