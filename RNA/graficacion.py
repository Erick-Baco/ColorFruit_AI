
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

np.random.seed(1968801)


def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin


# malla de puntos
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)

# leyendo los puntos del archivo
df = pd.read_csv("../ARDUINO/datos_rgb.csv")

# definir 5 registros por captura de rgb
x_1 = df['R'][0:202]
y_1 = df['G'][0:202]
z_1 = df['B'][0:202]

# puntos 2
x_2 = df['R'][202:402]
y_2 = df['G'][202:402]
z_2 = df['B'][202:402]

# puntos 3
x_3 = df['R'][402:600]
y_3 = df['G'][402:600]
z_3 = df['B'][402:600]

z = 5 * x + 5 * y

z2 = 3 * x + 7 * y

# crear la figura
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# dibujar el plano
ax.plot_surface(x, y, z, alpha=0.5, rstride=100, cstride=100, color='cyan')
ax.plot_surface(x, y, z2, alpha=0.5, rstride=100, cstride=100, color='pink')

ax.scatter(x_1, y_1, z_1, marker='o', color='red')
ax.scatter(x_2, y_2, z_2, marker='o', color='green')
ax.scatter(x_3, y_3, z_3, marker='o', color='blue')

# Configurar etiquetas
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')


# Mostrar el gráfico
plt.show()