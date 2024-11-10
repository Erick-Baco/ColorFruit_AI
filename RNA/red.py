import numpy as np
import pandas as pd


def escalon(n):
    for x in range(n.shape[0]):
        for y in range(n.shape[1]):
            n[x][y] = 1 / (1 + np.exp(n[x][y]))
    return n


df = pd.read_csv('../ARDUINO/datos_rgb.csv')
p = df[['R', 'G', 'B']].to_numpy()
a = df[['a1', 'a2', 'a3']].to_numpy()

w = np.random.rand(3, 3) - 1
b = np.random.rand(1, 3) - 1
e = np.zeros((600, 3))

for epoch in range(1000):
    for q in range(600):
        valor = escalon((np.dot(w, p[q].T) + b))
        if (valor != a[q]).all():
            e[q] = a[q] - valor
            w = w + (e[q] * p[q] * .1)
            b = b + e[q]

e_df = pd.DataFrame(e)
e_df.to_csv('pesos_e.csv', index=False, header=False)

print(w)
print(b)
print(e)


