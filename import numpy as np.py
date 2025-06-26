import numpy as np
import matplotlib.pyplot as plt

# Données (exemple basé sur l'image)
scenarios = ["URBAN", "RURAL", "TOTAL"]

# Exemple de données fictives (remplacez avec vos données réelles)
sum_active_urban = [10, 15, 20, 5, 3, 53]
sum_nonactive_urban = [8, 12, 18, 4, 2, 44]
sum_public_urban = [5, 7, 10, 2, 1, 25]
sum_active_rural = [6, 9, 12, 3, 2, 32]
sum_nonactive_rural = [7, 10, 14, 3, 2, 36]
sum_public_rural = [4, 5, 7, 2, 1, 19]

electricity = [sum_active_urban[0] + sum_nonactive_urban[0] + sum_public_urban[0],
               sum_active_rural[0] + sum_nonactive_rural[0] + sum_public_rural[0],
               sum_active_urban[0] + sum_nonactive_urban[0] + sum_public_urban[0] +
               sum_active_rural[0] + sum_nonactive_rural[0] + sum_public_rural[0]]

gasoline = [sum_active_urban[1] + sum_nonactive_urban[1] + sum_public_urban[1],
            sum_active_rural[1] + sum_nonactive_rural[1] + sum_public_rural[1],
            sum_active_urban[1] + sum_nonactive_urban[1] + sum_public_urban[1] +
            sum_active_rural[1] + sum_nonactive_rural[1] + sum_public_rural[1]]

diesel = [sum_active_urban[2] + sum_nonactive_urban[2] + sum_public_urban[2],
          sum_active_rural[2] + sum_nonactive_rural[2] + sum_public_rural[2],
          sum_active_urban[2] + sum_nonactive_urban[2] + sum_public_urban[2] +
          sum_active_rural[2] + sum_nonactive_rural[2] + sum_public_rural[2]]

gas = [sum_active_urban[3] + sum_nonactive_urban[3] + sum_public_urban[3],
       sum_active_rural[3] + sum_nonactive_rural[3] + sum_public_rural[3],
       sum_active_urban[3] + sum_nonactive_urban[3] + sum_public_urban[3] +
       sum_active_rural[3] + sum_nonactive_rural[3] + sum_public_rural[3]]

hydrogen = [sum_active_urban[4] + sum_nonactive_urban[4] + sum_public_urban[4],
            sum_active_rural[4] + sum_nonactive_rural[4] + sum_public_rural[4],
            sum_active_urban[4] + sum_nonactive_urban[4] + sum_public_urban[4] +
            sum_active_rural[4] + sum_nonactive_rural[4] + sum_public_rural[4]]

total = [sum_active_urban[-1] + sum_nonactive_urban[-1] + sum_public_urban[-1],
         sum_active_rural[-1] + sum_nonactive_rural[-1] + sum_public_rural[-1],
         sum_active_urban[-1] + sum_nonactive_urban[-1] + sum_public_urban[-1] +
         sum_active_rural[-1] + sum_nonactive_rural[-1] + sum_public_rural[-1]]

# Bar width and x positions
x = np.arange(len(scenarios))
width = 0.1  # Ajustement de la largeur des barres

# Création de la figure et des axes
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(x - 2.5*width, electricity, width, label="Electricity", color="#1f77b4")
ax.bar(x - 1.5*width, gasoline, width, label="Gasoline", color="#ff7f0e")
ax.bar(x - 0.5*width, diesel, width, label="Diesel", color="#2ca02c")
ax.bar(x + 0.5*width, gas, width, label="Natural Gas", color="#d62728")
ax.bar(x + 1.5*width, hydrogen, width, label="Hydrogen", color="#9467bd")
ax.bar(x + 2.5*width, total, width, label="Total", color="#8c564b")

# Labels et titres
ax.set_ylabel("Final energy consumption [TWh]", fontsize=14)
ax.set_title("Final energy consumption in the transport sector", fontsize=16)
ax.set_xticks(x)
ax.set_xticklabels(scenarios, fontsize=12)
ax.legend(loc="upper right", fontsize=12)

# Style
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.show()
